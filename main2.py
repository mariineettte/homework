from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    astronaut_id = request.form.get('astronaut_id')
    astronaut_password = request.form.get('astronaut_password')
    captain_id = request.form.get('captain_id')
    captain_token = request.form.get('captain_token')

    if astronaut_id and astronaut_password and captain_id and captain_token:
        return "<h2>Доступ разрешен</h2>"
    else:
        return "<h2>Доступ запрещен</h2>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)