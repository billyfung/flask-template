from flask import Blueprint, render_template, current_app, request, flash, \
    url_for, redirect, session, abort


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    nodes = ['BEN2201', 'HAY2201', 'INV2201', 'ISL2201', 'OTA2201']
    return render_template('frontend/test.html', nodes=nodes)
