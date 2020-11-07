import socket
import pygame, math, time, sys, os
from ast import literal_eval
from hooman import Hooman

class GUI_Support:

    #Initializes the GUI display
    def initDisplay(self, dims):
        pygame.init()
        self.backgroundColor = (255,255,255)
        return pygame.display.set_mode(dims)

    #Called when the x is clicked on the GUI
    def isQuit(self):
        pass

    #Function to draw and update GUI graphics as it receives new coordinates
    def drawGraphics(self, position, screen, dims):
        handX, handY, handZ = position
        handXVisual = handX
        handZVisual = handZ


        #Centers the X and Z coordinates
        handY = handY * -1
        handX += 500
        handZ += 500
        handY += 500
        width, height = dims
        screen.fill(self.backgroundColor)  #pass in chooseBackgroundColor() function

        #BACKGROUND COLOR SLIDER
        window_width, window_height = (400*1.25), (400*1.25)
        hapi = Hooman(window_width, window_height)


        slider_options = {"value_range": [0, 255]}

        r_slider = hapi.slider(50, 300, 400, 10, slider_options)
        g_slider = hapi.slider(50, 330, 400, 10, slider_options)
        b_slider = hapi.slider(50, 360, 400, 10, slider_options)

        while hapi.is_running:
            bg_col = (r_slider.value(), g_slider.value(), b_slider.value())
            hapi.background(bg_col)

            r_slider.update()
            g_slider.update()
            b_slider.update()

            hapi.fill(hapi.color["black"])
            r_text = "r:{}".format(r_slider.value())
            hapi.text(r_text, 50, 280)
            g_text = "g:{}".format(g_slider.value())
            hapi.text(g_text, 50, 310)
            b_text = "b:{}".format(b_slider.value())
            hapi.text(b_text, 50, 340)

            hapi.flip_display()
            hapi.event_loop()
    
        #color palette lines
        pygame.draw.line(screen, (0,0,0), (0,100), (1600,100))
    
    #def chooseBackgroundColor(self):

    

     #Not sure what this does but crashes without it
    def getTextObjects(self, text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()


#Changes the screen content and updates the display
def guiDisplay(coords):
    guiSupport.drawGraphics(coords, screen, (800, 800))
    pygame.display.update()


#Initializes the socket connection with the hand sensor file and starts the main loop
def connectToSocket():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))
    main()


#Receives coordinates from web socket connection and passes them to the drone and GUI portions of the code
def main():
    
    try:
        while True:
            guiDisplay((0,450,0))
            
    #         #Receive 1024 bits of websocket information (Is enough for our purposes)
    #         full_msg = ''
    #         msg = s.recv(1024)

    #         #Full message recieves a decoded string of the server data
    #         full_msg = msg.decode("utf-8")
    #         print(full_msg)

    #         #This is meant to clear the buffer until only one array is left if the buffer is filled too fast
    #         while(len(full_msg) > 40):

    #             #Re-receives 1024 bits of websocket information in order to clear the buffer 1024 bits at a time
    #             full_msg = ''
    #             msg = s.recv(1024)
    #             full_msg = msg.decode("utf-8")
    #             print(full_msg)
            

    #         #Turns the string array into an actual array of integers
    #         coordinateArr = literal_eval(full_msg)

    #         #Passes the GUI an array of the hand coordinates
    #         guiDisplay(coordinateArr)

    #         #Function that takes coordinates and outputs drone commands to the connected drone
           



    except Exception as inst:
        print(type(inst)) 
        print(inst) 
        print("Connection closed")
       


#Initial function that runs 
if __name__ == "__main__":
    #Gets current working directory to pass to the GUI
    path = os.getcwd()


    #Initializes the pygame GUI window
    guiSupport = GUI_Support()

    #Initializes window to  (1.25 multiplier)
    xWidth = 1000   
    yHeight = 1000
    screen = guiSupport.initDisplay((xWidth, yHeight))

    #Initializing font for coordinate display
    pygame.font.init()
    myFont = pygame.font.SysFont('Arial', 22)
    

    #Drone icon
    #icon = pygame.image.load(path + '\Drone.png')
    #pygame.display.set_icon(icon)
    pygame.display.set_caption('VR Paint')

    #Connect to socket
    main()
    #connectToSocket()