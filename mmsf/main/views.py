from flask import render_template, flash

from . import main
from .forms import KidsUploadForm
from .. import db
from ..models import Kids

@main.route('/hello')
def hello():
    return 'hello world'


@main.route('/kids/directory')
def kids_directory():
    kids = ['|'.join([kid.last_name, kid.first_name])for kid in Kids.query.all()]
    return '<br>'.join(kids)


@main.route('/kids/upload', methods=['GET', 'POST'])
def upload_kids():
    form = KidsUploadForm()
    if form.validate_on_submit():
        csvstring = form.csvstring.data.strip()
        Kids.insert_from_string(csvstring)
        flash('Uploaded (%s) kids to database' % len(csvstring.split('\n')))
    return render_template('upload_kids.html', form=form)