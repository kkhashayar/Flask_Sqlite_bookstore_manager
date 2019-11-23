#from app import *
from forms import *

# It might run to some problems, ill change it to import models instead.
# from models import *
import models
# for admin page
from admin import *
from models import Book


############################################################
########################## ROUTES ##########################
############################################################

#########################  HOME
@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
    form = SelectForm()
    all_books = models.show_all()
    return render_template("home.html", all_books=all_books, form=form)

######################### SELECT FIELDS
@app.route("/<id>", methods=["GET","POST"])
def id(id):
    book = Book.query.filter_by(id=id).first()
    #id = book.id
    form=SelectForm(title=book.title, author=book.author, quantity=book.quantity, price=book.price)

    if form.validate_on_submit():
        if form.delete.data:

            models.remove(id=id)
            return home()
        elif form.update.data:
            title = form.title.data
            author = form.author.data
            quantity = form.quantity.data
            price = form.price.data
            models.update(id,title,author,quantity,price)
            return home()

    return render_template("id.html",form=form)


#########################  INSERT
#-- inserting new records to database
@app.route("/insert", methods=["GET","POST"])
def insert():
    #-- form object from form class
    form = InsertForm()
    # instead of request.method = post using validate on submit
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        quantity = form.quantity.data
        price = form.price.data
        models.insert(title,author,quantity,price)
        return home()
    return render_template("insert.html", form=form)

#########################  REMOVE
#-- should move the link to info page with connector to given list object
@app.route("/remove", methods=["GET","POST"])
def remove():
    return render_template("remove.html")

#########################  UPDATE
#-- should move the link to info page with connector to given list object
@app.route("/update", methods=["GET","POST"])
def update():
    return render_template("update.html")

#------------ I'll use difflib and SequenceMatcher to improve the search
#########################  SEARCH BY TITLE
# basic search for title
@app.route("/search_by_title", methods=["GET","POST"])
def search_by_title():
    form = SearchTitleForm()
    if form.validate_on_submit():
        title = form.title.data
        result = models.search_by_title(title)
        return render_template("result.html", result=result)
    return render_template("search_by_title.html", form=form)

#########################  SEARCH BY AUTHOR
@app.route("/search_by_author", methods=["GET","POST"])
def search_by_author():
    form = SearchAuthorForm()
    if form.validate_on_submit():
        author = form.author.data
        result = models.search_by_author(author)
        return render_template("result.html", result=result)
    return render_template("search_by_author.html", form=form)

#########################  SEARCH BY QUANTITY
@app.route("/search_by_quantity", methods=["GET","POST"])
def search_by_quantity():
    form = SearchQuantityForm()
    if form.validate_on_submit():
        quantity = form.quantity.data
        result = models.search_by_quantity(quantity)
        return render_template("result.html", result=result)
    return render_template("search_by_quantity.html", form=form)

#########################  SEARCH BY PRICE
@app.route("/search_by_price", methods=["GET","POST"])
def search_by_price():
    form = SearchPriceForm()
    if form.validate_on_submit():
        price = form.price.data
        result = models.search_by_price(price)
        return render_template("result.html", result=result)
    return render_template("search_by_price.html", form=form)


#-- Calling the main function
if __name__ == '__main__':
    app.run(debug=True)
