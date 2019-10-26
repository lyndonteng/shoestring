import socket
import time

HOST = '127.0.0.1'
PORT = 65432


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        time.sleep(5)
        s.sendall(b'zoom 5')
        time.sleep(1)
        s.sendall(b'up 10')
        time.sleep(1)
        s.sendall(b'down 10')
        time.sleep(1)
        s.sendall(b'left 10')
        time.sleep(1)
        s.sendall(b'right 10')
        time.sleep(1)
        s.sendall(b'clockwise 90')
        time.sleep(1)
        s.sendall(b'anticlockwise 90')
        time.sleep(1)
        s.sendall(b'fit')
        s.close()


if __name__ == '__main__':
    main()
