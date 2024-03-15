from flask import Flask, render_template, request
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index')
@app.route('/')
def index():
    nazvanie = 'Главная'
    return render_template('base.html', title=nazvanie)


@app.route('/training/<prof>')
def train(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def prof(list):
    lst = ['слесарь'] * 15
    return render_template('prof.html', list=lst, znak=list)


@app.route('/form1', methods=['POST', 'GET'])
def form1():
    if request.method == 'GET':
        return render_template('form1.html')
    else:
        profil = {}
        profil['email'] = request.form.get('email')
        profil['class'] = request.form.get('class')
        return render_template('answer.html', **profil)


@app.route('/answer')
def answ():
    pass


def add_user():
    sess = db_session.create_session()
    user = User()
    user.surname = 'Ridley'
    user.name = 'Scott'
    user.age = 21
    user.position = 'capitan'
    user.email = 'sr@mars.com'
    user.speciality = 'resercher'
    user.hashed_password = '123'
    user.address = 'module 1'
    sess.add(user)
    sess.commit()
    sess.close()


def add_jobs():
    sess = db_session.create_session()
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    sess.add(job)
    sess.commit()
    sess.close()


def zapros():
    sess = db_session.create_session()
    user = sess.query(User).filter(User.age == 21)
    for el in user:
        print(el.name)
    sess.close()



def main():
    db_session.global_init("db/mars.db")
    zapros()
    # add_user()
    # add_jobs()
    app.run('127.0.0.1', port=80)


if __name__ == '__main__':
    main()
