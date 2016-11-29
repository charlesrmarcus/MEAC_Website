# -*- coding: utf-8 -*-
"""
    Erik Hansen
    MEAC_Website 
"""

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__, template_folder=pages)


# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'MEAC_Website.db'),
    DEBUG=True,
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
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_


@app.route('/')
def populateIndexPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by id desc, where page == \'index\' ')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)


# @app.route('/add', methods=['POST'])
# def add_entry():
#     if not session.get('logged_in'):
#         abort(401)
#     db = get_db()
#     db.execute('insert into entries (title, text) values (?, ?)',
#                [request.form['title'], request.form['text']])
#     db.commit()
#     flash('New entry was successfully posted')
#     return redirect(url_for('populateIndexPage'))

@app.route('/admin', methods=['GET', 'POST'])
def adminPage():
    if request.method == 'POST':
        db = get_db()
        for fields in request.form:
            db.execute('update entries set text = ? where page = ? and title = ?', [fields['text'], fields['page'], fields['title']])
        db.commit()
        return redirect(url_for('populateIndexPage'))
    elif request.method == 'GET':
        # retrieve all fields from db and populate admin page
        db = get_db()
        cur = db.execute('select page, title, text from entries order by page, title desc')
        entries = cur.fetchall()

        # potentially store in a dict for lookup capabilities
        # need to store by page so we can cluster the fields

        return render_template('admin.html', entries=entries)
    else:
        # error = 'improper method'
        abort(401)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('populateIndexPage'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('populateIndexPage'))

