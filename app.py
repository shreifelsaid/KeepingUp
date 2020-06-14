import billboard
import requests
from flask import Flask, render_template, Markup
import json



app = Flask('testapp')

@app.route('/')
def index():
    fic = book_api("https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=J9mhscz58wH1ZY76Z5SYHH4kr04gfRA6")
    nonfic = book_api("https://api.nytimes.com/svc/books/v3/lists/current/hardcover-nonfiction.json?api-key=J9mhscz58wH1ZY76Z5SYHH4kr04gfRA6")
    return render_template('index.html', charts=music_api(), nonfic=nonfic, fic=fic, movies = movies_api())

def music_api():
    chart = billboard.ChartData('hot-100')
    chart_list = "<ol>"
    for song in chart :
        chart_list = chart_list + "<li>" + song.title + " - " + song.artist + "</li><br><br>"
    chart_list = Markup(chart_list + "</ol>")
    return chart_list


def book_api(api):
    books = requests.get(api)
    nyt_dict = json.loads(books.content)
    books_list = nyt_dict["results"]["books"]
    books_html = "<ol>"
    for book in books_list:
        books_html = books_html + "<li>" + book["title"] + " - " + book["author"] + "</li><br><br>"
    books_html = Markup(books_html + "</ol>")
    return books_html

def movies_api():

    movies = requests.get("https://api.themoviedb.org/3/trending/movie/day?api_key=b8cc60315a4981d64fadb916a05eea0a")
    movies_dict = json.loads(movies.content)
    movies_list = movies_dict["results"]
    movies_html = "<ol>"
    for movie in movies_list:
        movies_html = movies_html +  "<li>" + "<p style=\"text-align:left;\">" + movie["title"] +"<span style=\"float:right;\">" + " - Rating : " + str(movie["vote_average"]) + "</span>" + "</p></li><br>"
    movies_html = Markup(movies_html + "</ol>")
    return movies_html



if __name__ == '__main__':
    app.run(debug =True)