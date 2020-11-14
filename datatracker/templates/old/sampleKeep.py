
from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint


bp = Blueprint('video_game', __name__)


@bp.route('/test')
def test():
    return "All good!"


@bp.route('/')
def index():

    message = "This text is coming from the 'video_game.py' module, not the html file!"
    phrase = "Python is cool!"
    return render_template('video_game/index.html', message=message, word=phrase)


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
            return redirect(url_for('video_game.index'))
        else:
            return render_template('video_game/postform.html', page_title=page_title)

    else:
        return render_template('video_game/postform.html', page_title="PostForm from Module Function")

