from flask import Flask,json,request, render_template

app = Flask(__name__)


@app.route('/')
def getData():
    with app.open_resource('static/data.json') as f:
        if __name__ == '__main__':
            data = json.load(f)
        return render_template('body.html', response=data)


if __name__ ==  "__main__":
    app.run(debug =True)
