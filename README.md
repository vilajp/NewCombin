# NewCombin

Se cuenta con 2 solo endpoints:

get(http://192.168.1.132:8000/facturas) para traer todas las facturas cargadas

post(http://192.168.1.132:8000/factura) para cargar una nueva factura.
{
    "tipo_servicio": "Escuelas Privadas",
    "descripcion_servicio": "Otto Kraus",
    "fecha_vencimiento": "2021-03-30 00:00:00",
    "importe_servicio": 10000.45,
    "status_del_pago": "Pendiente",
    "codigo_barras": 7792057999999988
}
