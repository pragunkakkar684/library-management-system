class book:
    def __init__(self,title,author,isbn,copies):
        self._title=title
        self._author=author
        self._isbn=isbn
        self._availableCopies=copies

    def borrowbook(self):
        if self._availableCopies>0:
            self._availableCopies-=1
            return True
        return False
    
    def returnbook(self):
        self._availableCopies+=1

class member:
    def __init__(self,name,member_id):
        self._name=name
        self._memberid=member_id
        self._borrowedbooks=[]

    def borrowbook(self,book):
        if book.borrowbook():
            self._borrowedbooks.append(book)
            print(f'{self._name} borrowed {book._title}')
        else:
            print(f'{book._title} is not available')

    def returnbook(self,book):
        if book in self._borrowedbooks:
            book.returnbook()
            self._borrowedbooks.remove(book)
            print(f'{self._name} returned {book._title}')
        else:
            print(f'{self._name} does not have {book._title}')
            


