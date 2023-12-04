import socket


TCP_IP = "127.0.0.1"
TCP_PORT = 8080


def run_client(ip=TCP_IP, port=TCP_PORT):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server = ip, port
        sock.connect(server)
        print(f'Connection established {server}')

        message = input("Message: ")

        sock.send(message.encode())
        print(f"Message: {message} sent to server: {server}")

        response = sock.recv(4)
        if response.decode() == "OK":
            print(f"Data transfer from {server} completed")
        else:
            print("Something went wrong!!!")


if __name__ == "__main__":
    run_client(TCP_IP, TCP_PORT)