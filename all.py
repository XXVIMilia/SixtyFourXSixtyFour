import pygame #contoller NEED TGUS
from samplebase import SampleBase
from rgbmatrix import graphics
import math
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
from subprocess import Popen, PIPE
import os

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.brightness=75
options.gpio_slowdown=0
options.pwm_bits=4
options.pwm_lsb_nanoseconds=180
options.multiplexing=0
#options.disable_hardware_pulsing
options.hardware_mapping = 'adafruit-hat-pwm'  # If you have an Adafruit HAT: 'adafruit-hat'
matrix = RGBMatrix(options = options)

def update(image_file):
    image = Image.open(image_file)  # Make image fit our screen.
    image.thumbnail((64, 64))#, Image.ANTIALIAS )
    matrix.SetImage(image.convert('RGB'))
    

    
class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="something went wrong")
        
    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../pi/rpi-rgb-led-matrix/fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 255)
        pos = offscreen_canvas.width
        my_text = "Press circle to start PONG"
        change =0
        while change==0:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 15, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.001)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            events = pygame.event.get()
            for event in events:
                    if event.type == pygame.JOYBUTTONDOWN:
                        change=1
                        self.matrix.Clear()
##def uploadText():
##    run_text = RunText()
##    run_text.process()
    
test=0
while (test == 0):
    try:    
        contollerVar = "checking connection of controller..."
        print(contollerVar)
        time.sleep(1)
        print("waiting...")
        pygame.joystick.init()
        pygame.display.init()
        j = pygame.joystick.Joystick(0)
        j.init()
        test = 1
    except pygame.error:
        test = 0
        
run_text = RunText()
run_text.process()
screen='home'
try:
    run_text.run()
    print("Press circle to start the game!")    
    while True:
        events = pygame.event.get()
        while (screen=='home'):
            events=pygame.event.get()
            for event in events:
                    if event.type == pygame.JOYBUTTONDOWN:
                        if(j.get_button(1)):#circle
                            screen='game'
                            print("Starting game")
                            print("Press triangle to pause")
        while screen=='game':
            events = pygame.event.get()
            for event in events:#NEED
                if j.get_axis(4)<-0.75:
                    player2velocity2=1
                elif j.get_axis(4)>0.75:
                    player2velocity2=-1
                else:# j.get_axis(4)<0.75 and j.get_axis(4)>-.75:
                    player2velocity2=0
                if j.get_axis(1)<-0.75:
                    player1velocity1=1
                elif j.get_axis(1)>0.75:
                    player1velocity1=-1
                else:# j.get_axis(1)<0.75 and j.get_axis(1)>-.75:
                    player1velocity1=0
                print(player1velocity1)
    
                if event.type == pygame.JOYBUTTONDOWN:#NEED
                    if (j.get_button(2) == 1):#triangle
                        print("Triangle to return to idle")
                        screen = 'home';
            update("yo.png")
            

                

                


except KeyboardInterrupt:
    print("exiting")
    matrix.Clear()
    j.quit()
