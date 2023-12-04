import socket


TCP_IP = "localhost"
TCP_PORT = 8080
MESSAGE = "Python Web development"


def run_client(ip: str, port: str):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'Connection established {server}')
        while True:
            user_input = input(">>> ")
            if user_input == "stop":
                break
            sock.send(user_input.encode())
            print(f"Data: {user_input} sent to server: {server}")
            data = sock.recv(1024)
            print(f"Received data: {data.decode()} from server: {server}")
    
    print(f'Data transfer completed')

if __name__ == "__main__":
    run_client(TCP_IP, TCP_PORT)