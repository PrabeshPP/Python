#ToDo create a Basic Class
class Book:
    def __init__(self,title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    #Instance method
    def getPrice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price*self._discount)/100
        else:
            return self.price
    
    def setDiscount(self,amount):
        self._discount = amount

        
#ToDo: Create an instance of the class

book1 = Book("Brave New World","Prabesh Bista",1000,12.99)
book2 = Book("War and Peace","Prabesh",1200,100.12)


#Printing the Object in the Python
print(book2.getPrice())
book2.setDiscount(10)
print(book2.getPrice())