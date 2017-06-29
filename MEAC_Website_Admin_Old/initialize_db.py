""" Initialize Database with Stock Elements """

from flask_prototype import db
db.drop_all()
db.create_all()

""" Import Models """
from flask_prototype import Page, Content, Files, Users, Admin, Flags, ListItem

# base_page = Page(name = 'base_page')
home_page = Page(name = 'home_page', display_name = 'Home')
about_page = Page(name = 'about_page', display_name = 'About')
contact_page = Page(name = 'contact_page', display_name = 'Contact')
get_help_page = Page(name = 'get_help_page', display_name = 'Get Help')
get_involved_page = Page(name = 'get_involved_page', display_name = 'Get Involved')
get_involved_financial_page = Page(name = 'get_involved_financial_page', display_name = 'Get Involved Financial')
get_involved_products_page = Page(name = 'get_involved_products_page', display_name = 'Marketplace Donations')
get_involved_volunteer_page = Page(name = 'get_involved_volunteer_page', display_name = 'Get Involved Volunteer')
history_page = Page(name = 'history_page', display_name = 'History')
impact_page = Page(name = 'impact_page', display_name = 'Impact')
meet_the_team_page = Page(name = 'meet_the_team_page', display_name = 'Meet The Team')
protected_content_page = Page(name = 'protected_content_page', display_name= 'Volunteer Portal')
supporters_page = Page(name = 'supporters_page', display_name = 'Supporters')

"""Home Page"""
#Content 
donate_content = Content(field='donate_content', display_name='Donate', text='Please help us continue to raise up one family at a time by taking a moment to donate.')
donate_content.set_description('Small text field describing the need to donate and how to contribute to MEAC.')

get_involved_content = Content(field='get_involved_content', display_name='Get Involved', text='We have a need for volunteer help and various product donations.')
get_involved_content.set_description('Text field describing volunteering and how to become involved at MEAC')

about_us_content = Content(field='about_us_content', display_name='About Us', text="We've been working to meet the needs of our community since 1986")
about_us_content.set_description('Short blurb about MEAC, and its mission')

get_help_content = Content(field='get_help_content', display_name='Get Help', text="Learn about the assistance we offer and access the forms you'll need to fill out to apply")
get_help_content.set_description('Small text field talking about MEACs ability to provide aid')

meac_description_content = Content(field='meac_description_content', display_name='MEAC Description Content', text='Since 1986, the Madisonville Education and Assistance Center has been providing direct aid and education to Cincinnati residents in crisis to help them navigate out of poverty.')
meac_description_content.set_description('Mission statement')

# #Files 
# united_way_image = Files(field='united_way_image', display_name='United Way Logo', file_path='../static/images/partners/UnitedWay_logo.png')
# united_way_image.set_visibility(True)
# cincy_works_image = Files(field='cincy_works_image', display_name='Cincinnati Works Logo', file_path="../static/images/partners/CincyWorks_logo.png")
# cincy_works_image.set_visibility(True)
# city_of_cincinnati_image = Files(field='city_of_cincinnati_image', display_name='City of Cincinnati Logo', file_path="../static/images/partners/CityOfCincinnati_logo.png")
# city_of_cincinnati_image.set_visibility(True)

#Flags
emergency_closure_flag = Flags(field='emergency_closure_flag', flag_value=False)

#Append Elements
home_page.content = [donate_content, get_involved_content, about_us_content, get_help_content, meac_description_content]
# home_page.files = [united_way_image, cincy_works_image, city_of_cincinnati_image]
home_page.flags = [emergency_closure_flag]
home_page.setContextEditor(True)
# home_page.setFileEditor(True)

"""About Page"""
#Content
service_area_content = Content(field='service_area_content', display_name='Service Area Content', text="Our service area includes Hyde Park, Oakley, East End, Fairfax, Mariemont, and Madisonville.")
service_area_content.set_description('Caption for Service Area Map')

mission_content = Content(field='mission_content', display_name='Our Mission', text='To offer help and hope to our neighbors in crisis by meeting their basic needs and providing education that enables them to navigate their way out of poverty.')
mission_content.set_description('Mission statement expanded')

programs_content = Content(field='programs_content', display_name='What We Do', text="For more than 30 years, MEAC has continued to provide vital services to assist individuals and families who reside in the Madisonville and surrounding communities.  MEAC's activities are centered on providing emergency assistance in the form of food, clothing, rent and utility assistance for our neighbours in need.  MEAC also provides programs to support self-sufficiency.  These programs include early childhood and adult literacy, financial/life coaching and job training, placement and retention through our partnership with Cincinnati Works.")
programs_content.set_description('Paragraph describing programs offered at MEAC')

history_content = Content(field='history_content', display_name='Our History', text="Explore a time line of MEAC's history to better understand our roots and what we stand for.")
history_content.set_description('Small text field describing History and linking to the respective page')

supporters_content = Content(field='supporters_content', display_name='Supporters', text='Learn about those who graciously support MEAC and help us impact our community.') 
supporters_content.set_description('Small text field describing Supporters and linking to the respective page')

meet_the_team_content = Content(field='meet_the_team_content', display_name='Meet the Team', text='Meet the staff, and other team members, who run the operations at MEAC.')
meet_the_team_content.set_description('Small text field describing Meet the Team and linking to the respective page')

contact_content = Content(field='contact_content', display_name='Contact', text='Find all contact information, including our address, phone numbers, fax, and email.')
contact_content.set_description('Small text field describing Contact and linking to the respective page')

#Files
# service_area_image = Files(field='service_area_image', display_name='Service Area Image', file_path='../static/images/MEAC Serving Area.png')
# service_area_image.set_visibility(True)

#Append Elements
about_page.content = [service_area_content, mission_content, programs_content, history_content, supporters_content, meet_the_team_content, contact_content]
# about_page.files = [service_area_image]
about_page.setContextEditor(True)
# about_page.setFileEditor(True)

"""Contact Page"""
#Content
address_content = Content(field='address_content', display_name='Address Content', text='4600 Erie Avenue, Cincinnati, OH 45227')
address_content.set_description('MEAC Address')

service_hours1 = Content(field='service_hours1', display_name='Staff Hours', text='MEAC Staff is available: Monday-Friday 9:00 AM - 5:00 PM')
service_hours1.set_description('service')

service_hours2 = Content(field='service_hours2', display_name='Emergency Assistance', text='Emergency Financial Assistance: by appointment only')
service_hours2.set_description('service')

service_hours3 = Content(field='service_hours3', display_name='Community Dinner', text='Monday Night Community Dinner: 5:00 PM - 6:30 PM')
service_hours3.set_description('service')

service_hours4 = Content(field='service_hours4', display_name='Marketplace Hours', text='MEAC Marketplace, including Choice Food Pantry: Tuesday & Thursday 9:30 AM - 3:00 PM')
service_hours4.set_description('service')

main_office_phone_content = Content(field='main_office_phone_content', display_name='Main Office Phone Content', text='(513) 271-5501')

fax_number_content= Content(field='fax_number_content', display_name='Fax Number Content', text='(513) 271-4701')

#Append Elements 
contact_page.content = [address_content, service_hours1, service_hours2, service_hours3, service_hours4, main_office_phone_content, fax_number_content]
contact_page.files = []
contact_page.setContextEditor(True)

"""Get Involved Page"""
#Content
get_involved_header_content = Content(field='get_involved_header_content', display_name='Get Involved', text="Everyday, with every donation and with every client, MEAC's mission is to change lives. There's no limit to what can be achieved and no reason to think small. For Madisonville and the surrounding areas, the only way is forward. Come with us.")

financial_gifts_content = Content(field="financial_gifts_content", display_name='Financial Gifts', text="Giving information - plus other simple ways to financially support MEAC.")

donate_products_content = Content(field='donate_products_content', display_name='Donate Products', text="Find a list of products we need to stock the MEAC Marketplace.")

volunteer_content = Content(field='volunteer_content', display_name='Volunteer', text="Learn about tangible way you can serve those in your community.")

event_calendar_content = Content(field='event_calendar_content', display_name='Event Calendar', text="See what programs we have coming up and add them to your calendar.")

#Append Elements
get_involved_page.content = [get_involved_header_content, financial_gifts_content, donate_products_content, volunteer_content, event_calendar_content]
get_involved_page.setContextEditor(True)

"""Get Involved Volunteer Page"""

#Content
volunteer_contact = Content(field='volunteer_contact', display_name='Volunteer Contact Information', text='If you have questions about getting involved as a volunteer please contact Carolyn Moseley at (513) 271-5501 ext. 13 or carolyn.mosely@fuse.net.')

#Files
job_descriptions_file = Files(field='job_descriptions_file', display_name='Volunteer Job Descriptions March 2017 with Openings', file_path="../static/documents/Volunteer Job Descriptions March 2017 with Openings.pdf")
job_descriptions_file.set_visibility(True)

volunteer_application_file = Files(field='volunteer_application_file', display_name='Volunteer Application Form', file_path="../static/documents/Volunteer Application Form 2017.pdf")
volunteer_application_file.set_visibility(True)

#Append Elements
get_involved_volunteer_page.content = [volunteer_contact]
get_involved_volunteer_page.files = [job_descriptions_file, volunteer_application_file]
get_involved_volunteer_page.setContextEditor(True)
get_involved_volunteer_page.setFileEditor(True)

"""Our Impact Page"""
#Content
marketplace_impact_content = Content(field='marketplace_impact_content', display_name='MEAC Marketplace', text='The MEAC Marketplace serves households in the MEAC community (zip codes:  45208, 45209, 45226, 45227) who meet the income guidelines.  MEAC provides emergency food assistance through our Choice Food Pantry which includes additional meat, bread and produce and donated clothing and household items which are new or gently used in our Clothing Shop.  All items are free with the amount available based on the size of the household. The MEAC Marketplace is open on Tuesdays and Thursdays from 9:30am to 3:00pm.')

family_literacy_content = Content(field='family_literacy_content', display_name='Family Literacy Night', text="Each month during the school year MEAC hosts a Family Literacy Night at the John P. Parker Elementary School.  It is a fun family event with activities focusing on reading literacy.  Each event has a special theme and next month's theme is Science. Pizza and drinks are provided and the family is invited. Family Literacy Night: April 6 from 5:30 to 7:00 PM. Contact Erin Patterson at erin.patterson@fuse.net")

food_pantry_content = Content(field='food_pantry_content', display_name='Food Pantry', text='3,437')
food_pantry_content.set_description('Household served in Food Pantry')
clothing_shop_content = Content(field='clothing_shop_content', display_name='Clothing Shop', text='3,212')
clothing_shop_content.set_description('Households served in the Clothing Shop')
literacy_program_content = Content(field='literacy_program_content', display_name='Family Night Literacy Program', text='342')
literacy_program_content.set_description('Attended our Family Night Literacy Program')
summer_reading_camp_content = Content(field='summer_reading_camp_content', display_name='Summer Reading Camp Content', text='26')
summer_reading_camp_content.set_description("K-3rd grade children attended our Summer Reading Camp")

#Append Elements
impact_page.content = [marketplace_impact_content, family_literacy_content, food_pantry_content, clothing_shop_content, literacy_program_content, summer_reading_camp_content]
impact_page.setContextEditor(True)

"""Get Help Page"""
#Content
service_and_programs_content = Content(field='service_and_programs_content', display_name='Services and Programs', text="Click the tabs below to explore the various services and programs we offer. Please note: an application is required for some services. For your convenience, and to expedite the application process, we've provided some of these documents here for you to fill out before visiting our office.")
contact_1 = Content(field='contact_1', display_name='Early Childhood Literacy Contact Information', text="For more information about Early Childhood Literacy contact Rachel Curry @ rachel.curry@fuse.net")
contact_2 = Content(field='contact_2', display_name='Enhance Your Life Contact Information', text="For more information about Enhance Your Life contact Tonia Griffin or Judy Gillens @ (513) 271-5501 ext 11")
contact_3 = Content(field='contact_3', display_name='Cincinnati Works Contact Information', text="For more information about Cincinnati Works contact Shauntel Dobbins @ (513) 271-5501 ext 20 ")
contact_4 = Content(field='contact_4', display_name='Counseling Contact Information', text="For more information about Counseling contact Tonia Griffin or Judy Gillens @ (513) 271-5501 ext 11")

#Assistance Tab
marketplace = ListItem(field='marketplace', text='food, toiletries, cleaning products, clothing, and household items.')
marketplace.set_description('assistance')
marketplace.set_title('Marketplace')

financial_assistance= ListItem(field='financial_assistance', text='pay utility bills, rent, and mortgage, birth certificates, etc.')
financial_assistance.set_description('assistance')
financial_assistance.set_title('Financial Assistance')

ohio_benefit_bank = ListItem(field='ohio_benefit_bank', text='access public benefits (SNAP (food stamps), WIC, Medicaid, child care subsidies, federal & state income taxes, etc.)')
ohio_benefit_bank.set_description('assistance')
ohio_benefit_bank.set_title('The Ohio Benefit Bank')

referrals = ListItem(field='referrals', text='to other organizations for services that MEAC does not provide.')
referrals.set_description('assistance')
referrals.set_title('Referrals')



#Programs Tab
child_literacy = ListItem(field='child_literacy', text='to help children (preschool through 3rd grade) who have reading deficiencies increase their reading abilities and confidence. Programs office at the John P. Parker Elementary School (Madisonville) and Summer Reading Camp at MEAC.')
child_literacy.set_description('programs')
child_literacy.set_title('Early Childhood Literacy')

adult_literacy = ListItem(field='adult_literacy', text='through our partnership with the LIteracy Network of Greater Cincinnati to teach literacy skills to adults who read at or below a 4th grade reading level.')
adult_literacy.set_description('programs')
adult_literacy.set_title('Adult Basic Reading')

enhance_life = ListItem(field='enhance_life', text='case management to provide support, information, resources, and other services to help prevent homelessness and increase income')
enhance_life.set_description('programs')
enhance_life.set_title('Enhance Your Life')

cincy_works = ListItem(field='cincy_works', text='employment training, placement, job retention for the unemployed and under-employeed.')
cincy_works.set_description('programs')
cincy_works.set_title('Cincinnati Works')

counseling = ListItem(field='counseling', text='individual counseling through the Mental Health of America Northern Kentucky and Southwest Ohio.')
counseling.set_description('programs')
counseling.set_title('Counseling')

#Events Tab
thanksgiving_basket = ListItem(field='thanksgiving_basket', text='food boxes and turkeys given out the Sunday before Thanksgiving.')
thanksgiving_basket.set_description('events')
thanksgiving_basket.set_title('Thanksgiving Basket')

monday_community_dinners = ListItem(field='monday_community_dinners', text='served weekly, excluding certain holidays (check out our Event Calendar), and provided by host groups/churches open to the community. Bingo and raffle prizes are often provided.')
monday_community_dinners.set_description('events')
monday_community_dinners.set_title('Monday Community Dinners')

swim_program = ListItem(field='swim_program', text='Cincinnati Recreation Center passes and swim apparel provided to household members.')
swim_program.set_description('events')
swim_program.set_title('Swim Program')

summer_literacy_camp = ListItem(field='summer_literacy_camp', text='Kindergarten through 2nd grade focused on increasing skills and confidence in the summer; 3 days/week for 4 weeks.')
summer_literacy_camp.set_description('events')
summer_literacy_camp.set_title('Summer Literacy Camp')

school_backpack = ListItem(field='school_backpack', text='back packs with school supplies provided for students through 12th grade.')
school_backpack.set_description('events')
school_backpack.set_title('School Back Packs')

holiday_shop = ListItem(field='holiday_shop', text='holiday shopping experience for clients who wish to have gifts for their household members around the Christmas season.')
holiday_shop.set_description('events')
holiday_shop.set_title('Happy Holiday Shop (Christmas)')

#Files 
informational_client_brochure_file = Files(field='informational_client_brochure_file', display_name='Informational Client Brochure', file_path='../static/documents/Informational Client Brochure.pdf')
informational_client_brochure_file.set_visibility(True)

benefit_bank_flyer_file = Files(field='benefit_bank_flyer_file', display_name='The Benefit Bank Flyer', file_path="../static/documents/The Benefit Bank.pdf")
benefit_bank_flyer_file.set_visibility(True)
benefit_bank_flyer_file.set_description('The Ohio Benefit Bank')

enhance_life_file = Files(field='enhance_life_file', display_name='Enhance Your Life Flyer', file_path='../static/documents/Enhance Your Life.pdf')
enhance_life_file.set_visibility(True)
enhance_life_file.set_description('Enhance Your Life')

cincy_works_file = Files(field='cincy_works_file', display_name='Cincinnati Works Flyer', file_path='../static/documents/Cincinnati Works.pdf')
cincy_works_file.set_visibility(True)
cincy_works_file.set_description('Cincinnati Works')

#Append Elements
get_help_page.content = [service_and_programs_content, contact_1, contact_2, contact_3, contact_4]
get_help_page.listitems = [marketplace, financial_assistance, ohio_benefit_bank, referrals, child_literacy, adult_literacy, enhance_life, cincy_works, counseling, thanksgiving_basket, monday_community_dinners, swim_program, summer_literacy_camp, school_backpack, holiday_shop]
get_help_page.files = [informational_client_brochure_file, benefit_bank_flyer_file, enhance_life_file, cincy_works_file]
get_help_page.setContextEditor(True)
get_help_page.setFileEditor(True)
get_help_page.setAddDeleteEditor(True)

"""Supporters Page"""
#Content

#Churches
d1 = ListItem(field='d1', text='Armstrong Chapel United Methodist Church')
d1.set_description('churches')
d2 = ListItem(field='d2', text='Center for Spiritual Living of Greater Cincinnati')
d2.set_description('churches')
d3 = ListItem(field='d3', text='Church of the Redeemer - Hyde Park')
d3.set_description('churches')
d4 = ListItem(field='d4', text='Cincinnati Bible Way Church')
d4.set_description('churches')
d5 = ListItem(field='d5', text='Eastminster Presbyterian Church')
d5.set_description('churches')
d6 = ListItem(field='d6', text='Gains United Methodist Church')
d6.set_description('churches')
d7 = ListItem(field='d7', text='Greater Harvest Missionary Baptist Church')
d7.set_description('churches')
d8 = ListItem(field='d8', text='Greater Liberty Baptist Church')
d8.set_description('churches')
d9 = ListItem(field='d9', text='Hyde Park Community United Methodist Church')
d9.set_description('churches')
d10 = ListItem(field='d10', text='Indian Hill Episcopal-Presbyterian Church')
d10.set_description('churches')
d11 = ListItem(field='d11', text='Knox Presbyterian Church')
d11.set_description('churches')
d12 = ListItem(field='d12', text='Korean-Madisonville United Methodist Church')
d12.set_description('churches')
d13 = ListItem(field='d13', text='Madisonville Church of God')
d13.set_description('churches')
d14 = ListItem(field='d14', text='Mariemont Church')
d14.set_description('churches')
d15 = ListItem(field='d15', text='New Mission Missionary Baptist Church')
d15.set_description('churches')
d16 = ListItem(field='d16', text='St. Anthony Catholic Church - Madisonville')
d16.set_description('churches')
d17 = ListItem(field='d17', text='St. Mary Church - Hyde Park')
d17.set_description('churches')
d18 = ListItem(field='d18', text='St. Paul Lutheran Church - Madisonville')
d18.set_description('churches')
d19 = ListItem(field='d19', text='St. Paul United Methodist Church - Madeira')
d19.set_description('churches')

#Organizations 
e1 = ListItem(field='e1', text='Bed, Bath, and Beyond')
e1.set_description('organizations')
e2 = ListItem(field='e2', text='Bob Evans Restaurants')
e2.set_description('organizations')
e3 = ListItem(field='e3', text='The Capital Grille')
e3.set_description('organizations')
e4 = ListItem(field='e4', text='CBRE Commercial Real-Estate')
e4.set_description('organizations')
e5 = ListItem(field='e5', text='Fresh Thyme Market - Oakley')
e5.set_description('organizations')
e6 = ListItem(field='e6', text='Fifth Third Bank')
e6.set_description('organizations')
e7 = ListItem(field='e7', text='Kroger - Madeira')
e7.set_description('organizations')
e8 = ListItem(field='e8', text='LOTH, Inc.')
e8.set_description('organizations')
e9 = ListItem(field='e9', text='Olive Garden Restaurants - Oakley')
e9.set_description('organizations')
e10 = ListItem(field='e10', text='Pizza Hut')
e10.set_description('organizations')
e11 = ListItem(field='e11', text='PNC Bank')
e11.set_description('organizations')
e12 = ListItem(field='e12', text='Scripps Howard Foundation')
e12.set_description('organizations')
e13 = ListItem(field='e13', text='Seasons 52')
e13.set_description('organizations')
e14 = ListItem(field='e14', text='Starbucks')
e14.set_description('organizations')
e15 = ListItem(field='e15', text='Target - Oakley')
e15.set_description('organizations')
e16 = ListItem(field='e16', text='Wimberg Landscaping')
e16.set_description('organizations')

#Append Elements
supporters_page.listitems = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16]

supporters_page.setAddDeleteEditor(True)


"""Get Involved Products Page"""
#Content
a1 = ListItem(field='a1', text='Cereal')
a1.set_description('marketplace')
a2 = ListItem(field='a2', text='Canned Fruit')
a2.set_description('marketplace')
a3 = ListItem(field='a3', text='Canned Tuna')
a3.set_description('marketplace')
a4 = ListItem(field='a4', text='Canned Salmon')
a4.set_description('marketplace')
a5 = ListItem(field='a5', text='Canned Chicken')
a5.set_description('marketplace')
a6 = ListItem(field='a6', text='Spam')
a6.set_description('marketplace')
a7 = ListItem(field='a7', text='Canned or Powdered Milk')
a7.set_description('marketplace')
a8 = ListItem(field='a8', text='Deodorant')
a8.set_description('marketplace')
a9 = ListItem(field='a9', text='Shampoo')
a9.set_description('marketplace')
a10 = ListItem(field='a10', text='Body Soap')
a10.set_description('marketplace')
a11 = ListItem(field='a11', text='Feminine Hygiene Products')
a11.set_description('marketplace')
a12 = ListItem(field='a12', text='Razors')
a12.set_description('marketplace')
a13 = ListItem(field='a13', text='Toilet Paper')
a13.set_description('marketplace')
a14 = ListItem(field='a14', text='Paper Towels')
a14.set_description('marketplace')
a15 = ListItem(field='a15', text='Facial Tissue')
a15.set_description('marketplace')
a16 = ListItem(field='a16', text='Laundry Detergent')
a16.set_description('marketplace')
a17 = ListItem(field='a17', text='Dish Detergent')
a17.set_description('marketplace')

b1 = ListItem(field='b1', text='Clothing (All sizes/sexes)')
b1.set_description('clothing')
b2 = ListItem(field='b2', text='Underwear (All sizes)')
b2.set_description('clothing')
b3 = ListItem(field='b3', text='Socks (All sizes)')
b3.set_description('clothing')

c1 = ListItem(field='c1', text='Curtains')
c1.set_description('misc')
c2 = ListItem(field='c2', text='Bedding')
c2.set_description('misc')
c3 = ListItem(field='c3', text='Small Appliances')
c3.set_description('misc')
c4 = ListItem(field='c4', text='Plastic and Paper bags')
c4.set_description('misc')

#Append Elements
get_involved_products_page.listitems = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, b1, b2, b3, c1, c2, c3, c4]

get_involved_products_page.setAddDeleteEditor(True)

"""Protected Content Page"""
#Files
volunteer_directory_file = Files(field='volunteer_directory_file', display_name='Volunteer Directory File', file_path="..\static\documents\Volunteer Job Descriptions March 2017 with Openings.pdf")
volunteer_directory_file.set_visibility(True)
volunteer_image = Files(field='volunteer_image', display_name='Volunteer Image', file_path='../static/images/volunteer.png')
volunteer_image.set_visibility(True)

#Append Elements
protected_content_page.files = [volunteer_directory_file, volunteer_image]
protected_content_page.setFileEditor(True)
protected_content_page.setAddDeleteFile(True)

"""Meet the Team Page"""
#Admins
office_assistant_user = Users(field='office_assistant_user', display_name='Evelyn Bostic')
office_assistant_user.set_phone_number('(513) 271-5501 ext.10')
office_assistant_user.set_email('evelyn.bostic1@fuse.net')
office_assistant_user.set_description('Role: Office Assistent')
office_assistant_user.set_visibility(True)
office_assistant_user.set_file_path('../static/images/team/evelyn_bostic.jpg')

social_services_coordinator_user = Users(field='social_services_coordinator_user', display_name='Tonia Griffin')
social_services_coordinator_user.set_phone_number('(513) 271-5501 ext. 11')
social_services_coordinator_user.set_email('tonia.griffin@fuse.net')
social_services_coordinator_user.set_description('Role: Social Services Coordinator (Licensed Social Worker)')
social_services_coordinator_user.set_visibility(True)
social_services_coordinator_user.set_file_path('../static/images/team/tonia_griffin.jpg')

executive_director_user = Users(field='executive_director_user', display_name='Doug Bierer') 
executive_director_user.set_phone_number('(513) 271-5501 ext. 12')
executive_director_user.set_email('dbc@fuse.net')
executive_director_user.set_description('Role: Executive Director')
executive_director_user.set_visibility(True)
executive_director_user.set_file_path('../static/images/team/doug_bierer.jpg')

operations_manager_user = Users(field='operations_manager_user', display_name='Carolyn Moseley')
operations_manager_user.set_phone_number('(513) 271-5501 ext. 13')
operations_manager_user.set_email('carolyn.moseley@fuse.net')
operations_manager_user.set_description('Role: Operations Manager & Volunteer Coordinator')
operations_manager_user.set_visibility(True)
operations_manager_user.set_file_path('../static/images/team/carolyn_moseley.jpg')

emergency_assistance_programs_manager_user = Users(field="emergency_assistance_programs_manager_user", display_name='Sean Cornforth')
emergency_assistance_programs_manager_user.set_phone_number("(513) 271-5501 ext. 16")
emergency_assistance_programs_manager_user.set_email('sean.cornforth@fuse.net')
emergency_assistance_programs_manager_user.set_description("Role: Emergency Assistance Programs Manager")
emergency_assistance_programs_manager_user.set_visibility(True)
emergency_assistance_programs_manager_user.set_file_path("../static/images/team/sean_cornforth.jpg")

financial_assistance_coordinator_user = Users(field="financial_assistance_coordinator_user", display_name='Judy Gillens')
financial_assistance_coordinator_user.set_phone_number(None)
financial_assistance_coordinator_user.set_email('judy.gillens@fuse.net')
financial_assistance_coordinator_user.set_description("Role: Financial Assistance Coordinator")
financial_assistance_coordinator_user.set_visibility(True)
financial_assistance_coordinator_user.set_file_path("../static/images/team/judy_gillens.jpg")

adult_literacy_program_coordinator_user = Users(field="adult_literacy_program_coordinator_user", display_name='Erin Patterson')
adult_literacy_program_coordinator_user.set_phone_number(None)
adult_literacy_program_coordinator_user.set_email("erin.patterson@fuse.net")
adult_literacy_program_coordinator_user.set_description("Role: Adult Literacy Program Coordinator")
adult_literacy_program_coordinator_user.set_visibility(True)
adult_literacy_program_coordinator_user.set_file_path("../static/images/team/erin_patterson.jpg")

child_literacy_program_coordinator_user = Users(field="child_literacy_program_coordinator_user", display_name='Rachel Curry')
child_literacy_program_coordinator_user.set_phone_number(None)
child_literacy_program_coordinator_user.set_email("rachel.curry@fuse.net")
child_literacy_program_coordinator_user.set_description("Role: Child Literacy Program Coordinator")
child_literacy_program_coordinator_user.set_visibility(True)
child_literacy_program_coordinator_user.set_file_path("../static/images/team/rachel_curry.jpg")

#Append Elements
meet_the_team_page.users = [executive_director_user, operations_manager_user, emergency_assistance_programs_manager_user, social_services_coordinator_user, financial_assistance_coordinator_user, office_assistant_user, adult_literacy_program_coordinator_user, child_literacy_program_coordinator_user]
meet_the_team_page.files = []
meet_the_team_page.setUserEditor(True)

"""History Page"""
#Content

timeline1 = Content(field='timeline1', display_name='Our Beginning', text='MEAC began in 1986 as a collaboration between twelve community churches along with the Madisonville Community Council to consolidate community resources to better serve our neighbors.')
timeline1.set_description('1986')
timeline1.set_title('Origin Story')
timeline2 = Content(field='timeline2', display_name='Expanded Service Area', text='MEAC expanded service to several of our neighboring communities to include the 45226, 45208, and 45209 zip codes - the Oakley, East End, and Hyde park areas.')
timeline2.set_description('2003')
timeline2.set_title('Making a Larger Mark')
timeline3 = Content(field='timeline3', display_name='Partnership', text='With help from the Ohio Benefit Bank, MEAC was able to expand services to assist clients with filling out applications for public benefits including food stamps and other state and federal programs.')
timeline3.set_description('2007')
timeline3.set_title('Finding Partners')
timeline4 = Content(field='timeline4', display_name='Preschool Literacy Program', text='We began offering a preschool literacy program for children ages 3-5')
timeline4.set_description('2009')
timeline4.set_title('Expanding Education')
timeline5 = Content(field='timeline5', display_name='Childhood Literacy', text="MEAC's Early Literacy Program was established at Madisonville's John P. Parker School for students in Pre-Kindergarten to 3rd grade.  This program exposes children who are not reading at their grade level to a variety of instructional techniques that will raise their reading accuracy, increase their reading comprehension and promote a lifetime love of reading.")
timeline5.set_description('2010')
timeline5.set_title('Increasing our Impact')
timeline6 = Content(field='timeline6', display_name='Expanding Programs', text='MEAC along with the support of Eastminster Presbyterian Church completes a major renovation project in the church building.  This renovation doubles the space of the MEAC Marketplace (formerly Food Pantry and Boutique), adds a much needed elevator to help with operations and service our clients who need this service and adds space for offices of MEAC staff.')
timeline6.set_description('2015')
timeline6.set_title('Facility Renovation')

#Append Elements 
history_page.content = [timeline1, timeline2, timeline3, timeline4, timeline5, timeline6]
history_page.setContextEditor(True)
history_page.setHistoryEditor(True)

"""Create Admin Users"""
admin_1 = Admin(field='admin_1', username='meac_admin', password='s${?~anV!6&B!L+7')
db.session.add(admin_1)
admin_1.hash_password(admin_1.password)
volunteer_1 = Admin(field='volunteer_1', username='meac_volunteer', password='4600MC*Volunteer')
db.session.add(volunteer_1)
volunteer_1.hash_password(volunteer_1.password)


""" Add and Commit => Last Task """
#Add and Commit the Pages
db.session.add_all([home_page, about_page, contact_page, get_help_page, get_involved_page, get_involved_financial_page, get_involved_products_page, get_involved_volunteer_page, history_page, impact_page, meet_the_team_page, protected_content_page, supporters_page])
db.session.commit()
