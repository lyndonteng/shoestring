from pyautocad import Autocad, APoint
import socket
import time
from functools import partial

#Connect python to AutoCAD
acad = Autocad() 
acad.prompt("Hello, Autocad from Python\n")
#acad.doc returns ActiveDocument: Returns a Document object that represents the the document with the focus. If there are no documents open, an error occurs. 
print (acad.doc.Name)


#Our example command is to draw a line from (0,0) to (5,5)
# command_str = 'ucs z 90 ' #Notice that the last SPACE is equivalent to hiting ENTER
#You should separate the command's arguments also with SPACE

#Send the command to the drawing
# acad.doc.SendCommand(command_str)


HOST = '127.0.0.1'
PORT = 65432


def zoom(x):
    command_str = 'zoom ' + str(x) + ' '
    acad.doc.SendCommand(command_str)
    

def up(x):
    command_str = '-pan 0,' + str(x) + '  '
    acad.doc.SendCommand(command_str)
    

def down(x):
    command_str = '-pan 0,-' + str(x) + '  '
    acad.doc.SendCommand(command_str)


def left(x):
    command_str = '-pan -' + str(x) + ',0  '
    acad.doc.SendCommand(command_str)


def right(x):
    command_str = '-pan ' + str(x) + ',0  '
    acad.doc.SendCommand(command_str)
    

def clockwise(x):
    command_str = 'ucs z -' + str(x) + ' plan  '
    acad.doc.SendCommand(command_str)


def anticlockwise(x):
    command_str = 'ucs z ' + str(x) + ' plan  '
    acad.doc.SendCommand(command_str)


def zoom_fit():
    command_str = 'zoom O all  '
    acad.doc.SendCommand(command_str)


def run_command(cmd, x):
    commands = {
        "zoom": partial(zoom, x),
        "up": partial(up, x),
        "down": partial(down, x),
        "left": partial(left, x),
        "right": partial(right, x),
        "clockwise": partial(clockwise, x),
        "anticlockwise": partial(anticlockwise, x),
        "fit": zoom_fit
    }
    try:
        commands[cmd]()
    except KeyError:
        pass


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print("Connection established.")
        with conn:
            while True:
                data = conn.recv(1024)
                cmds = data.decode('utf-8').rstrip().lower().split()
                if len(cmds) == 1:
                    cmd = cmds[0]
                    x = None
                else:
                    cmd = cmds[0]
                    x = cmds[1]
                print(cmds)
                run_command(cmd, x)


if __name__ == '__main__':
    main()
