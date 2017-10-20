from flask import Flask,json, render_template, request

app = Flask(__name__)


def load_data():
    with app.open_resource('static/data2.json') as f:
        data = json.load(f)
    return data


@app.route('/')
def home():
    return render_template('home.html', response=load_data())


@app.route('/about')
def about():
    return render_template('contact.html')


@app.route('/about', methods=['POST'])
def feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    fdbk = '{ "name":"' + name + '", "email":"' + email + '", "message":"' + message + '"}'
    with open("static/feedback.json", "a") as myfile:
        myfile.write(fdbk)
    return render_template('feedback.html')

@app.route('/about/feedback')
def feedback_received():
    return render_template('feedback.html')


@app.route('/<name>')
def movie(name=None):
        return render_template('movie.html', name=name, response=load_data())


@app.route('/genre')
def genre():
    load_data()
    genres=[]
    for movie in load_data().values():
        for genre in movie['genre']:
            if genre not in genres:
                genres.append(genre)
                genres.sort()
    return render_template('genre.html', gen=genres, response=load_data())


@app.route('/genre/<genre>')
def specific_genre(genre=None):
    return render_template('filtered.html', genre=genre, response=load_data())


if __name__ ==  "__main__":
    app.run(debug =True)
