import socket
import pygame, math, time. sys, os
from ast import literal_eval

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
        handX += 400
        handZ += 400
        handY += 850
        width, height = dims
        screen.fill(self.backgroundColor)  #pass in chooseBackgroundColor() function

    
    def chooseBackgroundColor(self):

    

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
            
            #Receive 1024 bits of websocket information (Is enough for our purposes)
            full_msg = ''
            msg = s.recv(1024)

            #Full message recieves a decoded string of the server data
            full_msg = msg.decode("utf-8")
            print(full_msg)

            #This is meant to clear the buffer until only one array is left if the buffer is filled too fast
            while(len(full_msg) > 20):

                #Re-receives 1024 bits of websocket information in order to clear the buffer 1024 bits at a time
                full_msg = ''
                msg = s.recv(1024)
                full_msg = msg.decode("utf-8")
                print(full_msg)
            

            #Turns the string array into an actual array of integers
            coordinateArr = literal_eval(full_msg)

            #Passes the GUI an array of the hand coordinates
            guiDisplay(coordinateArr)

            #Function that takes coordinates and outputs drone commands to the connected drone
            droneController(coordinateArr)



    except Exception as inst:
        print(type(inst)) 
        print(inst) 
        print("Connection closed")
        droneLand()


#Initial function that runs 
if __name__ == "__main__":
    #Gets current working directory to pass to the GUI
    path = os.getcwd()

    #Connects to the drone object
    connectToDrone()

    #Initializes the pygame GUI window
    guiSupport = GUI_Support()

    #Initializes window to 1300x800 but 800x800 is used for the X and Z portion of the display
    xWidth = 1300
    yHeight = 800
    screen = guiSupport.initDisplay((xWidth, yHeight))

    #Initializing font for coordinate display
    pygame.font.init()
    myFont = pygame.font.SysFont('Arial', 22)
    

    #Drone icon
    icon = pygame.image.load(path + '\Drone.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('VR Paint')

    #Connect to socket
    connectToSocket()