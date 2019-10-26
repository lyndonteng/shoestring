from keyboard import *
import time


def go_down():
    time.sleep(3)
    SendInput(Keyboard(VK_DOWN))
    time.sleep(0.2)
    SendInput(Keyboard(VK_DOWN))
    time.sleep(0.2)
    SendInput(Keyboard(VK_DOWN, KEYEVENTF_KEYUP))


if __name__ == '__main__':
    go_down()
