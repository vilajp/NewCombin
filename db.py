import sqlite3
DATABASE_NAME = "facturas.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        '''CREATE TABLE IF NOT EXISTS facturas(
                tipo_servicio TEXT NOT NULL,
                descripcion_servicio TEXT NOT NULL,
                fecha_vencimiento DATE NOT NULL,
                importe_servicio REAL NOT NULL,
                status_del_pago TEXT NOT NULL,
                codigo_barras  INTEGER NOT NULL UNIQUE,  
                id INTEGER PRIMARY KEY AUTOINCREMENT
                )''',

        '''CREATE TABLE IF NOT EXISTS transactions(
                metodo_de_pago TEXT NOT NULL,
                numero_de_tarjeta INTEGER,
                importe_pago INTEGER NOT NULL,
                codigo_barras INTEGER NOT NULL,
                fecha_de_pago TEXT NOT NULL,
                id INTEGER PRIMARY KEY AUTOINCREMENT
                )'''
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
