from app import app
from population import *
from models import *
from flask import render_template


@app.route('/')
def home_page():

    content = HomePageText.query.all()

    home_page_text = {}
    for item in content:
        home_page_text[item.field_name] = item

    content = HomePageFlags.query.all()

    home_page_flags = {}
    for item in content:
        home_page_flags[item.field_name] = item

    return render_template('home.html', content=home_page_text, flags=home_page_flags)


@app.route('/about')
def about_page():

    content = AboutPageText.query.all()

    about_page_text = {}
    for item in content:
        about_page_text[item.field_name] = item

    return render_template('about.html', content=about_page_text)


# to be removed, used to reset to the preset populations
@app.route('/reset')
def reset():
    populate_HomePageText()
    populate_HomePageFlags()
    populate_AboutPageText()
    return "wiped"