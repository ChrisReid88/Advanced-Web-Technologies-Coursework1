from flask import Flask,json,request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    with app.open_resource('static/data.json') as f:
        if __name__ == '__main__':
            data = json.load(f)
        return render_template('home.html', response=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<name>')
def movie(name=None):
    with app.open_resource('static/data2.json') as f:
        if __name__ == '__main__':
            data = json.load(f)

        return render_template('movie.html', name=name, response=data)

@app.route('/genre')
def genre():
    with app.open_resource('static/data2.json') as f:
        if __name__ == '__main__':
            data = json.load(f)
        genres=[]
        for movie in data.values():
            for genre in movie['genre']:
                if genre not in genres:
                    genres.append(genre)
                    genres.sort()
        return render_template('genre.html',gen=genres, response=data)

# @app.route('/genre/<genre>')
# def specificGenre():
#

if __name__ ==  "__main__":
    app.run(debug =True)
