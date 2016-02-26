from flask import render_template

from . import main
from .. import db
from ..models import Kids

@main.route('/hello')
def hello():
    return 'hello world'


@main.route('/kids/directory')
def kids_directory():
    kids = ['|'.join([kid.last_name, kid.first_name])for kid in Kids.query.all()]
    return str(len(kids))
    