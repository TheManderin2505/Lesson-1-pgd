#OOPS - object oreiented proggraming structure
#class - bleprint of a object, which has the properties and functions of an object

class Student:
    def __init__(self,name, age, grade, favcolor, hobby):
        self.name=name
        self.age=age
        self.grade=grade
        self.favcolor=favcolor
        self.hobby=hobby
        self.intro=" "

    def showdetails(self):
        print("The Deatails of the student are : ")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Grade : ",self.grade)
        print("Favourite Color : ",self.favcolor)
        print("Hobby : ", self.hobby)
        print()

    def getinto(self):
        self.intro=input("please introduce your self : ")
        print(self.intro)
        print()
        
#object

s1 = Student("Remi",14,"2nd year","blue","Model Planes")
#Object.function()
s1.showdetails()
s1.getinto()

s2 = Student("Mihir",11,"5th","gold","playing games")
s2.showdetails()
s2.getinto()

s3 = Student("James",13,"7th","Green","Football")
s3.showdetails()
s3.getinto()


