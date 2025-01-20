

class Dog():
    def __init__(self,name,color,age,size):
        self.dog_name = name
        self.dog_color = color
        self.dog_age = age
        self.dog_size = size

    def printdetails(self):
        print(self.dog_name)
        print(self.dog_color)
        print(self.dog_age)
        print(self.dog_size)

dog1 = Dog("sparx","white",10,"medium")
dog1.printdetails()
dog2 = Dog("keven","brown",5,"small")
dog2.printdetails()
dog3 = Dog("james","black and white",3,"large")
dog3.printdetails()