from flask import Flask, jsonify, request
import factura_controller
from db import create_tables

app = Flask(__name__)


@app.route('/facturas', methods=["GET"])
def get_facturas():
    facturas = factura_controller.get_facturas()
    return jsonify(facturas)


@app.route("/factura", methods=["POST"])
def insert_factura():
    factura_details = request.get_json()
    tipo_servicio = factura_details["tipo_servicio"]
    descripcion_servicio = factura_details["descripcion_servicio"]
    fecha_vencimiento =factura_details["fecha_vencimiento"]
    importe_servicio =factura_details["importe_servicio"]
    status_del_pago =factura_details["status_del_pago"]
    codigo_barras =factura_details["codigo_barras"]
    result = factura_controller.insert_factura(tipo_servicio, 
                                            descripcion_servicio, 
                                            fecha_vencimiento, 
                                            importe_servicio,
                                            status_del_pago,
                                            codigo_barras)
    return jsonify(result)

@app.route("/factura/pago", methods=["POST"])
def insert_transaction():
    transaction_details = request.get_json()
    metodo_de_pago = transaction_details["metodo_de_pago"]
    numero_de_tarjeta = transaction_details["numero_de_tarjeta"]
    importe_pago =transaction_details["importe_pago"]
    codigo_barras =transaction_details["codigo_barras"]
    fecha_de_pago = transaction_details["fecha_de_pago"]
    result = factura_controller.insert_transaction(metodo_de_pago,
                                            numero_de_tarjeta,
                                            importe_pago,
                                            codigo_barras,
                                            fecha_de_pago)
    return jsonify(result)


@app.route("/factura", methods=["PUT"])
def update_factura():
    factura_details = request.get_json()
    id = factura_details["id"]
    tipo_servicio = factura_details["tipo_servicio"]
    descripcion_servicio = factura_details["descripcion_servicio"]
    fecha_vencimiento =factura_details["fecha_vencimiento"]
    importe_servicio =factura_details["importe_servicio"]
    status_del_pago =factura_details["status_del_pago"]
    codigo_barras =factura_details["codigo_barras"]
    result = factura_controller.update_factura(id, tipo_servicio, 
                            descripcion_servicio, 
                            fecha_vencimiento,
                            importe_servicio,
                            status_del_pago,
                            codigo_barras)
    return jsonify(result)


@app.route("/factura/<id>", methods=["DELETE"])
def delete_factura(id):
    result = factura_controller.delete_factura(id)
    return jsonify(result)


@app.route("/factura/<id>", methods=["GET"])
def get_factura_by_id(id):
    factura = factura_controller.get_by_id(id)
    return jsonify(factura)




if __name__ == "__main__":
    create_tables()
    
    app.run(host='0.0.0.0', port=8000, debug=False)
