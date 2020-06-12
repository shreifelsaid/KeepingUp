import billboard
import requests
chart = billboard.ChartData('hot-100')


from flask import Flask, render_template, Markup
import json

app = Flask('testapp')

@app.route('/')
def index():
    chart_list = "<ol>"
    for song in chart :
        chart_list = chart_list + "<li>" + song.title + " - " + song.artist + "</li>"
    chart_list = Markup(chart_list + "</ol>")

    fic = book_api("https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=J9mhscz58wH1ZY76Z5SYHH4kr04gfRA6")
    nonfic = book_api("https://api.nytimes.com/svc/books/v3/lists/current/hardcover-nonfiction.json?api-key=J9mhscz58wH1ZY76Z5SYHH4kr04gfRA6")
    return render_template('index.html', charts=chart_list, nonfic=nonfic, fic=fic)

def book_api(api):
    books = requests.get(api)
    nyt_dict = json.loads(books.content)
    books_list = nyt_dict["results"]["books"]
    books_html = "<ol>"
    for book in books_list:
        books_html = books_html + "<li>" + book["title"] + " - " + book["author"] + "</li>"
    books_html = Markup(books_html + "</ol>")
    return books_html


if __name__ == '__main__':
    app.run()