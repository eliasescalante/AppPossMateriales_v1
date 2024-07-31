import socket
import json

def consultar_producto(producto):
    # Cambia esta dirección IP a la IP de tu PC donde se ejecuta el servidor
    HOST, PORT = "LocalHost", 9999  # Reemplaza IP_DEL_SERVIDOR con la IP del servidor
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            request = {
                "action": "consultar",
                "product": producto
            }
            # Enviar la solicitud al servidor
            sock.sendall(json.dumps(request).encode('utf-8'))
            
            # Recibir la respuesta del servidor
            response = sock.recv(4096)
            if response:
                response_data = json.loads(response.decode('utf-8'))
                print(response_data)
            else:
                print("No se recibió respuesta del servidor.")
    except Exception as e:
        print(f"Error al conectar con el servidor: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    producto = input("Ingrese el nombre del producto a consultar: ")
    consultar_producto(producto)


