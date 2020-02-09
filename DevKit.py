from Sixty_Four.assets import Sprites
import os.path
from PIL import Image, ImageDraw


class devKit:
    spriteList = []
    imageList= []
    toMatrix = []
    RGBMatrix = []
    collideList = []
    canvasSize = (64,64)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    inputPNG = Image.open(os.path.join(script_dir,"input.png"))
    temp = inputPNG


    def __init__(self):
        for x in range(64):
            self.toMatrix.append([])
            self.RGBMatrix.append([])
            for y in range(64):
                self.toMatrix[x].append([])
                self.RGBMatrix[x].append((0,0,0))
                self.toMatrix[x][y] = []


    def refreshBoard(self):
        for x in range(64):
            self.toMatrix.append([])
            self.RGBMatrix.append([])
            for y in range(64):
                self.toMatrix[x].append([])
                self.RGBMatrix[x].append((0,0,0))
                self.toMatrix[x][y].append([])  
                

    def makeSprite(self, sprName, sprSheet, coord):
        new = Sprites.sprite(sprName,sprSheet)
        new.coordnate = coord
        self.spriteList.append(new)

    def primeImage(self, spr):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        img = Image.open(os.path.join(script_dir,spr.spriteSheet))
        self.imageList.append([spr.coordnate, img, spr.hitbox, spr.name])


    def drawHitbox(self):
        hitTemp = self.temp
        draw = ImageDraw.Draw(hitTemp)
        for img in self.imageList:
            off = img[2]
            box = (img[0][0], img[0][1], img[0][0]+off[0], img[0][1]+off[1])
            draw.rectangle(box,outline = (0,0,0))
            hitTemp.putpixel((img[0][0], img[0][1]), (255,0,0))
            for y in range(16):
                for x in range(16):
                    if(hitTemp.getpixel((img[0][0] + x,img[0][1]+y)) == (0, 0, 0)):
                        for digs in self.toMatrix[img[0][1]+y][img[0][0]+x]:
                            if(digs[1] == img[3]):
                                break
                        else:
                            self.toMatrix[img[0][1]+y][img[0][0]+x].append(["x",img[3]])

        hitTemp = hitTemp.save(os.path.join(self.script_dir,"hit.png"))
        

                    

    def drawRGB(self):
        for img in self.imageList:
            for y in range(15):
                for x in range(15):
                    self.RGBMatrix[img[0][1]+y][img[0][0]+x] = img[1].getpixel((x,y))


    def createPNG(self):
        final = self.inputPNG.convert('RGB')

        for y in range(64):
            for x in range(64):
                final.putpixel((x,y), self.RGBMatrix[y][x])

        final = final.save(os.path.join(self.script_dir,"output.png"))
        #final = self.inputPNG
        self.inputPNG = self.temp



    def updateBoard(self):
        for x in self.spriteList:
            x.coordnate[0] += x.velocity[0]
            x.coordnate[1] += x.velocity[1]

        for x in self.spriteList:
            self.primeImage(x)
            self.drawHitbox()
            self.drawRGB()
        self.createPNG()
        

        
        
    def evaluateHits(self):
        temp = []
        for a in range(64):
            for b in range(64):
                depth = len(self.toMatrix[a][b])
                #print(depth)
                for x in range(depth):
                    #print(self.toMatrix[a][b][x][1] == "temp")

                    if(depth != 1):
                        if(self.toMatrix[a][b][x][1] != "temp"):
                            #print(self.toMatrix[a][b], [a,b])
                            for y in temp:
                                if y == self.toMatrix[a][b][x][1]:
                                    break
                            else:
                                temp.append(self.toMatrix[a][b][x][1])

                for d in self.collideList:
                    if(d == temp):
                       break
                else:
                     self.collideList.append(temp)  
        
                    
            
            


    def printMatrix(self):
        for a in range(64):
            for b in range(64):
                print(self.toMatrix[a][b][0][0],sep ="", end =" ")
            print("\n")

    def testCode(self):
        self.makeSprite("stickBoi", "sprite.png",[30,50])
        self.makeSprite("uwu", "sprite2.png", [37,31])
        for x in range(1):
            self.updateBoard()
            self.evaluateHits()
            #self.printMatrix()
            print(self.collideList)           
            self.collideList.clear()
            self.RGBMatrix.clear()
            self.toMatrix.clear()
            self.imageList.clear()
            self.refreshBoard()
            #self.evaluateHits()

    def testImage(self):
        print(self.img.format, self.img.size, self.img.mode)
        print(self.img.getpixel((6,3)))
