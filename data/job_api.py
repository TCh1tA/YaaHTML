import flask

from . import db_session
from . import jobs
from .jobs import Jobs

blueprint = flask.Blueprint(
    'get_job',
    __name__,
    template_folder='templates'
)


@blueprint.route('/test/jobs')
def get_job():
    d = {}
    sess = db_session.create_session()
    req = sess.query(Jobs).all()
    for el in req:
        d[el.id] = {
            'team_leader': el.team_leader,
            'job': el.job,
            'work_size': el.work_size,
            'collaborators': el.collaborators,
            'start_date': el.start_date,
            'end_date': el.end_date,
            'is_finished': el.is_finished
        }
    return flask.jsonify(d)
