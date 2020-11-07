import socket
import pygame, math, time, sys, os
from ast import literal_eval


class GUI_Support:

    #Initializes the GUI display
    def initDisplay(self, dims):
        pygame.init()
        self.drawBool = False
        self.drawingColor = (0,0,0)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 50, 50)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 50)
        self.BLUE = (50, 50, 255)
        self.GREY = (200, 200, 200)
        self.ORANGE = (200, 100, 50)
        self.WHITE = (255,255,255)
        self.backgroundColor = (255,255,255)
        return pygame.display.set_mode(dims)

    #Called when the x is clicked on the GUI
    def isQuit(self):
        pass

    #Function to draw and update GUI graphics as it receives new coordinates
    def drawGraphics(self, position, screen, dims):
        indexX, indexY, indexZ = position[0]
        thumbX, thumbY, thumbZ = position[1]

        if(((indexX - thumbX) > 55) or ((thumbX - indexX) > 55) or ((indexZ - thumbZ) > 55) or ((thumbZ - indexZ) > 55)):
            self.drawBool = False
        else:
            self.drawBool = True
        indexX = indexX * 1.5
        indexZ = indexZ * 1.5

        #Centers the X and Z coordinates
        indexX += 600
        indexZ += 450
        indexY = indexY / 20
        indexX = int(indexX)
        indexY = int(indexY)
        indexZ = int(indexZ)
        width, height = dims
        screen.fill(self.backgroundColor)  #pass in chooseBackgroundColor() function
        circleRadius = indexY

        temp = indexX

        
        #color palette lines
        screen.blit(background, (0,0))
        
        

        #dot
        pygame.draw.circle(screen, self.drawingColor, (indexX, indexZ), circleRadius)
        if(self.drawBool):
            pygame.draw.circle(background,self.drawingColor,(indexX, indexZ), circleRadius)
        
        #color pallet
        #pygame.draw.rect(screen, self.RED, (0,0,1200,100)
        pygame.draw.line(screen, self.BLACK, (0,100), (1200,100))
        pygame.draw.circle(screen, self.BLACK, (50,50), 40)
        pygame.draw.circle(screen, self.RED, (150,50), 40)
        pygame.draw.circle(screen, self.BLUE, (250,50), 40)
        pygame.draw.circle(screen, self.GREEN, (350,50), 40)
        pygame.draw.circle(screen, self.GREY, (450,50), 40)
        pygame.draw.circle(screen, self.ORANGE, (550,50), 40)
        pygame.draw.circle(screen, self.YELLOW, (650,50), 40)

        pygame.draw.circle(screen, self.WHITE, (850,50), 40)
  

    

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


#Receives coordinates from web socket connection and passes them to the  and GUI portions of the code
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
            while(len(full_msg) > 40):

                #Re-receives 1024 bits of websocket information in order to clear the buffer 1024 bits at a time
                full_msg = ''
                msg = s.recv(1024)
                full_msg = msg.decode("utf-8")
                print(full_msg)
            

            #Turns the string array into an actual array of integers
            coordinateArr = literal_eval(full_msg)
            print(coordinateArr)
            #Passes the GUI an array of the hand coordinates
            guiDisplay(coordinateArr)
            
            #Testing
            # guiDisplay((0,450,0))

            #Function that takes coordinates and outputs  commands to the connected 
           



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

    #Initializes window to  (1.50 multiplier)
    xWidth = 1200   
    yHeight = 900
    screen = guiSupport.initDisplay((xWidth, yHeight))
    background=pygame.Surface(screen.get_size())
    background=background.convert()
    background.fill((255,255,255))

    #Initializing font for coordinate display
    pygame.font.init()
    myFont = pygame.font.SysFont('Arial', 22)
    

    # icon
    #icon = pygame.image.load(path + '\.png')
    #pygame.display.set_icon(icon)
    pygame.display.set_caption('VR Paint')

    #Connect to socket
    #main()
    connectToSocket()