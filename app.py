import billboard
chart = billboard.ChartData('hot-100')


from flask import Flask, render_template, Markup

app = Flask('testapp')

@app.route('/')
def index():
    chart_list = "<ol>"
    for song in chart :
        chart_list = chart_list + "<li>" + song.title + " - " + song.artist + "</li>"
    chart_list = Markup(chart_list + "</ol>")
    return render_template('index.html', variable=chart_list)

if __name__ == '__main__':
    app.run()