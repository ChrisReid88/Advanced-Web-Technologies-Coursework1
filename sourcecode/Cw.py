from flask import Flask,json, render_template, request

app = Flask(__name__)


# Get the data from the json file and save in a dictionary
def load_data():
    with app.open_resource('static/data2.json') as f:
        data = json.load(f)
    return data


# Home page with the parsed json data being passed to it as 'response'
@app.route('/')
def home():
    return render_template('home.html', response=load_data())


# Contact page
@app.route('/contact')
def about():
    return render_template('contact.html')


# Feedback page with post method to receive and store text entered by user
@app.route('/about', methods=['POST'])
def feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    fdbk = '{ "name":"' + name + '", "email":"' + email + '", "message":"' + message + '"}'
    with open("static/feedback.json", "a") as myfile:
        myfile.write(fdbk)
    return render_template('feedback.html')


#  Simple gratitude page for when user submits feedback
@app.route('/about/feedback')
def feedback_received():
    return render_template('feedback.html')

# Individual movie page where the route is set to actual movie title
@app.route('/<name>')
def movie(name=None):
        return render_template('movie.html', name=name, response=load_data())


# Genre page that creates a list of genres which are taken from the genre lists for each movie in the json.
# Ensures duplicates aren't
# added and then sorts them in ascending order.
@app.route('/genre')
def genre():
    load_data()
    categories=[]
    for movie in load_data().values():
        for category in movie['genre']:
            if category not in categories:
                categories.append(category)
                categories.sort()
    return render_template('genre.html', gen=categories, response=load_data())


# Displays the set of genres. Clicking a genre filters displayed movies by that specific genre
# Movies that are clicked navigate back to the '/<movie>' page.
@app.route('/genre/<genre>')
def specific_genre(genre=None):
    return render_template('filtered.html', genre=genre, response=load_data())


# Redirect user if url they entered is not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html')


@app.errorhandler(Exception)
def exception_error(error):
    return render_template('not_found.html')

if __name__ ==  "__main__":
    app.run(debug =True)
