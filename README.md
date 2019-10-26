# shoestring
Digital Shoestring Hackathon 

## Sending keyboard inputs (Windows)

Use `SendInput(Keyboard(KEY))` to press keys and `SendInput(Keyboard(KEY, KEYEVENTF_KEYUP))` to release keys.
Replace `KEY` with the desired key.

Useful keys:

`VK_CONTROL, VK_SHIFT, VK_MENU, VK_DOWN` etc.

Example:

```python
from keyboard import *
import time

def go_down():
    time.sleep(3)
    SendInput(Keyboard(VK_DOWN))
    time.sleep(0.2)
    SendInput(Keyboard(VK_DOWN, KEYEVENTF_KEYUP))
    
if __name__ == '__main__':
    go_down()

```