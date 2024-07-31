import socketserver
from modelo import BaseDatos
import json
from decoradores import log_evento

@log_evento
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recibir datos del cliente
        self.data = self.request.recv(1024).strip()
        print(f"Recibido: {self.data}")

        try:
            # Convertir datos a JSON
            request = json.loads(self.data.decode('utf-8'))
            action = request.get('action')
            product_name = request.get('product')

            response = {}
            if action == 'consultar' and product_name:
                productos = BaseDatos.select().where(BaseDatos.producto.contains(product_name))
                if productos:
                    response['status'] = 'success'
                    response['data'] = [
                        {
                            'id': p.id,
                            'producto': p.producto,
                            'stock': p.stock,
                            'costo': float(p.costo),  # Convertir Decimal a float
                            'venta': float(p.venta),  # Convertir Decimal a float
                            'proveedor': p.proveedor
                        } for p in productos
                    ]
                else:
                    response['status'] = 'error'
                    response['message'] = f"No se encontraron resultados para {product_name}"
            else:
                response['status'] = 'error'
                response['message'] = 'Acción no válida o faltan parámetros'
        except Exception as e:
            response = {
                'status': 'error',
                'message': str(e)
            }

        # Enviar respuesta al cliente
        response_data = json.dumps(response)
        print(f"Enviando: {response_data}")
        self.request.sendall(response_data.encode('utf-8'))

if __name__ == "__main__":
    HOST, PORT = "LocalHost", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print("Servidor iniciado en {}:{}".format(HOST, PORT))
        server.serve_forever()
