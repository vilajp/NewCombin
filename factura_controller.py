from db import get_db


def insert_factura(tipo_servicio, 
                    descripcion_servicio, 
                    fecha_vencimiento,
                    importe_servicio,
                    status_del_pago,
                    codigo_barras):
    db = get_db()
    cursor = db.cursor()
    statement = '''INSERT INTO facturas(tipo_servicio, 
                                    descripcion_servicio, 
                                    fecha_vencimiento,
                                    importe_servicio,
                                    status_del_pago,
                                    codigo_barras) VALUES (?, ?, ?, ?, ?, ?)'''
    cursor.execute(statement, [tipo_servicio, descripcion_servicio, fecha_vencimiento, importe_servicio, status_del_pago, codigo_barras])
    db.commit()
    return True

def insert_transaction(metodo_de_pago,
                    numero_de_tarjeta,
                    importe_pago,
                    codigo_barras,
                    fecha_de_pago):
    db = get_db()
    cursor = db.cursor() 
    statement = '''SELECT id, 
                            tipo_servicio, 
                            descripcion_servicio, 
                            fecha_vencimiento,
                            importe_servicio,
                            status_del_pago,
                            codigo_barras FROM facturas WHERE codigo_barras = ?'''
    cursor.execute(statement, [codigo_barras])
    factura = cursor.fetchone()
    if factura[4]==importe_pago:
        statement = '''INSERT INTO transactions(metodo_de_pago,
                        numero_de_tarjeta,
                        importe_pago,
                        codigo_barras,
                        fecha_de_pago) VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(statement, [metodo_de_pago,
                        numero_de_tarjeta,
                        importe_pago,
                        codigo_barras,
                        fecha_de_pago])
        statement = '''UPDATE facturas SET 
                                status_del_pago = ?,
                                WHERE id = ?'''
        cursor.execute(statement, ["paid", factura[0] ])
        db.commit()
    else:
        return {"Error":"No coincide importe de factura", "adeudado":factura[4], "pagado":importe_pago}
    return True

def update_factura(id, tipo_servicio, 
                        descripcion_servicio, 
                        fecha_vencimiento,
                        importe_servicio,
                        status_del_pago,
                        codigo_barras):
    db = get_db()
    cursor = db.cursor()
    statement = '''UPDATE facturas SET tipo_servicio = ?, 
                                descripcion_servicio = ?, 
                                fecha_vencimiento = ?,
                                importe_servicio = ?,
                                status_del_pago = ?,
                                codigo_barras=? WHERE id = ?'''
    cursor.execute(statement, [tipo_servicio, 
                                descripcion_servicio, 
                                fecha_vencimiento,
                                importe_servicio,
                                status_del_pago,
                                codigo_barras, id])
    db.commit()
    return True


def delete_factura(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM facturas WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = '''SELECT id, 
                            tipo_servicio, 
                            descripcion_servicio, 
                            fecha_vencimiento,
                            importe_servicio,
                            status_del_pago,
                            codigo_barras FROM facturas WHERE id = ?'''
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_facturas():
    db = get_db()
    cursor = db.cursor()
    query = '''SELECT id, tipo_servicio, 
                                    descripcion_servicio, 
                                    fecha_vencimiento,
                                    importe_servicio,
                                    status_del_pago,
                                    codigo_barras FROM facturas'''
    cursor.execute(query)
    return cursor.fetchall()
