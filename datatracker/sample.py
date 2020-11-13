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
        requeststring = request.form['title']
        result = api_request.run_requests(requeststring)
        error = None
        if error is not None:
            flash(error)
        elif request.form['title'] == "go home":
            return redirect(url_for('sample.index'))
        else:
            return render_template('sample/postform.html', table_data=result)
    return render_template('sample/postform.html')

