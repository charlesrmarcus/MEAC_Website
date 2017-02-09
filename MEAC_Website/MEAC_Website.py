# -*- coding: utf-8 -*-
"""
    Erik Hansen
    MEAC_Website
"""

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from collections import defaultdict
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='pages')

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'MEAC_Website.db'),
    DEBUG=False,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_


@app.route('/admin', methods=['GET', 'POST'])
def adminPage():
    # if not session.get('logged_in'):
    #     abort(401)
    if request.method == 'POST':
        compoundKeys = []
        for field in request.form:
            compoundKeys.append((request.form[field], field.split(':')[0], field.split(':')[1]))
        db = get_db()
        for line in compoundKeys:
            db.execute('UPDATE entries SET text = ? WHERE page = ? AND field = ?', [line[0], line[1], line[2]])
        db.commit()
        return redirect(url_for('populateIndexPage'))
    elif request.method == 'GET':
        db = get_db()
        cur = db.execute('SELECT id from pages')
        pages = cur.fetchall()

        data = {}

        for page in pages:
            page_data = {}

            # get entries
            cur = db.execute('SELECT * FROM entries where entries.page = ?', [page['id']])
            entries = cur.fetchall()
            page_data['entries'] = entries

            # get images
            cur = db.execute('SELECT * FROM images where images.page = ? ORDER BY id DESC', [page['id']])
            images = cur.fetchall()
            page_data['images'] = images

            # get files
            cur = db.execute('SELECT * FROM files where files.page = ? ORDER BY id DESC', [page['id']])
            files = cur.fetchall()
            page_data['files'] = files

            # get flags
            cur = db.execute('SELECT * FROM flags where flags.page = ? ORDER BY id DESC', [page['id']])
            flags = cur.fetchall()
            page_data['flags'] = flags


            data[page['id']] = page_data
        cur.close()

        return render_template('admin.html', data=data, pages=pages)

def get_entries():

    return True

def get_images():

    return True

def get_flags():

    return True

def get_files():

    return True

"""Password Hashing and Salting for Database Storage"""
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    currentUser = User('username', 'password')
    hashed_password = currentUser.pw_hash
    """New Security Constraint with Password"""
    if request.method == 'POST':
        #if request.form['username'] != app.config['USERNAME']:
        if currentUser.check_password('password') == False:
            error = 'Invalid username'
        #elif request.form['password'] != app.config['PASSWORD']:
        #elif check_password('password') == True:
        #    error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('populateVolunteerPage'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('populateIndexPage'))


# @app.route('/')
# def populateHomePage():
#     db = get_db()
#     cur = db.execute('SELECT field, text, page FROM entries ORDER BY field DESC WHERE page == \'home\' ')
#     entries = cur.fetchall()
#     return render_template('home.html', entries=entries)
#
#

@app.route('/about')
def populateAboutPage():
    db = get_db()
    cur = db.execute('SELECT field, text, page FROM entries WHERE page == \'about\' ORDER BY field DESC')
    entries = cur.fetchall()
    return render_template('about.html', entries=entries)

@app.route('/protected_content')
def populateVolunteerPage():
	db = get_db()
	cur = db.execute('SELECT field, text, page FROM entries WHERE page == \'about\' ORDER BY field DESC')
	entries = cur.fetchall()
	return render_template('protected_content.html', entries=entries)

#
# @app.route('/contact')
# def populateContactPage():
#     db = get_db()
#     cur = db.execute('SELECT field, text, page FROM entries ORDER BY field DESC, WHERE page == \'contact\' ')
#     entries = cur.fetchall()
#     return render_template('index.html', entries=entries)
#
#
# @app.route('/events')
# def populateEventsPage():
#     db = get_db()
#     cur = db.execute('SELECT field, text, page FROM entries ORDER BY field DESC, WHERE page == \'events\' ')
#     entries = cur.fetchall()
#     return render_template('events.html', entries=entries)
#
#
# @app.route('/get_help')
# def populateGetHelpPage():
#     db = get_db()
#     cur = db.execute('SELECT field, text, page FROM entries ORDER BY field DESC, WHERE page == \'gethelp\' ')
#     entries = cur.fetchall()
#     return render_template('get_help.html', entries=entries)
#
#
# @app.route('/get_involved')
# def populateGetInvolvedPage():
#     db = get_db()
#     cur = db.execute('SELECT field, text, page FROM entries ORDER BY field DESC, WHERE page == \'getinvolved\' ')
#     entries = cur.fetchall()
#     return render_template('get_involved.html', entries=entries)
#
#
# @app.route('/history')
# def populateHistoryPage():
#     db = get_db()
#     cur = db.execute('SELECT field, text, page FROM entries ORDER BY field DESC, WHERE page == \'history\' ')
#     entries = cur.fetchall()
#     return render_template('history.html', entries=entries)
#
#
# @app.route('/meet_the_team')
# def populateMeetTheTeamPage():
#     db = get_db()
#     cur = db.execute('SELECT field, text, page FROM entries ORDER BY field DESC, WHERE page == \'meettheteam\' ')
#     entries = cur.fetchall()
#     return render_template('meet_the_team.html', entries=entries)
#
#
# @app.route('/supporters')
# def populateSupportersPage():
#     db = get_db()
#     cur = db.execute('SELECT field, text, page FROM entries ORDER BY field DESC, WHERE page == \'supporters\' ')
#     entries = cur.fetchall()
#     return render_template('supporters.html', entries=entries)
#
#
# @app.route('/whats_happening')
# def populateWhatsHappeningPage():
#     db = get_db()
#     cur = db.execute('SELECT field, text, page FROM entries ORDER BY field DESC, WHERE page == \'whatshappening\' ')
#     entries = cur.fetchall()
#     return render_template('whats_happening.html', entries=entries)


if __name__ == '__main__':
    app.run()
