from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from . import api_request
bp = Blueprint('video_game', __name__)

@bp.route('/test')
def test():
    return "All good!"


@bp.route('/yearly', methods=('GET', 'POST'))
def yearly():
    if request.method == 'POST':
        year = request.form['year']
        result = api_request.request_games_year(year)
        chart = api_request.process_filter(result)
        return render_template('video_game/yearly.html', table_data=result, chart_data=chart)

    else:
        result = api_request.request_games_year(1996)
        chart = api_request.process_filter(result)
        return render_template('video_game/yearly.html', table_data=result, chart_data=chart)


@bp.route('/')
def index():
    return render_template('video_game/index.html')


@bp.route('/topconsole')
def top_console():
    result = api_request.top_console()
    return render_template('video_game/topconsole.html', table_data=result)


@bp.route('/chartmain')
def chart_main():
    result = api_request.request_default()
    return render_template('video_game/chart_main.html', table_data=result)


@bp.route('/chartdetails')
def chart_details():
    result = api_request.request_console_game("LEGO Marvel Super Heroes")
    return render_template('video_game/chart_detailsview.html', table_data=result)


@bp.route('/search')
def search():
    search_string = request.args.get('search', default = "", type = str)
    if search_string == "":
        return render_template('video_game/search.html')
    result = api_request.request_search_string(search_string)
    return render_template('video_game/search.html', table_data=result)
