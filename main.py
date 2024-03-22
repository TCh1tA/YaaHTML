from flask import Flask, render_template, request, redirect
from data import db_session, jopan_api, job_api
from data.jobs import Jobs
from data.users import User
from data.login_form import LoginForm
from flask_login import LoginManager, login_user, logout_user
from flask_restful import Api
from data import user_resource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user.hashed_password and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect('/succes')
        else:
            return render_template('login.html', message='Неверно', form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/succes')
def suc():
    return 'Успешно'


def login_user(user, remember=False):
    pass


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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
        profil = {'email': request.form.get('email'), 'class': request.form.get('class')}
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
    user.set_password('123')
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
    # zapros()
    # add_user()
    # add_jobs()
    app.register_blueprint(job_api.blueprint)
    app.register_blueprint(jopan_api.blueprint)
    api.add_resource(user_resource.UserResource, '/api/v2/users/<int:user_id>')
    api.add_resource(user_resource.UserResourceList, '/api/v2/users/')
    app.run('127.0.0.1', port=80)


if __name__ == '__main__':
    main()
