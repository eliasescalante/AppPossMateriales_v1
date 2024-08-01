import socket
import json

def consultar_producto(producto):
    """
    Consulta un producto en la base de datos.
    """
    # conecto al LocalHost para comenzar la conexion al puerto para enlazar con el servidor
    HOST, PORT = "LocalHost", 9999
    
    try:
        # Creo un socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Conecto al servidor especificado en HOST y PORT
            sock.connect((HOST, PORT))
            request = {
                "action": "consultar",
                "product": producto
            }
            # Envio la solicitud al servidor en formato JSON
            sock.sendall(json.dumps(request).encode('utf-8'))
            
            # recibo la respuesta del servidor
            response = sock.recv(4096)
            if response:
                # convierto la respuesta de JSON a un diccionario
                response_data = json.loads(response.decode('utf-8'))
                print(response_data)
            else:
                print("No se recibió respuesta del servidor.")
    except Exception as e:
        # manejar cualquier excepcion que ocurra durante la conexion
        print(f"Error al conectar con el servidor: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    #solicito al usuario el nombre del producto a consultar
    producto = input("Ingrese el nombre del producto a consultar: ")
    consultar_producto(producto)
