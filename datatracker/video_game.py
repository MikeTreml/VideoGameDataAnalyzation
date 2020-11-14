from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from . import api_request
bp = Blueprint('video_game', __name__)

@bp.route('/test')
def test():
    return "All good!"

@bp.route('/yearly')
def yearly():


    return render_template('video_game/yearly.html')

@bp.route('/')
def index():


    return render_template('video_game/index.html')


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
    result = api_request.request_search_string("Super")
    return render_template('video_game/search.html', table_data=result)

