#Local
import models

# Flask
import flask

app: flask.app.Flask = flask.Flask(__name__)
users: list['models.User'] = []

@app.route('/reg', methods=['GET', 'POST'])
def registration() -> flask.Response:
    if flask.request.method == 'POST':
        data: dict = flask.request.form
        users.append(
            models.User.create(**data, users=users)
        )

    return flask.render_template(
        'regis.html'
    )

@app.route('/')
def main_page():
    return "Hello"

if __name__ == '__main__':

    app.run(
        host='localhost',
        port=8080,
        debug=True
    )