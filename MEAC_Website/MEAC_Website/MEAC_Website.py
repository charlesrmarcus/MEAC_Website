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
def populateHomePage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'home\' ')
    entries = cur.fetchall()
    return render_template('home.html', entries=entries)

@app.route('/about')
def populateAboutPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'about\' ')
    entries = cur.fetchall()
    return render_template('about.html', entries=entries)

@app.route('/contact')
def populateContactPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'contact\' ')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)

@app.route('/events')
def populateEventsPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'events\' ')
    entries = cur.fetchall()
    return render_template('events.html', entries=entries)

@app.route('/get_help')
def populateGetHelpPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'gethelp\' ')
    entries = cur.fetchall()
    return render_template('get_help.html', entries=entries)

@app.route('/get_involved')
def populateGetInvolvedPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'getinvolved\' ')
    entries = cur.fetchall()
    return render_template('get_involved.html', entries=entries)

@app.route('/history')
def populateHistoryPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'history\' ')
    entries = cur.fetchall()
    return render_template('history.html', entries=entries)

@app.route('/meet_the_team')
def populateMeetTheTeamPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'meettheteam\' ')
    entries = cur.fetchall()
    return render_template('meet_the_team.html', entries=entries)

@app.route('/supporters')
def populateSupportersPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'supporters\' ')
    entries = cur.fetchall()
    return render_template('supporters.html', entries=entries)

@app.route('/whats_happening')
def populateWhatsHappeningPage():
    db = get_db()
    cur = db.execute('select title, text, page from entries order by title desc, where page == \'whatshappening\' ')
    entries = cur.fetchall()
    return render_template('whats_happening.html', entries=entries)

@app.route('/admin', methods=['GET', 'POST'])
def adminPage():
    if not session.get('logged_in'):
        abort(401)
    if request.method == 'POST':
        db = get_db()
        for fields in request.form:
            
            
            compoundKeys = [] # list of tuples
            foreach(value in fields):
                compoundKeys.append((value[0].split(':')[0], value[0].split(':')[1]), value[1])


            db.execute('update entries set text = ? where page = ? and title = ?', [compoundKeys[0]])
            # db.execute('update entries set text = ? where page = ? and title = ?', [fields['text'], fields['page'], fields['title']])
        db.commit()
        return redirect(url_for('populateIndexPage'))
    elif request.method == 'GET':
        db = get_db()
        cur = db.execute('select page, title, text from entries order by page, title desc')
        entries = cur.fetchall()
        # TODO may need to convert entries to dict

        return render_template('admin.html', entries=entries)
    else:
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
            return redirect(url_for('adminPage'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('populateIndexPage'))

