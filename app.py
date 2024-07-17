from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route('/')
def hello():
    myURL = url_for('eightball')
    return render_template('8ball.html', url = myURL)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return f'Thanks for submitting the form {request.form["fname"]}!'
    return render_template('signup.html', signup=url_for('signup'))


@app.route('/eightball', methods=["GET", "POST"])
def eightball():
    if request.method == "POST":
        res = request.form['8ballquestion']
        answers = ["No ", "Hell No ", "I don't know ", "Of course ", "Time will tell...", "Listen...", "Yes!"]
        answer = random.choice(answers)
        print('8ballquestion: ' + res)
        return answer
        # return render_template("8ball.html", answer=answer, question=res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
