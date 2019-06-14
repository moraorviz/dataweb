'''Blueprint to consume from sparql using some hard-coded
queries. Then some json objects are built and returned
in the response for the template to present the results to
the end user.'''

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .modules import consume


bp = Blueprint('view', __name__)


@bp.route('/')
def view():
    bodies = consume.getobjects()

    return render_template('show.html', bodies=bodies)
