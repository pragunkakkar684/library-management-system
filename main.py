from classes import *

library1 = library()

book1=book("1984","Ramesh Babu","12345",3)
book2=book("Harry potter","Suresh Babu","12346",5)

librarian1= librarian("Ramu","L001")
librarian1.add_book(library1,book1)
librarian1.add_book(library1,book2)

library1.display_books()

member1= member("Pragun","M001")
print(member1)

member1.borrowbook(book1)
library1.display_books()
member1.returnbook(book1)
librarian1.remove_book(library1,book1)
library1.display_books()