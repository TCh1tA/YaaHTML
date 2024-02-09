from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    nazvanie = 'Главная'
    return render_template('base.html', title=nazvanie)


@app.route('/training/<prof>')
def train(prof):
    return render_template('training.html', prof=prof)


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.<br>
            Человечеству мала одна планета.<br>
            Мы сделаем обитаемыми безжизненные пока планеты.<br>
            И начнем с Марса!<br>
            Присоединяйся!'''


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1><br>
                    <img src={url_for('static', filename='img/mars.jpg')}
                    alt='здесь должна была быть картинка, но не нашлась'><br>
                    Вот она какая, красная планета
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Bootstrap demo</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                    <link href="static/css/stile.css" rel= "stylesheet">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename='img/mars.jpg')}
                    alt='здесь должна была быть картинка, но не нашлась'><br>
                    <div class="alert alert-primary">Человечество вырастает из детства.</div>
                    <div class="alert alert-secondary">Человечеству мала одна планета.</div>
                    <div class="alert alert-success">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-danger">И начнем с Марса!</div>
                    <div class="alert alert-warning">Присоединяйся!</div>


                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
                  </body>
                </html>"""


@app.route('/list_prof/<list>')
def prof(list):
    lst = ['слесарь'] * 15
    return render_template('prof.html', list=lst, znak=list)


@app.route('/form1', methods=['POST', 'GET'])
def form1():
    if request.method == 'GET':
        return render_template("form1.html")
    else:
        return render_template("base.html")


if __name__ == '__main__':
    app.run('127.0.0.1', port=80)
