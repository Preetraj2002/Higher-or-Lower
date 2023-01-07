from flask import Flask
from random import randint

app = Flask(__name__)
temp=randint(0,9)
print(temp)

@app.route("/")
def hello():
    return "<h1><b>Guess a number between 0 and 9</b></h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>" \
           "<p>Good Lord</p>"

@app.route('/<int:number>')
def randi(number):

    if number<temp:
        return "<h1 style='color:red;'><b>Too low,try again!</b></h1>" \
               "<img style='width:400;' src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    if number>temp:
        return '<h1 style="color:purple;"><b>Too high,try again!</b></h1>' \
               '<img style="width:400;" src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    if number==temp:
        return "<h1 style='color:green;'><b>You found me!</b></h1>" \
               "<img style='width:400;' src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__=="__main__":
    app.run(debug=True)
