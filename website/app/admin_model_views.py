from app import app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import *

admin = Admin(app, name='MEAC Admin', template_mode='bootstrap3')


class HomePageTextView(ModelView):
    can_create=False
    can_delete=False
    column_list = ('display_name', 'description', 'text_content')
    form_columns = ('display_name', 'description', 'text_content')
    form_widget_args = {
        'display_name': {
            'readonly': True
        },
        'description': {
            'readonly': True
        },
    }

admin.add_view(HomePageTextView(HomePageText, db.session))


class HomePageFlagView(ModelView):
    can_create=False
    can_delete=False
    column_list = ('display_name', 'description', 'flag_value')
    form_columns = ('display_name', 'description', 'flag_value')
    form_widget_args = {
        'display_name': {
            'readonly': True
        },
        'description': {
            'readonly': True
        },
    }

admin.add_view(HomePageFlagView(HomePageFlags, db.session))


class AboutPageTextView(ModelView):
    can_create=False
    can_delete=False
    column_list = ('display_name', 'description', 'text_content')
    form_columns = ('display_name', 'description', 'text_content')
    form_widget_args = {
        'display_name': {
            'readonly': True
        },
        'description': {
            'readonly': True
        },
    }

admin.add_view(AboutPageTextView(AboutPageText, db.session))

