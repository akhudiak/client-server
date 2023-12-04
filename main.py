from client import run_client
from server import run_server
from threading import Thread


while True:
    server_port = input("\nServer port: ")

    try:
        server_port = int(server_port)
    except ValueError:
        print("Port must be str. Good bye!")
        break

    client_thread = Thread(target=run_client, kwargs={"port": server_port})
    server_thread = Thread(target=run_server, kwargs={"port": server_port})
    client_thread.start()
    server_thread.start()
    client_thread.join()
    server_thread.join()