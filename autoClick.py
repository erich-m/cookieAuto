import pyautogui as gui
import threading

gui.FAILSAFE = False

x = 250
y = 350

gui.moveTo(0,0)
gui.moveTo(x,y)

offset = 0

print(gui.position())

def worker(argument):
    while str(gui.position()) == 'Point(x=250, y=350)':
        gui.doubleClick()
    return

threadCount = 45
for t in range(threadCount):
    thread = threading.Thread(target=worker, args=[t])
    thread.start()
