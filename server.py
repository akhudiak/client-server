import concurrent.futures as cf
import socket


TCP_IP = "127.0.0.1"
TCP_PORT = 8080


def run_server(ip=TCP_IP, port=TCP_PORT):

    def handle(sock: socket.socket, address: str):

        print(f'Connection established {address}')

        data = sock.recv(1024)

        print(f"Received data: {data.decode()} from: {address}")
        response = "OK"
        sock.send(response.encode())
        print(f"Response {response} sent")
        
        print(f'Socket connection closed {address}')
        sock.close()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = ip, port
    sock.bind(server)
    sock.listen(1)
    print(f'Start echo server {sock.getsockname()}')

    try:
        new_sock, address = sock.accept()
        handle(new_sock, address)
    except KeyboardInterrupt:
        print("Server destroyed")
    finally:
        sock.close()

    return address


if __name__ == "__main__":
    run_server(TCP_IP, TCP_PORT)