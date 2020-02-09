"""
Things a sprite should hold:
fixed info:
-The sprite name
-The sprite text file name
-Priority

Variable info:
-The Coordinate its located on
-various event flags with bools for the game to use
--is collieded?
-sprite dimention
-hurtbox dimention
-sprite sheet index numbers


"""

class sprite:
    
    def __init__(self, n, sSheet):
        self.name = n
        self.spriteSheet= sSheet
        self.coordnate = [31,31]
        self.spriteDimention = [15,15]
        self.hitbox = [5,10]
        self.priority = 1
        self.indexNum = 1
        self.index = 1
        self.velocity = [0,0]


    def printInfo(self):
        print(self.name, self.spriteSheet, self.coordnate, self.spriteDimention, self.hurtbox, self.priority)
        
