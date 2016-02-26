from flask import render_template

from . import main
from .. import db

@main.route('/hello')
def hello():
    return 'hello world'