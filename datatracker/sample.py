from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from . import api_request
bp = Blueprint('sample', __name__)


@bp.route('/test')
def test():
    return "All good!"

@bp.route('/yearly')
def yearly():
    api_request.run_request()

    return render_template('sample/yearly.html')

@bp.route('/')
def index():
    api_request.run_request()

    return render_template('sample/index.html')


@bp.route('/postform', methods=('GET', 'POST'))
def other_example():
    if request.method == 'POST':
        page_title = request.form['title']
        error = None

        if not page_title:
            error = 'You must enter a title'

        if error is not None:
            flash(error)
        elif request.form['title'] == "go home":
            return redirect(url_for('sample.index'))
        else:
            return render_template('sample/postform.html', page_title=page_title)

    else:
        return render_template('sample/postform.html', page_title="PostForm from Module Function")

