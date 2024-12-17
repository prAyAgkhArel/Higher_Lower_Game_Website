from flask import Flask
from random import randint
app = Flask(__name__)

random_int = randint(0,9)
@app.route('/')
def homepage():
    return ('<h1 >Guess a number between 0 and 9</h1>'
            '<img style="width:500" src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGxyMDRrdmVxMmE2ODZzNjExcGxsej'
            'RxMzdla2w3M2pvNGVjYzU1ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rs2QPsshsFI9zeT4Kn/giphy.gif">')

@app.route('/<int:number>')
def result(number):
    if random_int == number:
        return ('<h1 style="color:blue">You found me.</h1>'
                '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')

    elif random_int > number:
        return ('<h1 style="color:blue">Too low</h1>'
                '<img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')

    else:
        return ('<h1 style="color:blue">Too High</h1>'
                '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')

if __name__ == "__main__":
    app.run(debug=True)



