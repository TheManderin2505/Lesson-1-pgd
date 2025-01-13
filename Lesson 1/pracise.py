
class Plane():
    def __init__(self,height,width,lenght,color,speed,):
        self.height = height
        self.width = width
        self.lenght = lenght
        self.color = color
        self.speed = speed
    
    def showdetails(self):
        print("height : ",self.height)
        print("width : ",self.width)
        print("lenght : ",self.lenght)
        print("color : ",self.color)
        print("speed : ",self.speed)
        
p1 = Plane(5,32,28,"grey","700 mph")
p1.showdetails()
    

        