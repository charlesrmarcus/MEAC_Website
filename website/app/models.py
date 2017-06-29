from app import app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


'''
    Home page fields
'''
class HomePageText(db.Model):
    __tablename__ = 'home_page_text'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    display_name = db.Column(db.Text)
    description = db.Column(db.Text)
    text_content = db.Column(db.Text)


class HomePageFlags(db.Model):
    __tablename__ = 'home_page_flags'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    display_name = db.Column(db.Text)
    description = db.Column(db.Text)
    flag_value = db.Column(db.Boolean)

'''
    About page fields
'''
class AboutPageText(db.Model):
    __tablename__ = 'about_page_text'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    display_name = db.Column(db.Text)
    description = db.Column(db.Text)
    text_content = db.Column(db.Text)


'''
    Contact page fields
'''
class ContactPageText(db.Model):
    __tablename__ = 'contact_page_text'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    display_name = db.Column(db.Text)
    description = db.Column(db.Text)
    text_content = db.Column(db.Text)


'''
    Get Involved page fields
'''
class GetInvolvedPageText(db.Model):
    __tablename__ = 'get_involved_page_text'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    display_name = db.Column(db.Text)
    description = db.Column(db.Text)
    text_content = db.Column(db.Text)


class GetInvolvedProductsText(db.Model):
    __tablename__ = 'get_involved_product_text'
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.Text)
    field_name = db.Column(db.Text)
    text_content = db.Column(db.Text)


'''
    Get Involved Volunteer page fields
'''
class GetInvolvedVolunteerPageText(db.Model):
    __tablename__ = 'get_involved_volunteer_page_text'
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.Text)
    field_name = db.Column(db.Text)
    text_content = db.Column(db.Text)


'''
    Our Impact page fields
'''
class OurImpactPageText(db.Model):
    __tablename__ = 'our_impact_page_text'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    text_content = db.Column(db.Text)


'''
    Get Help page fields
'''
class GetHelpPageText(db.Model):
    __tablename__ = 'get_help_page_text'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    text_content = db.Column(db.Text)


class GetHelpPageAssistanceTabListItem(db.Model):
    __tablename__ = 'get_help_page_assistance_list_item'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    title_content = db.Column(db.Text)
    text_content = db.Column(db.Text)


class GetHelpPageProgramsTabListItem(db.Model):
    __tablename__ = 'get_help_page_programs_list_item'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    title_content = db.Column(db.Text)
    text_content = db.Column(db.Text)


class GetHelpPageAssistanceTabListItem(db.Model):
    __tablename__ = 'get_help_page_assistance_tab'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    title_content = db.Column(db.Text)
    text_content = db.Column(db.Text)


class GetHelpPageProgramsTabListItem(db.Model):
    __tablename__ = 'get_help_page_programs_tab'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    title_content = db.Column(db.Text)
    text_content = db.Column(db.Text)


class GetHelpPageEventsTabListItem(db.Model):
    __tablename__ = 'get_help_page_events_tab'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    title_content = db.Column(db.Text)
    text_content = db.Column(db.Text)


'''
    Supporters page fields
'''
class SupportersPageText(db.Model):
    __tablename__ = 'supporters_page_text'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    supporter_type = db.Column(db.Text)
    text_content = db.Column(db.Text)


'''
    Meet the Team page fields
'''
class MeetTheTeamPagePeople(db.Model):
    __tablename__ = 'meet_the_team_page_people'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    phone_number = db.Column(db.Text)
    email = db.Column(db.Text)
    role = db.Column(db.Text)
    visibility = db.Column(db.Boolean)
    file_path = db.Column(db.Text)


'''
    History Page
'''
class HistoryPageTimelineItem(db.Model):
    __tablename__ = 'history_page_timeline'
    id = db.Column(db.Integer, primary_key=True)
    field_name = db.Column(db.Text)
    year = db.Column(db.Integer)
    item_title = db.Column(db.Text)
    item_subtitle = db.Column(db.Text)
    item_text = db.Column(db.Text)


'''
    Protected Page
'''


'''
    Files
'''


'''
    Admin Users
'''

db.create_all()