"""
    Test Database - SQLAlchemy Extension 
    Erik Hansen & Charlie Marcus 
"""

import os
from datetime import datetime
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from collections import defaultdict
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

""" WTF forms implemented - 2/17/2017 """
from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, DateTimeField, TextAreaField, BooleanField, SelectField, PasswordField, RadioField#, RecaptchaField
from wtforms.validators import Required, Optional, Regexp, DataRequired, Length, Email
from werkzeug import secure_filename

"""Flask Login"""
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user, logout_user

""" Emergency Closure Alert - 2/21/2017 """
from datetime import datetime, date, time

""" Foreign Key Functionality """
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection

@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


"""Database Configuration"""
#import initialize_db
app = Flask(__name__, template_folder='pages')


# Load default config and override config from an environment variable
app.config.update(dict(
    # DATABASE=os.path.join(app.root_path, 'MEAC_Website.db'),
    DATABASE='C:\Users\E967288\PycharmProjects\MEAC_Website\MEAC_Website.db',
    DEBUG=False,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='password'
    
))

UPLOAD_FOLDER = "../MEAC_Website/static/uploads/"
ALLOWED_EXTENSIONS = set(['pdf','doc','docx','jpg','jpeg','png'])

"""Recaptcha Field Configurations"""
# RECAPTCHA_PUBLIC_KEY = 'key'
# RECAPTCHA_PRIVATE_KEY = 'secret'

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# basedir = os.path.abspath(os.path.dirname('MEAC_Website.db'))
basedir = 'C:\Users\E967288\PycharmProjects\MEAC_Website\MEAC_Website.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\Users\E967288\PycharmProjects\MEAC_Website\data.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

"""Login Manager"""
login_manager = LoginManager()
login_manager.protection = 'strong'
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_admin(admin_id):
    return Admin.query.get(int(admin_id))

""" Create the Database """
db = SQLAlchemy(app)

""" Database Models """
class Page(db.Model):
    __tablename__ = 'pages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    display_name = db.Column(db.String(64), unique=True)
    showContextEditor = db.Column(db.Boolean, nullable=False)
    showFileEditor = db.Column(db.Boolean, nullable=False)
    showUserEditor = db.Column(db.Boolean, nullable=False)
    showAddDeleteEditor = db.Column(db.Boolean, nullable=False)
    showHistoryEditor = db.Column(db.Boolean, nullable=False)
    showAddDeleteFile = db.Column(db.Boolean, nullable=False)
    content = db.relationship('Content', backref='page')
    files = db.relationship('Files', backref='page')
    users = db.relationship('Users', backref='page')
    listitems = db.relationship('ListItem', backref='page')
    
    def __init__(self, name, display_name):
        self.name = name
        self.display_name = display_name
        self.showContextEditor = False
        self.showFileEditor = False
        self.showUserEditor = False
        self.showAddDeleteEditor = False
        self.showHistoryEditor = False
        self.showAddDeleteFile = False
    
    def __repr__(self):
        return '<Page %r>' % self.id
        
    """Setters/Getters"""
    def setContextEditor(self, editorValue):
        self.showContextEditor = editorValue
    def setFileEditor(self, editorValue):
        self.showFileEditor = editorValue
    def setUserEditor(self, editorValue):
        self.showUserEditor = editorValue
    def setAddDeleteEditor(self, editorValue):
        self.showAddDeleteEditor = editorValue
    def setHistoryEditor(self, editorValue):
        self.showHistoryEditor = editorValue
    def setAddDeleteFile(self, editorValue):
        self.showAddDeleteFile = editorValue

class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(64), nullable=False)
    display_name = db.Column(db.String(64), nullable=True)
    title = db.Column(db.Text, nullable=True)
    text = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    
    def __init__(self, field, display_name, text):
        self.field = field
        self.display_name = display_name
        self.text = text
        
    def set_description(self, description):
        self.description = description
    def set_title(self, title):
        self.title = title
    
    def __repr__(self):
        return '<Content %r>' % self.field
        
class ListItem(db.Model):
    __tablename__ = 'listitems'
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(64), nullable=False)
    text = db.Column(db.String(64), nullable=True)
    description = db.Column(db.Text, nullable=True)
    title = db.Column(db.Text, nullable=True)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    
    def __init__(self, field, text):
        self.field = field
        self.text = text
        
    def set_description(self, description):
        self.description = description
    def set_title(self, title):
        self.title = title
        
    def __repr__(self):
        return '<ListItem %r>' % self.field
        
        
class Files(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(64), nullable=False)
    display_name = db.Column(db.String(64), nullable=False)
    file_path = db.Column(db.String(128), nullable=False)
    visible = db.Column(db.Boolean, nullable=True)
    description = db.Column(db.Text, nullable=True)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    
    def __init__(self, field, display_name, file_path):
        self.field = field
        self.display_name = display_name
        self.file_path = file_path
        
    def set_description(self, description):
        self.description = description
    def set_visibility(self, visible):
        self.visible = visible
    
    def __repr__(self):
        return '<File %r>' % self.field
        
class Flags(db.Model):
    __tablename__ = 'flags'
    id = db.Column(db.Integer, primary_key=True, index=True)
    field = db.Column(db.String(64), nullable=False)
    flag_value = db.Column(db.Boolean, nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    
    def __init__(self, field, flag_value):
        self.field = field
        self.flag_value = flag_value
    
    def __repr__(self):
        return '<File %r>' % self.field
        
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(64), nullable=False)
    display_name = db.Column(db.String(64), nullable=False)
    phone_number = db.Column(db.Text, nullable=True, unique=True)
    email = db.Column(db.Text, nullable=True, unique=True)
    description = db.Column(db.Text, nullable=True)
    visible = db.Column(db.Boolean, nullable=False)
    file_path = db.Column(db.String(128), nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    
    """Default Methods"""
    def __init__(self, field, display_name):
        self.field = field
        self.display_name = display_name
    def __repr__(self):
        return '<User %r>' % self.username
        
    """Getter/Setter"""
    def set_email(self, email):
        self.email = email
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number     
    def set_description(self, description):
        self.description = description    
    def set_visibility(self, visible):
        self.visible = visible
    def set_file_path(self, file_path):
        self.file_path = file_path
        

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    pw_hash = db.Column(db.String(128))
    #page_id = db.Column(db.Integer, db.ForeignKey('pages.id'))
    
    """Inherited Flask_Login Credentials"""
    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)
        
    """Default Methods"""
    def __init__(self, field, username, password):
        self.field = field
        self.username = username
        self.password = password
    def __repr__(self):
        return '<Admin %r>' % self.username
        
    """Password Hashing and Salting for Database Storage""" 
    #@password.setter
    def hash_password(self, password):
        self.pw_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.pw_hash, password)
        
        
""" Database Methods """
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    # db = get_db()
    # with app.open_resource('schema.sql', mode='r') as f:
        # db.cursor().executescript(f.read())
    # db.commit()
    import initialize_db
    initialize_db
    

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
        
        
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

    
def flash_errors(form):
    errorList = []
    for field, errors in form.errors.items():
        for error in errors:
            errorMessage = u"Error in the %s field - %s" % (getattr(form, field).label.text, error)
            errorList.append(errorMessage)
    return errorList
            
        
""" WTF Form Classes """
class PageForm(FlaskForm):
    #Page Field
    choices = []
    page = SelectField('Page Name', choices)
    submit = SubmitField('Go')
    
class ContentForm(FlaskForm):
    #Content Field
    choices = []
    content_field = SelectField('Content Field', choices)
    content_submit = SubmitField('Submit')
    
class SaveContentForm(FlaskForm):
    content_display_name = StringField('Content Name', validators=[Required()])
    content_text = TextAreaField('Content Text', validators=[Required(message="Required Field")])
    content_description = TextAreaField('Content Description', validators=[Required(message="Required Field")])
    save_content = SubmitField('Save')
    
class NewHistoryForm(FlaskForm):
    display_name = StringField('History Header', validators=[Required()])
    title = StringField('History Paragraph Title', validators=[Required()])
    text = TextAreaField('History Text', validators=[Required()])
    description = TextAreaField('History Year', validators=[Required()])
    save_content = SubmitField('Add')
    
class NewContentForm(FlaskForm):
    choices = []
    title = StringField('Content Title', validators=[Required()])
    text = TextAreaField('Content Text', validators=[Required()])
    description = SelectField('Content Description', choices)
    save_content = SubmitField('Add')
    
class UserForm(FlaskForm):
    #User Field
    choices = []
    users = SelectField('Team Members', choices)
    submit = SubmitField('Submit')
    
class SaveUserForm(FlaskForm):
    display_name = StringField('Full Name', validators=[Required()])
    phone_number = StringField('Phone Number', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    description = TextAreaField('Role Description', validators=[Required()])
    #visibility = BooleanField('Visibility/Check if Visible', validators=[Required()])
    file = FileField('Profile Picture Selection', validators=[Required()])
    save_user = SubmitField('Save')
    
    
class NewTeamForm(FlaskForm):
    display_name = StringField('Full Name', validators=[Required()])
    phone_number = StringField('Phone Number', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    description = TextAreaField('Role Description', validators=[Required()])
    #visibility = BooleanField('Visibility/Check if Visible', validators=[Required()])
    file = FileField('Profile Photo Selection', validators=[Required()])
    save_content = SubmitField('Add')

class FileForm(FlaskForm):
    #File Field
    choices = []
    file_field = SelectField('File Field', choices)
    file_submit = SubmitField('Submit')
    
class SaveFileForm(FlaskForm):
    file = FileField('File Selection (Photos or PDFs)', validators=[Required()])
    file_display_name = StringField('File Name', validators=[Required()])
    #file_visibility = BooleanField('Check to make visible', validators=[Optional()])
    save_file = SubmitField('Save')
    
class NewFileForm(FlaskForm):
    file = FileField('File Upload (PDFs only)', validators=[Required()])
    file_name = StringField('File Name', validators=[Required()])
    file_description = TextAreaField('File Description', validators=[Required()])
    add_file = SubmitField('Add')
    
class DeleteForm(FlaskForm):
    deleteButton = SubmitField('Delete')
    
class SelectDeleteForm(FlaskForm):
    choices = []
    field = SelectField('Content Field', choices)
    delete = SubmitField('Delete')
      
class FlagForm(FlaskForm):
    # #Red Banner Alert Implementation - 2/21/2017
    # start_date = DateTimeField('Closed From -', format='%Y-%m-%d %H:%M:%S', validators=[Optional()])
    # end_date = DateTimeField('Closed Until -', format='%Y-%m-%d %H:%M:%S', validators=[Optional()])
    # #Flag Field
    # flag_field = StringField('Flag Field', validators=[Required()])
    #flag = RadioField(choices=[(True, 'MEAC Closed'), (False, 'MEAC Open')], validators=[Required()])
    flag = BooleanField('Check if MEAC Closed', validators=[Required()])
    
    submit = SubmitField('Submit')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    #recaptcha = RecaptchaField()
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login In')
    
""" Query Functions """
def list2dict(list):
    dict = {}
    counter = 0
    while counter < len(list):
        dict[list[counter].field] = list[counter].text
        counter += 1
    return dict
    
def get_content(list):
    dict = {}
    counter = 0
    while counter < len(list):
        dict[list[counter].field] = (list[counter].display_name, list[counter].text)
        counter += 1
    return dict
    
def get_files(list):
    dict = {}
    counter = 0
    while counter < len(list):
        dict[list[counter].field] = (list[counter].display_name, list[counter].file_path)
        counter += 1
    return dict

def get_flags(list):
    dict = {}
    counter = 0
    while counter < len(list):
        dict[list[counter].field] = list[counter].flag_value
        counter += 1
    return dict
        
""" View Functions/Templates """
currentPage_id = 0
showEditors = False
editContent = False
addContent = False
editFile = False
editUser = False
editHistory = False
addFile = False
page_name = ''
@app.route('/new_admin_flow1', methods=['GET', 'POST'])
@login_required
def new_adminPage():
    #Query the Database to get Possible Page Entries
    # global editContent, editFile
    # editContent = False
    # editFile = False
    pages = Page.query.order_by(Page.name)
    choices = [('', '')]
    
    for page in pages:
        name_pair = (page.name, page.display_name)
        choices.append(name_pair)
    
    #Initialized Form Values   
    #Database Variables/Updates
    page = ''
    form = PageForm()
    form.page.choices = choices
    if form.is_submitted() and form.submit.data:
        
        page = form.page.data
        if (page == "" or page == None):
            flash("You need to select a page to edit before proceeding.")
            return redirect(url_for('new_adminPage'))
        else:
            selectedPage = Page.query.filter_by(name=str(page)).first()
            global currentPage_id, editContent, editFile, editUser, editHistory, showEditors, page_name, addContent, addFile
            showEditors = True
            currentPage_id = selectedPage.id
            editContent = selectedPage.showContextEditor
            editFile = selectedPage.showFileEditor
            # if selectedPage.id == 12:
                # # TODO New Content Creation for Meet the Team Page
            editUser = selectedPage.showUserEditor
            addContent = selectedPage.showAddDeleteEditor
            addFile = selectedPage.showAddDeleteFile
            editHistory = selectedPage.showHistoryEditor
            page_name = selectedPage.display_name
            return redirect(url_for('new_adminPage'))
            
    """Updating Booleans"""
    global show_user, show_content, show_file
    show_user = False
    show_content = False
    show_file = False
    
    return render_template('new_admin_flow1.html', form=form, pages=pages, editContent=editContent, editFile=editFile, editUser=editUser, editHistory=editHistory, showEditors=showEditors, addContent=addContent, addFile=addFile, page_name=page_name)
    
@app.route('/add_content', methods=['GET', 'POST'])
@login_required
def add_content():
    new_content_form = NewContentForm()
    delete_form = SelectDeleteForm()
    listitems = ListItem.query.filter_by(page_id=currentPage_id).all()
    delete_choices = []
    for element in listitems:
        if element.title != None and currentPage_id == 4:
            delete_pair = (element.field, element.title)
            delete_choices.append(delete_pair)
        else:
            delete_pair = (element.field, element.text)
            delete_choices.append(delete_pair)
    delete_form.field.choices = delete_choices   


    if currentPage_id == 4:
        desc_choices = [('assistance', 'Assistance'), ('events', 'Events'), ('programs', 'Programs')]
    elif currentPage_id == 7:
        desc_choices = [('marketplace', 'Marketplace'), ('clothing', 'Clothing'), ('misc', 'Miscellaneous')]
    elif currentPage_id == 13:
        desc_choices = [('churches', 'Churches'), ('organizations', 'Organizations')]
        
    new_content_form.description.choices = desc_choices
        
    if new_content_form.validate_on_submit() and new_content_form.save_content.data:
        new_listitem = ListItem(field='new_listitem', text=new_content_form.text.data)
        new_listitem.set_description(new_content_form.description.data)
        new_listitem.set_title(new_content_form.title.data)
        currentPage = Page.query.get(currentPage_id)
        currentPage.listitems.append(new_listitem)
        print currentPage.content
        """Database Commit"""
        flash('Your changes were saved!')
        db.session.commit()
        return redirect(url_for('add_content'))
    else:
        errorList = flash_errors(new_content_form)
        
    if delete_form.is_submitted() and delete_form.delete.data:
        current_list = ListItem.query.filter_by(field=delete_form.field.data).first()
        db.session.delete(current_list)
        flash('Your changes were saved!')
        db.session.commit()
        return redirect(url_for('add_content'))
    
    """Updating Booleans"""
    global showEditors, editContent, addContent, editFile, editUser, editHistory, addFile
    showEditors = False
    editContent = False
    addContent = False
    editFile = False
    editUser = False
    editHistory = False
    addFile = False
    
    """Updating Booleans"""
    global show_user, show_content, show_file
    show_user = False
    show_content = False
    show_file = False
    
    return render_template('add_content.html', new_content_form=new_content_form, delete_form=delete_form, errorList=errorList)
    
    
@app.route('/add_files', methods=['GET', 'POST'])
@login_required
def add_files():
    file_form = NewFileForm()
    delete_form = SelectDeleteForm()
    files = Files.query.filter_by(page_id=currentPage_id).all()
    delete_choices = []
    for element in files:
        delete_pair = (element.field, element.display_name)
        delete_choices.append(delete_pair)
    delete_form.field.choices = delete_choices
    
    if file_form.validate_on_submit() and file_form.add_file.data:
        file = file_form.file.data
        if file != None:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_file_path = "../static/uploads/" + filename
            new_file = Files(field='new_file', display_name=file_form.file_name.data, file_path=new_file_path)
            new_file.set_description(file_form.file_description.data)
            currentPage = Page.query.get(currentPage_id)
            currentPage.files.append(new_file)
            
            """Database Commit"""
            flash('Your changes were saved!')
            db.session.commit()
            return redirect(url_for('add_files'))
    else:
        errorList = flash_errors(file_form)
        
    if delete_form.is_submitted() and delete_form.delete.data:
        current_list = Files.query.filter_by(field=delete_form.field.data).first()
        db.session.delete(current_list)
        flash('Your changes were saved!')
        db.session.commit()
        return redirect(url_for('add_files'))
    
    """Updating Booleans"""
    global showEditors, editContent, addContent, editFile, editUser, editHistory, addFile
    showEditors = False
    editContent = False
    addContent = False
    editFile = False
    editUser = False
    editHistory = False
    addFile = False
    
    
    """Updating Booleans"""
    global show_user, show_content, show_file
    show_user = False
    show_content = False
    show_file = False
        
    return render_template('add_files.html', file_form=file_form, delete_form=delete_form, errorList=errorList)
    
@app.route('/add_history', methods=['GET', 'POST'])
@login_required
def add_history():
    new_content_form = NewHistoryForm()
    delete_form = SelectDeleteForm()
    content = Content.query.filter_by(page_id=currentPage_id).all()
    delete_choices = []
    for element in content:
            delete_pair = (element.field, u"%s - %s" % (element.description,element.title))
            delete_choices.append(delete_pair)
    delete_form.field.choices = delete_choices    

    if new_content_form.validate_on_submit() and new_content_form.save_content.data:
        new_content = Content(field='new_content', display_name=new_content_form.display_name.data, text=new_content_form.text.data)
        new_content.set_description(new_content_form.description.data)
        new_content.set_title(new_content_form.title.data)
        currentPage = Page.query.get(currentPage_id)
        currentPage.content.append(new_content)
      
        """Database Commit"""
        flash('Your changes were saved!')
        db.session.commit()
        return redirect(url_for('add_history'))
    else:
        errorList = flash_errors(new_content_form)
        
    if delete_form.is_submitted() and delete_form.delete.data:
        current_list = Content.query.filter_by(field=delete_form.field.data).first()
        db.session.delete(current_list)
        flash('Your changes were saved!')
        db.session.commit()
        return redirect(url_for('add_history'))
    
    """Updating Booleans"""
    global showEditors, editContent, addContent, editFile, editUser, editHistory, addFile
    showEditors = False
    editContent = False
    addContent = False
    editFile = False
    editUser = False
    editHistory = False
    addFile = False
    
    
    """Updating Booleans"""
    global show_user, show_content, show_file
    show_user = False
    show_content = False
    show_file = False
    
    return render_template('add_history.html', new_content_form=new_content_form, delete_form=delete_form, errorList=errorList)

@app.route('/new_team', methods=['GET', 'POST'])
@login_required
def new_teamContent():
    team_form = NewTeamForm()
    if team_form.validate_on_submit() and team_form.save_content.data:
        file = team_form.file.data
        if file != None:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_file_path = "../static/uploads/" + filename
            """Create New User Object"""
            new_team_member = Users(field="new_team_member", display_name=team_form.display_name.data)
            new_team_member.set_phone_number(team_form.phone_number.data)
            new_team_member.set_email(team_form.email.data)
            new_team_member.set_description(team_form.description.data)
            new_team_member.set_visibility(team_form.visibility.data)
            new_team_member.set_file_path(new_file_path)
            
            currentPage = Page.query.get(currentPage_id)
            currentPage.users.append(new_team_member)
            """Database Commit"""
            flash('Your changes were saved!')
            db.session.commit()
        return redirect(url_for('new_teamContent'))
    else:
        errorList = flash_errors(team_form)
    
    """Updating Booleans"""
    global showEditors, editContent, addContent, editFile, editUser, editHistory, addFile
    showEditors = False
    editContent = False
    addContent = False
    editFile = False
    editUser = False
    editHistory = False
    addFile = False
    
    
    """Updating Booleans"""
    global show_user, show_content, show_file
    show_user = False
    show_content = False
    show_file = False
    return render_template('new_team.html', team_form=team_form, errorList=errorList)
    
show_user = False
queryUserField = 'office_assistant_user'
@app.route('/edit_team', methods=['GET', 'POST'])
@login_required
def edit_teamContent():
    users = Users.query.filter_by(page_id=currentPage_id).all()
    userQuery = Users.query.filter_by(field=queryUserField).first()
    
    user_choices = []
    for user in users:
        user_pair = (user.field, user.display_name)
        user_choices.append(user_pair)
        
    user_form = UserForm()
    user_form.users.choices = user_choices
    save_form = SaveUserForm()
    delete_form = DeleteForm()
    if user_form.is_submitted() and user_form.submit.data:
        global show_user
        show_user = True
        global queryUserField
        queryUserField = user_form.users.data
        userQuery = Users.query.filter_by(field=queryUserField).first()
        return redirect(url_for('edit_teamContent'))
        
    if save_form.validate_on_submit() and save_form.save_user.data:
        print "Validated!"
        file = save_form.file.data
        #if save_form.display_name.data != '' and file != None:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_file_path = "../static/uploads/" + filename
    
        userQuery.display_name = save_form.display_name.data
        userQuery.set_phone_number(save_form.phone_number.data)
        userQuery.set_email(save_form.email.data)
        userQuery.set_description(save_form.description.data)
        #userQuery.set_visibility(save_form.visibility.data)
        userQuery.set_file_path(new_file_path)
        db.session.commit()
        flash('Your changes were saved!')
        return redirect(url_for('edit_teamContent'))
    else:
        errorList = flash_errors(save_form)
        
    if delete_form.is_submitted() and delete_form.deleteButton.data:
        db.session.delete(userQuery)
        db.session.commit()
        flash('Your changes were saved!')
        return redirect(url_for('edit_teamContent'))
 
    """Updating Booleans"""
    global showEditors, editContent, addContent, editFile, editUser, editHistory, addFile
    showEditors = False
    editContent = False
    addContent = False
    editFile = False
    editUser = False
    editHistory = False
    addFile = False
    
    
    """Updating Booleans"""
    global show_content, show_file
    show_content = False
    show_file = False
    
    return render_template('edit_team.html', user_form=user_form, save_form=save_form, delete_form=delete_form, show_user=show_user, userQuery=userQuery, errorList=errorList)
    
show_content = False
queryContentField = 'donate_content'
@app.route('/new_admin_flow2', methods=['GET', 'POST'])
@login_required
def new_adminContent():
    #Query Entries, Files, and Images
    content = Content.query.filter_by(page_id=currentPage_id).all()
    contentQuery = Content.query.filter_by(field=queryContentField).first()
    
    content_choices = []
    for entry in content:
        entry_pair = (entry.field, entry.display_name)
        content_choices.append(entry_pair)
    
    content_form = ContentForm()
    content_form.content_field.choices = content_choices
    save_form = SaveContentForm()
    if content_form.is_submitted() and content_form.content_submit.data:
        global show_content
        show_content = True
        global queryContentField
        queryContentField = content_form.content_field.data
        contentQuery = Content.query.filter_by(field=content_form.content_field.data).first()
        #content_details = {'field': contentQuery.field, 'text': contentQuery.text, 'description': contentQuery.description}
        return redirect(url_for('new_adminContent'))
        
    if save_form.validate_on_submit() and save_form.save_content.data:
        #if save_form.content_text.data != '':
        if true: # only for history
            contentQuery.title = save_form.content_display_name.data
        contentQuery.display_name = save_form.content_display_name.data
        contentQuery.text = save_form.content_text.data
        contentQuery.set_description(save_form.content_description.data)
        """Database Commit"""
        db.session.commit()
        flash('Your changes were saved!')
        return redirect(url_for('new_adminContent'))
    else:
        errorList = flash_errors(save_form)
        

    """Updating Booleans"""
    global showEditors, editContent, addContent, editFile, editUser, editHistory, addFile
    showEditors = False
    editContent = False
    addContent = False
    editFile = False
    editUser = False
    editHistory = False
    addFile = False
    
    
    """Updating Booleans"""
    global show_user, show_file
    show_user = False
    show_file = False
    
    return render_template('new_admin_flow2.html', content_form=content_form, save_form=save_form, show_content=show_content, contentQuery=contentQuery, errorList=errorList)

    
show_file = False
queryFileField = 'united_way_image'
@app.route('/new_admin_flow3', methods=['GET', 'POST'])
@login_required
def new_adminFile():    
    files = Files.query.filter_by(page_id=currentPage_id).all()
    fileQuery = Files.query.filter_by(field=queryFileField).first()
    
    file_choices = []
    for file in files:
        file_pair = (file.field, file.display_name)
        file_choices.append(file_pair)
        
    file_form = FileForm()
    file_form.file_field.choices = file_choices
    save_form = SaveFileForm()
    if file_form.is_submitted() and file_form.file_submit.data:
        global show_file
        show_file = True
        global queryFileField
        queryFileField = file_form.file_field.data
        fileQuery = Files.query.filter_by(field=file_form.file_field.data).first()
        #file_details = {'field': fileQuery.field, 'file_path': fileQuery.file_path, 'visibility': fileQuery.visible}
        return redirect(url_for('new_adminFile'))
        
    if save_form.validate_on_submit() and save_form.save_file.data:
        new_file = save_form.file.data
        if new_file != None:
            filename = secure_filename(new_file.filename)
            new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fileQuery.file_path = "../static/uploads/" + filename
            #fileQuery.visibility = save_form.file_visibility.data
            fileQuery.display_name = save_form.file_display_name.data
        """Database Commit"""
        db.session.commit()
        flash('Your changes were saved!')
        return redirect(url_for('new_adminFile'))
    else:
        errorList = flash_errors(save_form)
        
    """Updating Booleans"""
    global showEditors, editContent, addContent, editFile, editUser, editHistory, addFile
    showEditors = False
    editContent = False
    addContent = False
    editFile = False
    editUser = False
    editHistory = False
    addFile = False
    
    
    """Updating Booleans"""
    global show_user, show_content
    show_user = False
    show_content = False
    
    return render_template('new_admin_flow3.html', file_form=file_form, save_form=save_form, show_file=show_file, fileQuery=fileQuery, errorList=errorList)

show_flag = False
@app.route('/new_admin_flow4', methods=['GET', 'POST'])
@login_required
def new_adminFlag():
    form = FlagForm()
    if form.is_submitted():
        global show_flag
        show_flag = form.flag.data
        flash('Your changes were saved!')
        return redirect(url_for('new_adminFlag'))
    
    """Updating Booleans"""
    global showEditors, editContent, addContent, editFile, editUser, editHistory, addFile
    showEditors = False
    editContent = False
    addContent = False
    editFile = False
    editUser = False
    editHistory = False
    addFile = False
    
    
    """Updating Booleans"""
    global show_user, show_content, show_file
    show_user = False
    show_content = False
    show_file = False
    return render_template('new_admin_flow4.html', form=form)
    
@app.route('/admin_splash')
@login_required
def admin_splash():
    """Updating Booleans"""
    global showEditors, editContent, addContent, editFile, editUser, editHistory, addFile
    showEditors = False
    editContent = False
    addContent = False
    editFile = False
    editUser = False
    editHistory = False
    addFile = False
    
    
    """Updating Booleans"""
    global show_user, show_content, show_file
    show_user = False
    show_content = False
    show_file = False
    return render_template('admin_splash.html')
    
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    """New Security Constraint with Password"""
    form = LoginForm()
    if form.validate_on_submit():
        print "Validated!"
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is not None and admin.verify_password(form.password.data):
            login_user(admin, form.remember_me.data)
            return redirect(url_for('admin_splash'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)
    
@app.route('/volunteer_login', methods=['GET', 'POST'])
def volunteer_login():
    """New Security Constraint with Password"""
    form = LoginForm()
    if form.validate_on_submit():
        print "Validated!"
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is not None and admin.verify_password(form.password.data):
            login_user(admin, form.remember_me.data)
            return redirect(url_for('populateProtectedContentPage'))
        else:
            flash('Invalid username or password.')
    return render_template('volunteer_login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('populateHomePage'))

@app.route('/')
def populateHomePage():
    content = Content.query.filter_by(page_id=1).all()
    #Convert DB Row to Dictionary
    content_dict = get_content(content)
    print show_flag
    return render_template('home.html', content_dict=content_dict, show_flag=show_flag)

now = datetime.now()
year = now.year
#print year
    
@app.route('/base')
def populateBasePage():
    return render_template('base.html', year=year)

@app.route('/about')
def populateAboutPage():
    content = Content.query.filter_by(page_id=2).all()
    content_dict = get_content(content)
    return render_template('about.html', content_dict=content_dict)

@app.route('/protected_content')
def populateProtectedContentPage():
    files = Files.query.filter_by(page_id=12).all()
    files_dict = get_files(files)
    return render_template('protected_content.html', files=files, files_dict=files_dict)

@app.route('/contact')
def populateContactPage():
    serviceList = []
    content = Content.query.filter_by(page_id=3).all()
    for element in content:
        if element.description == 'service':
            serviceList.append(element)
      
    print serviceList
    content_dict = get_content(content)
    return render_template('contact.html', content_dict=content_dict, serviceList=serviceList)


@app.route('/event_calendar')
def populateEventCalendarPage():
    return render_template('event_calendar.html')

@app.route('/get_help')
def populateGetHelpPage():
    assistanceList = []
    programList = []
    eventsList = []
    
    listitems = ListItem.query.filter_by(page_id=4).order_by(ListItem.title).all()
    files = Files.query.filter_by(page_id=4).all()
    content = Content.query.filter_by(page_id=4).all()
    
    for element in listitems:
        if element.description == 'assistance':
            assistanceList.append(element)
        elif element.description == 'programs':
            programList.append(element)
        elif element.description == 'events':
            eventsList.append(element)
           
    content_dict = get_content(content)
    files_dict = get_files(files)
    return render_template('get_help.html', assistanceList=assistanceList, programList=programList, eventsList=eventsList, content_dict=content_dict, files_dict=files_dict)

""" Get Involved Pages """
@app.route('/get_involved')
def populateGetInvolvedPage():
    content = Content.query.filter_by(page_id=5).all()
    content_dict = get_content(content)
    return render_template('get_involved.html', content_dict=content_dict)

@app.route('/get_involved_financial')
def populateGetInvolvedFinancialPage():
    return render_template('get_involved_financial.html')
    
@app.route('/get_involved_products')
def populateGetInvolvedProductsPage():
    marketplaceList = []
    clothingList = []
    miscList = []
    listitems = ListItem.query.filter_by(page_id=7).order_by(ListItem.text).all()
    for element in listitems:
        if element.description == 'marketplace':
            marketplaceList.append(element)
        elif element.description == 'clothing':
            clothingList.append(element)
        elif element.description == 'misc':
            miscList.append(element)
    
    return render_template('get_involved_products.html', marketplaceList=marketplaceList, clothingList=clothingList, miscList=miscList)
    
@app.route('/get_involved_volunteer')
def populateGetInvolvedVolunteerPage():
    content = Content.query.filter_by(page_id=8).all()
    files = Files.query.filter_by(page_id=8).all()
    
    content_dict = get_content(content)
    files_dict = get_files(files)
    
    return render_template('get_involved_volunteer.html', files_dict=files_dict, content_dict=content_dict)

@app.route('/history')
def populateHistoryPage():
    content = Content.query.filter_by(page_id=9).order_by(Content.description).all()
    return render_template('history.html', content=content)

@app.route('/meet_the_team')
def populateMeetTheTeamPage():
    users = Users.query.filter_by(page_id=11).all()
    # entries_dict = list2dict(entries)
    return render_template('meet_the_team.html', users=users)

@app.route('/supporters')
def populateSupportersPage():
    churchList = []
    orgList = []
    listitems = ListItem.query.filter_by(page_id=13).order_by(ListItem.text).all()
    for element in listitems:
        if element.description == 'churches':
            churchList.append(element)
        elif element.description == 'organizations':
            orgList.append(element)
            
    return render_template('supporters.html', churchList=churchList, orgList=orgList)

@app.route('/impact')
def populateImpactPage():
    content = Content.query.filter_by(page_id=10).all()
    content_dict = get_content(content)
    return render_template('impact.html', content_dict=content_dict)

if __name__ == '__main__':
    app.run()