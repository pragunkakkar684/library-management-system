class book:
    def __init__(self,title,author,isbn,copies):
        self._title=title
        self._author=author
        self._isbn=isbn
        self._availableCopies=copies

    def boroowbook(self):
        if self._availableCopies>0:
            self._availableCopies-=1
            return True
        return False
    
    def returnbook(self):
        self._availableCopies+=1

        
