class Book:
    def __init__(self,title) -> None:
        self.title = title


class Newspaper:
    def __init__(self,name):
        self.name = name


b1 = Book("The Catcher in the Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2= Newspaper("The New York Times")

#Using type function to inspect the Object type
print(type(n1))
print(type(b1))

#Compare Two Types Together
print(type(b1) == type(n1))

#Using isIstance to compare a specific instance to a known type
print(isinstance(b1,Book))
print(isinstance(n1,Newspaper))
