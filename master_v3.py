from microbit import *

import radio
import random
import music

radio.on()
radio.config(channel = 26, address = 0x27182818)

pins = [pin2, pin1, pin8]

r = pins[0]
g = pins[1]
b = pins[2]

msg = ["0 0", "0 0"]
positions = ['tl', 'tr', 'bl', 'br']
images = [Image.ARROW_NW, Image.ARROW_NE, Image.ARROW_SW, Image.ARROW_SE]

currentNum = random.randint(0, 3)
lastTime = running_time()

timeDif = 2000

for p in [pin2, pin1, pin8]:
    p.write_analog(0)

def getNextDab(currentNum):
    if currentNum == 0:
        return random.randint(1, 3)
    elif currentNum == 1:
        n = random.randint(1, 3)
        return n if n != 1 else 0
    elif currentNum == 2:
        n = random.randint(0, 2)
        return n if n != 2 else 3
    else:
        return random.randint(0, 2)

def getValidDab(position, msg):
    bend = [m[0] == "1" for m in msg]
    pitch = [0, 0]

    try:
        pitch = [float(m[2:]) for m in msg]
    except ValueError:
        return True
    
    if position[1] == "l":
        if bend[0] or not bend[1]:
            return False
    else:
        if not bend[0] or bend[1]:
            return False
    
    if position[0] == "t":
        return pitch[0] > 20 and pitch[1] > 20
    else:
        return pitch[0] < -20 and pitch[1] < -20
        
while True:
    try:
        newMsg = radio.receive()
    except Exception as e:
        #Removes the radio messages that were causing it to crash
        radio.receive_bytes()
    
    #print(newMsg)
    
    display.show(images[currentNum])
    
    if newMsg and isinstance(newMsg, str):
        newMsg = newMsg.split(" ")
        msg[0 if newMsg[0] == "L" else 1] = " ".join(newMsg[1:3])
    
    if running_time() - lastTime > timeDif:
        #print(msg)
        
        if getValidDab(positions[currentNum], msg):
            #music.play(music.POWER_UP, wait=False)
            print("tick")
            timeDif = max(500, timeDif - 50)
            r.write_digital(0)
            g.write_digital(1)
            b.write_digital(0)
        else:
            #music.play(music.POWER_DOWN, wait=False)
            print("cross")
            r.write_digital(1)
            g.write_digital(0)
            b.write_digital(0)
        
        lastTime = running_time()
        
        currentNum = getNextDab(currentNum)
        print(positions[currentNum])
        
        