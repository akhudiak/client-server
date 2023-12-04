import concurrent.futures as cf
import socket


TCP_IP = "localhost"
TCP_PORT = 8080


def run_server(ip, port):

    def handle(sock: socket.socket, address: str):

        print(f'Connection established {address}')

        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode()} from: {address}")
            sock.send(data)
            print(f"Data: {data.decode()} sent to: {address}")
        
        print(f'Socket connection closed {address}')
        sock.close()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = ip, port
    sock.bind(server)
    sock.listen(10)
    print(f'Start echo server {sock.getsockname()}')

    with cf.ThreadPoolExecutor(10) as server_threads:

        try:
            while True:
                    new_sock, address = sock.accept()
                    server_threads.submit(handle, new_sock, address)
        except KeyboardInterrupt:
            print("Server destroyed")
        finally:
            sock.close()


if __name__ == "__main__":
    run_server(TCP_IP, TCP_PORT)