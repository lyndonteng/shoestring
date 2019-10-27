import socket
import time

HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        time.sleep(5)
        s.sendall(b"hello")
        # time.sleep(0.1)
        # s.sendall(b'out')
        # time.sleep(1)
        # s.sendall(b'up')
        # time.sleep(1)
        # s.sendall(b'down')
        # time.sleep(1)
        # s.sendall(b'left')
        # time.sleep(1)
        # s.sendall(b'right')
        # time.sleep(1)
        # s.sendall(b'clockwise')
        # time.sleep(1)
        # s.sendall(b'anticlockwise')
        # time.sleep(1)
        # s.sendall(b'previous')
        # time.sleep(1)
        # s.sendall(b'next')
        # time.sleep(1)
        # s.sendall(b'width')
        # time.sleep(1)
        # s.sendall(b'page')
        s.close()


if __name__ == '__main__':
    main()
