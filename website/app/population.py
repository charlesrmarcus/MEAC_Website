from models import *


def wipe_db():
    db.drop_all()


def populate_HomePageText():
    HomePageText.query.delete()

    content = []

    content.append(HomePageText(field_name="donate_content",
                                description="Small text field describing the need to donate and how to contribute to MEAC.",
                                display_name="Donate Content",
                                text_content='Please help us continue to raise up one family at a time by taking a moment to donate.'))

    content.append(HomePageText(field_name="get_involved_content",
                                description="Text field describing volunteering and how to become involved at MEAC",
                                display_name="Get Involved",
                                text_content='We have a need for volunteer help and various product donations.'))

    content.append(HomePageText(field_name="about_us_content", description="Short blurb about MEAC, and its mission",
                                display_name="About Us",
                                text_content="We've been working to meet the needs of our community since 1986"))

    content.append(HomePageText(field_name="get_help_content",
                                description="Small text field talking about MEACs ability to provide aid",
                                display_name="Get Help",
                                text_content="Learn about the assistance we offer and access the forms you'll need to fill out to apply"))

    content.append(HomePageText(field_name="meac_description_content", description="Mission statement",
                                display_name="MEAC Description Content",
                                text_content="Our mission is to offer help and hope to our neighbors in crisis by meeting their basic needs and providing education that enables them to navigate their way out of poverty."))

    for item in content:
        db.session.add(item)

    db.session.commit()


def populate_HomePageFlags():
    HomePageFlags.query.delete()

    content = []

    content.append(
        HomePageFlags(field_name="emergency_closure_flag", flag_value=False, display_name="Emergency Closure Banner",
                      description="Activates the MEAC is closed for the day banner"))

    for item in content:
        db.session.add(item)

    db.session.commit()


def populate_AboutPageText():
    AboutPageText.query.delete()

    content = []

    content.append(AboutPageText(field_name="service_area_content",
                                 text_content="Our service area includes Hyde Park, Oakley, East End, Fairfax, Mariemont, and Madisonville.",
                                 display_name="Service Area Content", description="Caption for Service Area Map"))

    content.append(AboutPageText(field_name="mission_content",
                                 text_content="To offer help and hope to our neighbors in crisis by meeting their basic needs and providing education that enables them to navigate their way out of poverty.",
                                 display_name="Our Mission", description="Mission statement expanded"))

    content.append(AboutPageText(field_name="programs_content",
                                 text_content="For more than 30 years, MEAC has continued to provide vital services to assist individuals and families who reside in the Madisonville and surrounding communities.  MEAC's activities are centered on providing emergency assistance in the form of food, clothing, rent and utility assistance for our neighbours in need.  MEAC also provides programs to support self-sufficiency.  These programs include early childhood and adult literacy, financial/life coaching and job training, placement and retention through our partnership with Cincinnati Works.",
                                 display_name="What We Do",
                                 description="Paragraph describing programs offered at MEAC"))

    content.append(AboutPageText(field_name="history_content",
                                 text_content="Explore a time line of MEAC's history to better understand our roots and what we stand for.",
                                 display_name="Our History",
                                 description="Small text field describing History and linking to the respective page"))

    content.append(AboutPageText(field_name="supporters_content",
                                 text_content="Learn about those who graciously support MEAC and help us impact our community.",
                                 display_name="Supporters",
                                 description="Small text field describing Supporters and linking to the respective page"))

    content.append(AboutPageText(field_name="meet_the_team_content",
                                 text_content="Meet the staff, and other team members, who run the operations at MEAC.",
                                 display_name="Meet the Team",
                                 description="Small text field describing Meet the Team and linking to the respective page"))

    content.append(AboutPageText(field_name="contact_content",
                                 text_content="Find all contact information, including our address, phone numbers, fax, and email.",
                                 display_name="Contact",
                                 description="Small text field describing Contact and linking to the respective page"))

    for item in content:
        db.session.add(item)

    db.session.commit()


def populate_ContactPageText():
    ContactPageText.query.delete()

    content = []

    content.append(ContactPageText(field_name="address_content", text_content="4600 Erie Avenue, Cincinnati, OH 45227",
                                   display_name="Address Content", description="MEAC Address"))

    content.append(ContactPageText(field_name="staff_hours",
                                   text_content="MEAC Staff is available: Monday-Friday 9:00 AM - 5:00 PM",
                                   display_name="Staff Hours", description="Field to input staff hours of operation"))

    content.append(ContactPageText(field_name="emergency_hours",
                                   text_content="Emergency Financial Assistance: by appointment only",
                                   display_name="Emergency Assistance",
                                   description="Field to input emergency assistance hours of operation"))

    content.append(
        ContactPageText(field_name="community_hours", text_content="Monday Night Community Dinner: 5:00 PM - 6:30 PM",
                        display_name="Community Dinner",
                        description="Field to input community dinner hours of operation"))

    content.append(ContactPageText(field_name="marketplace_hours",
                                   text_content="MEAC Marketplace, including Choice Food Pantry: Tuesday & Thursday 9:30 AM - 3:00 PM",
                                   display_name="Marketplace Hours",
                                   description="Field to input marketplace hours of operation"))

    content.append(ContactPageText(field_name="main_office_phone_content", text_content="(513) 271-5501",
                                   display_name="Main Office Phone Content",
                                   description="Field for main office phone number"))

    content.append(ContactPageText(field_name="fax_number_content", text_content="(513) 271-4701",
                                   display_name="Fax Number Content", description="Field for office fax number"))

    for item in content:
        db.session.add(item)

    db.session.commit()


def populate_GetInvolvedPageText():
    GetInvolvedPageText.query.delete()

    content = []

    content.append(GetInvolvedPageText(field_name="get_involved_header_content",
                                       text_content="Everyday, with every donation and with every client, MEAC's mission is to change lives. There's no limit to what can be achieved and no reason to think small. For Madisonville and the surrounding areas, the only way is forward. Come with us.",
                                       display_name="Get Involved",
                                       description="Content for the header of the get involved page"))

    content.append(GetInvolvedPageText(field_name="financial_gifts_content",
                                       text_content="Giving information - plus other simple ways to financially support MEAC.",
                                       display_name="Financial Gifts",
                                       description="Content for the financial gifts explanation"))

    content.append(GetInvolvedPageText(field_name="donate_products_content",
                                       text_content="Find a list of products we need to stock the MEAC Marketplace.",
                                       display_name="Donate Products",
                                       description="Content that explains the list of products available"))

    content.append(GetInvolvedPageText(field_name="volunteer_content",
                                       text_content="Learn about tangible way you can serve those in your community.",
                                       display_name="Volunteer",
                                       description="Content that explains how to serve in the community"))

    content.append(GetInvolvedPageText(field_name="event_calendar_content",
                                       text_content="See what programs we have coming up and add them to your calendar.",
                                       display_name="Event Calendar", description="Content that explains the calendar"))

    content.append(GetInvolvedPageText(field_name="", text_content="", display_name="", description=""))

    for item in content:
        db.session.add(item)

    db.session.commit()


def populate_GetInvolvedVolunteerPageText():
    GetInvolvedVolunteerPageText.query.delete()

    content = []

    content.append(GetInvolvedVolunteerPageText(field_name="volunteer_contact",
                                                text_content="If you have questions about getting involved as a volunteer please contact Carolyn Moseley at (513) 271-5501 ext. 13 or carolyn.mosely@fuse.net.",
                                                display_name="Volunteer Contact Information",
                                                description="Content about how to get in touch for volunteering"))

    for item in content:
        db.session.add(item)

    db.session.commit()


def populate_OurImpactPageText():
    OurImpactPageText.query.delete()

    content = []

    content.append(OurImpactPageText(field_name="marketplace_impact_content",
                                     text_content="The MEAC Marketplace serves households in the MEAC community (zip codes:  45208, 45209, 45226, 45227) who meet the income guidelines.  MEAC provides emergency food assistance through our Choice Food Pantry which includes additional meat, bread and produce and donated clothing and household items which are new or gently used in our Clothing Shop.  All items are free with the amount available based on the size of the household. The MEAC Marketplace is open on Tuesdays and Thursdays from 9:30am to 3:00pm.",
                                     display_name="MEAC Marketplace", description="Who MEAC Serves"))

    content.append(OurImpactPageText(field_name="family_literacy_content",
                                     text_content="Each month during the school year MEAC hosts a Family Literacy Night at the John P. Parker Elementary School.  It is a fun family event with activities focusing on reading literacy.  Each event has a special theme and next month's theme is Science. Pizza and drinks are provided and the family is invited. Family Literacy Night: April 6 from 5:30 to 7:00 PM. Contact Erin Patterson at erin.patterson@fuse.net",
                                     display_name="Family Literacy Night", description="Explain Family Literacy Night"))

    content.append(OurImpactPageText(field_name="food_pantry_content", text_content="3,437", display_name="Food Pantry",
                                     description="Household served in Food Pantry"))

    content.append(
        OurImpactPageText(field_name="clothing_shop_content", text_content="Clothing Shop", display_name="3,212",
                          description="Households served in the Clothing Shop"))

    content.append(OurImpactPageText(field_name="literacy_program_content", text_content="342",
                                     display_name="Family Night Literacy Program",
                                     description="Attended our Family Night Literacy Program"))

    content.append(OurImpactPageText(field_name="summer_reading_camp_content", text_content="26",
                                     display_name="Summer Reading Camp Content",
                                     description="K-3rd grade children attended our Summer Reading Camp"))

    for item in content:
        db.session.add(item)

    db.session.commit()


def populate_GetHelpPageText():
    GetHelpPageText.query.delete()

    content = []

    content.append(GetHelpPageText(field_name="service_and_programs_content",
                                   text_content="Click the tabs below to explore the various services and programs we offer. Please note: an application is required for some services. For your convenience, and to expedite the application process, we've provided some of these documents here for you to fill out before visiting our office.",
                                   display_name="Services and Programs", description=""))

    content.append(GetHelpPageText(field_name="early_childhood_contact",
                                   text_content="For more information about Early Childhood Literacy contact Rachel Curry @ rachel.curry@fuse.net",
                                   display_name="Early Childhood Literacy Contact Information", description="Contact for early childhood literacy"))

    content.append(GetHelpPageText(field_name="enhance_your_life_contact",
                                   text_content="For more information about Enhance Your Life contact Tonia Griffin or Judy Gillens @ (513) 271-5501 ext 11",
                                   display_name="Enhance Your Life Contact Information", description="Contact for enhance your life"))

    content.append(GetHelpPageText(field_name="cincinnati_works_contact",
                                   text_content="For more information about Cincinnati Works contact Shauntel Dobbins @ (513) 271-5501 ext 20 ",
                                   display_name="Cincinnati Works Contact Information", description="Contact for Cincinnati Works"))

    content.append(GetHelpPageText(field_name="counseling_contact",
                                   text_content="For more information about Counseling contact Tonia Griffin or Judy Gillens @ (513) 271-5501 ext 11",
                                   display_name="Counseling Contact Information", description="Contact for counseling"))

    content.append(GetHelpPageText(field_name="",
                                   text_content="",
                                   display_name="", description=""))

    for item in content:
        db.session.add(item)

    db.session.commit()


def populate_GetHelpPageAssistanceTabListItem():
    GetHelpPageAssistanceTabListItem.query.delete()

    content = []

    content.append(GetHelpPageAssistanceTabListItem(field_name="marketplace", text_content="food, toiletries, cleaning products, clothing, and household items.", title_content="Marketplace"))

    content.append(GetHelpPageAssistanceTabListItem(field_name="financial_assistance", text_content="pay utility bills, rent, and mortgage, birth certificates, etc.", title_content="Financial Assistance"))

    content.append(GetHelpPageAssistanceTabListItem(field_name="ohio_benefit_bank", text_content="access public benefits (SNAP (food stamps), WIC, Medicaid, child care subsidies, federal & state income taxes, etc.)", title_content="The Ohio Benefit Bank"))

    content.append(GetHelpPageAssistanceTabListItem(field_name="referrals", text_content="to other organizations for services that MEAC does not provide.", title_content="Referrals"))

    for item in content:
        db.session.add(item)

    db.session.commit()




