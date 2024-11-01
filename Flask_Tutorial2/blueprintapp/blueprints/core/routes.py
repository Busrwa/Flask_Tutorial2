from flask import render_template, request, make_response, redirect, url_for, Response, jsonify, send_from_directory, session, flash, Blueprint
from blueprintapp.blueprints.todos.models import Todo
from blueprintapp.blueprints.people.models import Person

#from blueprintapp.app import db

core = Blueprint('core', __name__, template_folder='templates' )

@core.route('/')
def index():
    return render_template('core/index.html')

