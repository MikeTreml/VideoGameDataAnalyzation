from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from . import api_request
bp = Blueprint('video_game', __name__)

@bp.route('/test')
def test():
    return "All good!"

@bp.route('/yearly')
def yearly():
    api_request.request_default()

    return render_template('video_game/yearly.html')

@bp.route('/')
def index():
    api_request.request_default()

    return render_template('video_game/index.html')


@bp.route('/postform', methods=('GET', 'POST'))
def other_example():
    result = api_request.request_default()
    if request.method == 'POST':
        requeststring = request.form['title']

        error = None
        if error is not None:
            flash(error)
        elif request.form['title'] == "go home":
            return redirect(url_for('video_game.index'))
        else:
            return render_template('video_game/postform.html', table_data=result)
    return render_template('video_game/postform.html', table_data=result)

