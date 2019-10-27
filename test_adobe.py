import socket
import time
# from [STT module] import f

HOST = '127.0.0.1'
PORT = 65432

### this needs to go into the STT file
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    print()  # output of STT engine here3

def main(f):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        time.sleep(5)
        s.sendall(f)
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
    main(f)
