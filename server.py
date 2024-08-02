import socketserver
from modelo import BaseDatos
import json
from decoradores import log_evento
from my_logging import setup_logging

# Configuración del logging
logger = setup_logging()

@log_evento
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    clase para manejar las solicitudes del cliente
    """
    def handle(self):
        # recibo datos del cliente
        self.data = self.request.recv(1024).strip()
        print(f"Recibido: {self.data}")
        logger.info(f"Recibido: {self.data}")

        try:
            # Convierto a JSON
            request = json.loads(self.data.decode('utf-8'))
            action = request.get('action')
            product_name = request.get('product')

            response = {}
            if action == 'consultar' and product_name:
                # consulto la DB para encontrar productos que coincidan
                productos = BaseDatos.select().where(BaseDatos.producto.contains(product_name))
                if productos:
                    # creo la respuesta de la consulta con los valores encontrados
                    response['Estado de la consulta'] = 'exitoso'
                    response['consulta'] = [
                        {
                            'id': p.id,
                            'producto': p.producto,
                            'stock': p.stock,
                            'costo': float(p.costo),
                            'venta': float(p.venta), 
                            'proveedor': p.proveedor
                        } for p in productos
                    ]
                else:
                    # si no se encontro el producto envio msj
                    response['status'] = 'error'
                    response['message'] = f"No se encontraron resultados para {product_name}"
            else:
                # accion no valida o con parametros faltantes
                response['status'] = 'error'
                response['message'] = 'Acción no válida o faltan parámetros'
        except Exception as e:
            #para manejar cualquier excepcion y dar un msj
            response = {
                'status': 'error',
                'message': str(e)
            }
            print(f"Error procesando solicitud: {e}")
            logger.error(f"Error procesando solicitud: {e}")

        # Envio la respuesta al cliente
        # convierto la respuesta a JSON y la envio al cliente
        response_data = json.dumps(response)
        print(f"Enviando: {response_data}")
        logger.info(f"Enviando: {response_data}")
        self.request.sendall(response_data.encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "LocalHost", 9999
    # creo y ejecuto el servidor TCP
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print("Servidor iniciado en {}:{}".format(HOST, PORT))
        logger.info("Servidor iniciado en {}:{}".format(HOST, PORT))
        server.serve_forever()