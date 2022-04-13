from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db
import functools

# Import and register the blueprint from the factory 
# using 'app.register_blueprint()'
bp = Blueprint('auth', __name__, url_prefix='/auth')


# '@bp.route' associates the URL /register 
# with the register view function
@bp.route('/register', methods=('GET', 'POST'))
def register():

    # If the user submitted the form, 'request.method' will be 'POST'. 
    # In this case, start validating the input.
    if request.method == 'POST':

        # 'request.form' is a special type of dict mapping 
        # submitted form keys and values.
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        error = None

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (email, password) VALUES (?, ?)",
                    (email, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {email} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None

        db = get_db()

        # 'fetchone()' returns one row from the query
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect email or password.'

        # 'check_password_hash()' hashes the submitted password in the 
        # same way as the stored hash and securely compares them
        elif not check_password_hash(user['password'], password):
            error = 'Password error.'

        if error is None:
            
            # 'session' is a dict that stores data across requests
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


# bp.before_app_request() registers a function that runs 
# before the view function, no matter what URL is requested.
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


# To logout, you remove the user id from the session
@bp.route('/logout')
def logout():
    session.clear()

    # The url_for() function generates the URL 
    # to a view based on a name and arguments.
    return redirect(url_for('index'))


# Creating, editing, and deleting blog posts 
# will require a user to be logged in
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
    