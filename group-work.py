books = [] #list
clients = [] #queue
borrowed_books = [] #stack

#record books

def record_books(bookID,title,author,availability):
    book = {
        "bookID": bookID,
        "title": title,
        "author": author,
        "availability": availability 
    }
    books.append(book)


record_books(1,'The Great Gatsby','F. Scott Fitzgerald','Yes')
record_books(2,'To Kill a Mockingbird','Harper Lee','Yes')
record_books(3,'how to talk to any one','Harper Lee','Yes')
record_books(4,'rules of life','Harper Lee','Yes')
record_books(5,'rich dad poor dad','Harper Lee','Yes')
record_books(6,'millionaires fast lane','Harper Lee','Yes')
record_books(7,'the power of habit','Harper Lee','Yes')
record_books(8,'dark psycology and manipulation','Harper Lee','Yes')
record_books(9,'surrounded by idiots','Harper Lee','Yes')
record_books(10,'the laws of human nature','Harper Lee','Yes')
record_books(11,'thinking fast and slow','Harper Lee','Yes')
record_books(12,'law governing trust','Harper Lee','Yes')
record_books(13,'johnson 1988 cheese','Harper Lee','Yes')
record_books(14,'harry potter and the magical wand','Harper Lee','Yes')
record_books(15,'beauty and the beast','Harper Lee','Yes')
record_books(16,'sherlock holmes','Harper Lee','Yes')
record_books(17,'candlestick bible','Harper Lee','Yes')
record_books(18,'2019 zero float enry','Harper Lee','Yes')
record_books(19,'hanzo shaddow codes','Harper Lee','Yes')
record_books(20,'trading in the zone','Harper Lee','Yes')
print("all books:")
print(f'{"book ID":<12} {"Book Name":<35} {"book Author":<22} {"book Availability":<32}')
print('-'*100)
for book in books:
    bookID,title,author,availability = book
    print(f'{book[bookID]:<12} {book[title]:<35} {book[author]:<22} {book[availability]:<32}')
print("\n")
# add clients to request books queue

def waiting_list(username,title):
    user = {
        "username": username,
        "book": title
    }
    clients.append(user)

# call waiting list function

waiting_list('heshima','To Kill a Mockingbird')
waiting_list('heshima','trading in the zone')

# display waiting list queue

print("all clients waiting for books after running waiting_list() function (enqueue):")
print(f'{"username":<12} {"Book Name":<35}')
print('-'*40)
for client in clients:
    print(f'{client['username']:<12} {client['book']:<12}')
print("\n")
print("\n")

#define borrow book

def borrow_book():
    if clients:
        client = clients.pop(0)
        available_book = next((book for book in books if book['title'] == client['book']),[])
        if available_book:
            if available_book["availability"] == 'Yes':
                borrowed_books.append(client)
                for index,book in enumerate(books):
                    if book['title'] == client['book']:
                        books[index]["availability"] = 'no'
            else:
                print('book is is already borrowed')
        else:
            print('book not found')
# call borrow book function

borrow_book()

# display updated list of waiting list after borrowing a book (after dequeue operation)

print('list of clients requesting books after borrowing a book after calling borrow_book() function (dequeue from waiting list):')
print(f'{"username":<12} {"Book Name":<35}')
print('-'*40)
for client in clients:
    print(f'{client['username']:<12} {client['book']:<12}')
print("\n")
print("\n")

# display borrowed books + corresponding clients 

print('list of borrowed books after pushing into borrowed books stack:')
print(f'{"username":<12} {"Book Name":<35}')
print('-'*40)
for client in borrowed_books:
    print(f'{client['username']:<12} {client['book']:<12}')
print("\n")
print("\n")

# display updated list of books (the book which is already borrowed must change the avalability to false)


print('updated list of books after borrowing a book:')
print(f'{"book ID":<12} {"Book Name":<35} {"book Author":<22} {"book Availability":<32}')
print('-'*100)
for book in books:
    bookID,title,author,availability = book
    print(f'{book[bookID]:<12} {book[title]:<35} {book[author]:<22} {book[availability]:<32}')
print("\n")

# define the return borrowed books function 

def return_borrowed_books():
    if borrowed_books:
        client = borrowed_books.pop()
        for index,book in enumerate(books):
            if books[index]["title"] == client["book"]:
                books[index]["availability"] = 'Yes'

# call the return borrowed books func (pop operation from the stack and change the book status)

return_borrowed_books()

# didplay the updated list after returning the borrowed book( status changed back to available)

print('updated list of books after returning a book:')
print(f'{"book ID":<12} {"Book Name":<35} {"book Author":<22} {"book Availability":<32}')
print('-'*100)
for book in books:
    bookID,title,author,availability = book
    print(f'{book[bookID]:<12} {book[title]:<35} {book[author]:<22} {book[availability]:<32}')
print("\n")



