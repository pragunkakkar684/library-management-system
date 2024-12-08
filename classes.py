class book:
    def __init__(self,title,author,isbn,copies):
        self._title=title
        self._author=author
        self._isbn=isbn
        self._availableCopies=copies

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def availableCopies(self):
        return self._availableCopies

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
            print(f'{self._name} borrowed {book.title}')
        else:
            print(f'{book.title} is not available')

    def returnbook(self,book):
        if book in self._borrowedbooks:
            book.returnbook()
            self._borrowedbooks.remove(book)
            print(f'{self._name} returned {book.title}')
        else:
            print(f'{self._name} does not have {book.title}')

class library():
    def __init__(self):
        self._books=[]

    def add_book(self,book):
        for b in self._books:
            if b._isbn == book._isbn:
                b._availableCopies += book._availableCopies
                return
        self._books.append(book)

    def remove_book(self,book):
        self._books.remove(book)

    def display_books(self):
        print("Available books: ")
        for book in self._books:
            print(f'{book.title} by {book.author} - copies {book.availableCopies}')

class librarian():
    def __init__(self,name,employee_id):
        self._name=name
        self._eid=employee_id

    def add_book(self,library,book):
        library.add_book(book)

    def remove_book(self,library,book):
        library.remove_book(book)

    

