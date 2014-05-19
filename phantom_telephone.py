import time
import os
import RPi.GPIO as io
import threading
import sys
import subprocess

pir_pin     = 24 
hook_pin    = 23
drawer3_pin = 25
drawer4_pin = 8
drawer1_pin = 7
drawer2_pin = 17
drawer5_pin = 4
drawer6_pin = 22
drawer7_pin = 10

ringing         = "/home/pi/Weybourne/pi/phone/telephone-ring-1.mp3"
offhook         = "/home/pi/Weybourne/pi/phone/phone-off-hook-1.mp3"
drawer1         = "/home/pi/Weybourne/pi/phone/drawer1.wav"
drawer2         = "/home/pi/Weybourne/pi/phone/drawer2.wav"
drawer3         = "/home/pi/Weybourne/pi/phone/drawer3.wav"
drawer4         = "/home/pi/Weybourne/pi/phone/drawer4.wav"
drawer5         = "/home/pi/Weybourne/pi/phone/drawer5.wav"
drawer6         = "/home/pi/Weybourne/pi/phone/drawer6.wav"
drawer7         = "/home/pi/Weybourne/pi/phone/drawer7.wav"
intro           = "/home/pi/Weybourne/pi/phone/intro.wav"

mpegplayer      = "/usr/bin/mpg123"
wavplayer       = "/usr/bin/aplay"

class mp3playerThread(threading.Thread):

    def __init__ (self, file):
        threading.Thread.__init__(self)
        self.mp3file = file
    
    def terminate(self):
        self.subproc.terminate()

    def run(self):
        #while True:
            self.subproc = subprocess.Popen([mpegplayer, self.mp3file])
            self.subproc.wait()

class wavplayerThread(threading.Thread):

    def __init__ (self, file):
        threading.Thread.__init__(self)
        self.wavfile = file
    
    def terminate(self):
        self.subproc.terminate()

    def run(self):
        #while True:
            self.subproc = subprocess.Popen([wavplayer, self.wavfile])
            self.subproc.wait()

io.setmode(io.BCM)
io.setup(pir_pin    , io.IN, pull_up_down=io.PUD_UP) 
io.setup(hook_pin   , io.IN, pull_up_down=io.PUD_UP) 
io.setup(drawer1_pin, io.IN, pull_up_down=io.PUD_UP) 
io.setup(drawer2_pin, io.IN, pull_up_down=io.PUD_UP) 
io.setup(drawer3_pin, io.IN, pull_up_down=io.PUD_UP) 
io.setup(drawer4_pin, io.IN, pull_up_down=io.PUD_UP) 
io.setup(drawer5_pin, io.IN, pull_up_down=io.PUD_UP) 
io.setup(drawer6_pin, io.IN, pull_up_down=io.PUD_UP) 
io.setup(drawer7_pin, io.IN, pull_up_down=io.PUD_UP) 

offhookThread   = mp3playerThread(offhook)
ringThread      = mp3playerThread(ringing)
drawer1Thread   = wavplayerThread(drawer1)
drawer2Thread   = wavplayerThread(drawer2)
drawer3Thread   = wavplayerThread(drawer3)
drawer4Thread   = wavplayerThread(drawer4)
drawer5Thread   = wavplayerThread(drawer5)
drawer6Thread   = wavplayerThread(drawer6)
drawer7Thread   = wavplayerThread(drawer7)

state = 0

while True:
    if io.input(drawer1_pin):
        if state == 2:
            state = 3
            if offhookThread.isAlive():
                offhookThread.terminate()
            sys.stdout.write('1')
            sys.stdout.flush()
            if not drawer1Thread.isAlive():
                drawer1Thread = wavplayerThread(drawer1)
                drawer1Thread.start()
            state = 2
    elif state == 2:
        if drawer1Thread.isAlive():
            drawer1Thread.terminate()

    if io.input(drawer2_pin):
        if state == 2:
            state = 3
            if offhookThread.isAlive():
                offhookThread.terminate()
            sys.stdout.write('2')
            sys.stdout.flush()
            if not drawer2Thread.isAlive():
                drawer2Thread = wavplayerThread(drawer2)
                drawer2Thread.start()
            state = 2
    elif state == 2:
        if drawer2Thread.isAlive():
            drawer2Thread.terminate()

    if io.input(drawer3_pin):
        if state == 2:
            state = 3
            if offhookThread.isAlive():
                offhookThread.terminate()
            sys.stdout.write('3')
            sys.stdout.flush()
            if not drawer3Thread.isAlive():
                drawer3Thread = wavplayerThread(drawer3)
                drawer3Thread.start()
            state = 2
    elif state == 2:
        if drawer3Thread.isAlive():
            drawer3Thread.terminate()

    if io.input(drawer4_pin):
        if state == 2:
            state = 3
            if offhookThread.isAlive():
                offhookThread.terminate()
            sys.stdout.write('4')
            sys.stdout.flush()
            if not drawer4Thread.isAlive():
                drawer4Thread = wavplayerThread(drawer4)
                drawer4Thread.start()
            state = 2
    elif state == 2:
        if drawer4Thread.isAlive():
            drawer4Thread.terminate()

    if io.input(drawer5_pin):
        if state == 2:
            state = 3
            if offhookThread.isAlive():
                offhookThread.terminate()
            sys.stdout.write('5')
            sys.stdout.flush()
            if not drawer5Thread.isAlive():
                drawer5Thread = wavplayerThread(drawer5)
                drawer5Thread.start()
            state = 2
    elif state == 2:
        if drawer5Thread.isAlive():
            drawer5Thread.terminate()

    if io.input(drawer6_pin):
        if state == 2:
            state = 3
            if offhookThread.isAlive():
                offhookThread.terminate()
            sys.stdout.write('6')
            sys.stdout.flush()
            if not drawer6Thread.isAlive():
                drawer6Thread = wavplayerThread(drawer6)
                drawer6Thread.start()
            state = 2
    elif state == 2:
        if drawer6Thread.isAlive():
            drawer6Thread.terminate()

    #if io.input(drawer7_pin):
    #    if state == 2:
    #        state = 3
    #        if offhookThread.isAlive():
    #            offhookThread.terminate()
    #        sys.stdout.write('7')
    #        sys.stdout.flush()
    #        if not drawer7Thread.isAlive():
    #            drawer7Thread = wavplayerThread(drawer7)
    #            drawer7Thread.start()
    #        state = 2
    #elif state == 2:
    #    if drawer7Thread.isAlive():
    #        drawer7Thread.terminate()

    if not io.input(pir_pin) and io.input(hook_pin):
        state = 1
        print("Ringing!")
        if offhookThread.isAlive():
            offhookThread.terminate()

        if not ringThread.isAlive():
            ringThread = mp3playerThread(ringing)
            ringThread.start()

    if not io.input(hook_pin):
        if state <= 1:
            state = 2
            print("Receiver up!")
            if ringThread.isAlive():
                ringThread.terminate()

            if not offhookThread.isAlive():
                offhookThread = wavplayerThread(intro)
                offhookThread.start()

    elif state == 2:
        state = 0
        print("Receiver down!")
        if offhookThread.isAlive():
            offhookThread.terminate()

        if ringThread.isAlive():
            ringThread.terminate()

        if drawer1Thread.isAlive():
            drawer1Thread.terminate()

        if drawer2Thread.isAlive():
            drawer2Thread.terminate()

        if drawer3Thread.isAlive():
            drawer3Thread.terminate()

        if drawer4Thread.isAlive():
            drawer4Thread.terminate()

        if drawer5Thread.isAlive():
            drawer5Thread.terminate()

        if drawer6Thread.isAlive():
            drawer6Thread.terminate()

        if drawer7Thread.isAlive():
            drawer7Thread.terminate()

    time.sleep(0.5)
    print('HERE')
