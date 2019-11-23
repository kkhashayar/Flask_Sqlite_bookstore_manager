from app import *
########################## MODELS (DATABASE FORMATION)
# database object inherit app object as superclass
db = SQLAlchemy(app)
# For migration
# Migrate with app,db as super classes
Migrate(app,db)

"""
for automation i might create a separate file.
for now i do it manually

    1)set FLASK_APP=app.py #-- script that holds the app and db (with any file structure)
    2)flask db init creates migration file structure
    3)ipytohn db.create_all() to create tables
    #-- First time and after any changes in db structure:
    1)flask db migrate -m "message" to migrate
    2)flask db upgrade
"""
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    author = db.Column(db.String())
    quantity = db.Column(db.Integer())
    price = db.Column(db.Integer)

    #-- for debuging later on ill cheng it to __str__
    def __repr__(self):
        return f"{self.title} | {self.author} | {self.price} | {self.quantity}"

#-- Instead of creating methods i use separate functions
def get_id(title):
    book = Book.query.filter_by(title=title).first()
    return book.id

def insert(title, author, quantity, price):
    new_book = Book(title=title, author=author, quantity=quantity, price=price)
    db.session.add(new_book)
    db.session.commit()

def remove(id):
    book = Book.query.filter_by(id=id).first()
    if book is None:
        print("Record not found")
    else:
        db.session.delete(book)
        db.session.commit()

def update(id,title,author,quantity,price):
    book = Book.query.filter_by(id=id).first()
    book.title = title
    book.author = author
    book.quantity = quantity
    book.price = price
    db.session.commit()


def show_all():
    all_books = Book.query.all()
    return all_books

def search_by_title(title):
    book = Book.query.filter_by(title=title).all()
    return book

def search_by_author(author):
    books = Book.query.filter_by(author=author).all()
    return books

def search_by_quantity(quantity):
    books = Book.query.filter_by(quantity=quantity).all()
    return books

def search_by_price(price):
    books = Book.query.filter_by(price=price).all()
    return books

def book(id):
    book = Book.query.filter_by(id=id).first()
    return book
