from keyboard import *
import socket
import time

HOST = ''
PORT = 13000


def zoom_in():
    SendInput(Keyboard(VK_CONTROL), Keyboard(VK_OEM_PLUS))
    time.sleep(0.2)
    SendInput(Keyboard(VK_CONTROL, KEYEVENTF_KEYUP))
    SendInput(Keyboard(VK_OEM_PLUS, KEYEVENTF_KEYUP))


def zoom_out():
    SendInput(Keyboard(VK_CONTROL), Keyboard(VK_OEM_MINUS))
    time.sleep(0.2)
    SendInput(Keyboard(VK_OEM_PLUS, KEYEVENTF_KEYUP))
    SendInput(Keyboard(VK_CONTROL, KEYEVENTF_KEYUP))


def up():
    SendInput(Keyboard(VK_UP))
    time.sleep(0.2)
    SendInput(Keyboard(VK_UP, KEYEVENTF_KEYUP))


def down():
    SendInput(Keyboard(VK_DOWN))
    time.sleep(0.2)
    SendInput(Keyboard(VK_DOWN, KEYEVENTF_KEYUP))


def left():
    SendInput(Keyboard(VK_LEFT))
    time.sleep(0.2)
    SendInput(Keyboard(VK_LEFT, KEYEVENTF_KEYUP))


def right():
    SendInput(Keyboard(VK_RIGHT))
    time.sleep(0.2)
    SendInput(Keyboard(VK_RIGHT, KEYEVENTF_KEYUP))


def clockwise():
    SendInput(Keyboard(VK_SHIFT), Keyboard(VK_CONTROL), Keyboard(VK_OEM_PLUS))
    time.sleep(0.2)
    SendInput(Keyboard(VK_OEM_PLUS, KEYEVENTF_KEYUP))
    SendInput(Keyboard(VK_CONTROL, KEYEVENTF_KEYUP))
    SendInput(Keyboard(VK_SHIFT, KEYEVENTF_KEYUP))


def anticlockwise():
    SendInput(Keyboard(VK_SHIFT), Keyboard(VK_CONTROL), Keyboard(VK_OEM_MINUS))
    time.sleep(0.2)
    SendInput(Keyboard(VK_OEM_MINUS, KEYEVENTF_KEYUP))
    SendInput(Keyboard(VK_CONTROL, KEYEVENTF_KEYUP))
    SendInput(Keyboard(VK_SHIFT, KEYEVENTF_KEYUP))


def previous_page():
    SendInput(Keyboard(VK_PRIOR))
    time.sleep(0.2)
    SendInput(Keyboard(VK_PRIOR, KEYEVENTF_KEYUP))


def next_page():
    SendInput(Keyboard(VK_NEXT))
    time.sleep(0.2)
    SendInput(Keyboard(VK_NEXT, KEYEVENTF_KEYUP))


def zoom_fit_to_width():
    SendInput(Keyboard(VK_CONTROL), Keyboard(KEY_3))
    time.sleep(0.2)
    SendInput(Keyboard(KEY_3, KEYEVENTF_KEYUP))
    SendInput(Keyboard(VK_CONTROL, KEYEVENTF_KEYUP))


def zoom_fit_to_page():
    SendInput(Keyboard(VK_CONTROL), Keyboard(KEY_0))
    time.sleep(0.2)
    SendInput(Keyboard(KEY_0, KEYEVENTF_KEYUP))
    SendInput(Keyboard(VK_CONTROL, KEYEVENTF_KEYUP))


def text_to_command(texts):
    commands = {
        "big": zoom_in,
        "bigger": zoom_in,
        "expand": zoom_in,
        "larger": zoom_in,
        "large": zoom_in,
        "small": zoom_out,
        "smaller": zoom_out,
        "up": up,
        "down": down,
        "left": left,
        "right": right,
        "clockwise": clockwise,
        "anticlockwise": anticlockwise,
        "anti": anticlockwise,
        "previous": previous_page,
        "back": previous_page,
        "next": next_page,
        "with": zoom_fit_to_width,
        "width": zoom_fit_to_width,
        "page": zoom_fit_to_page
    }
    
    for i, text in enumerate(texts):
        if text in commands:
            try:
                commands[text]()
                time.sleep(1)
            except KeyError:
                pass


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    print("Connection established.")
    while True:
        data, addr = s.recvfrom(1024)
        texts = data.decode('utf-8').rstrip().lower().split()
        print(texts)
        text_to_command(texts)


if __name__ == '__main__':
    main()
