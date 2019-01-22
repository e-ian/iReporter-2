from config import TestingConfig
from api.v1 import app

""" Dummy data for redflags """
redflag = {
    "created_by": "emmanuel",
    "incident_type": "redflag",
    "location": "kikoni",
    "status": "draft",
    "image": "vbdjhdhjs",
    "comment": "bribery in OPM"
}
invalid_redflag = {
    "created_by": "emmanuel",
    "incident_type": "redflag",
    "status": "draft",
    "image": "vbdjhdhjs",
    "comment": "bribery in OPM"
}
edit_redflag_location = {"location": "apac"}

edit_redflag_location_not_found = {  
    "location": "lira"   
}
edit_invalid_redflag_location = {  
    "locatio": "lira"
}
edit_redflag_comment = {  
    "comment": "bribery"   
}
edit_redflag_comment_not_found = {  
    "comment": "bribery"   
}
edit_invalid_redflag_comment = {  
    "comme": "bribery"   
}
edit_redflag_status = {  
    "status": "resolved"   
}
edit_redflag_status_not_found = {  
    "status": "resolved"   
}
edit_invalid_redflag_status = {  
    "stat": "resolved"   
}

empty_incident_type = {
    "created_by": "emmanuel",
    "incident_type": "",
    "location": "kikoni",
    "status": "draft",
    "image": "vbdjhdhjs",
    "comment": "bribery in OPM"
}
empty_image = {
    "created_by": "emmanuel",
    "incident_type": "redflag",
    "location": "kikoni",
    "status": "draft",
    "image": "",
    "comment": "bribery in OPM"
}
empty_comment = {
    "created_by": "emmanuel",
    "incident_type": "redflag",
    "location": "kikoni",
    "status": "draft",
    "image": "vbdjhdhjs",
    "comment": ""
}

""" dummy data for interventions """
intervention = {
    "created_by": "emmanuel",
    "incident_type": "intervention",
    "location": "kikoni",
    "status": "draft",
    "image": "vbdjhdhjs",
    "comment": "bribery in OPM"
}
invalid_intervention = {
    "created_by": "emmanuel",
    "incident_type": "intervention",
    "status": "draft",
    "image": "vbdjhdhjs",
    "comment": "bribery in OPM"
}
empty_comment_int = {
    "created_by": "emmanuel",
    "incident_type": "intervention",
    "location": "kikoni",
    "status": "draft",
    "image": "vbdjhdhjs",
    "comment": ""
}
empty_image_int = {
    "created_by": "emmanuel",
    "incident_type": "intervention",
    "location": "kikoni",
    "status": "draft",
    "image": "",
    "comment": "bribery in OPM"
}
edit_int_location = {"location": "gulu"}

edit_invalid_int_location = {  
    "locatio": "gulu"
}
edit_int_comment = {  
    "comment": "nepotism"   
}

edit_invalid_int_comment = {  
    "comme": "bribery"   
}
edit_int_status = {  
    "status": "resolved"   
}

edit_invalid_int_status = { 
    "stat": "resolved"   
}

"""dummy data for testing users"""
login_admin ={
    "username": "ogwalian",
    "password": "ogwal123"
}
create_admin ={
"firstname": "emmanuel",
"lastname": "ogwal",
"username": "ogwalian",
"password": "ogwal123",
"email": "ogwal@gmail.com",
"role": "admin"
}
create_user ={
"firstname": "emmanuel",
"lastname": "ogwal",
"username": "emma",
"password": "emma123",
"email": "ogwal@gmail.com",
"role": "user"
}
login_user ={
    "username": "emma",
    "password": "emma123"}
invalid_username ={
"firstname": "emmanuel",
"lastname": "ogwal",
"username": "123",
"password": "emmal123",
"email": "ogwal@gmail.com",
"role": "user"
}
invalid_firstname ={
"firstname": "3223",
"lastname": "ogwal",
"username": "emma",
"password": "emmal123",
"email": "ogwal@gmail.com",
"role": "user"
}
invalid_lastname ={
"firstname": "emmanuel",
"lastname": "3344",
"username": "emma",
"password": "emmal123",
"email": "ogwal@gmail.com",
"role": "user"
}
invalid_role ={
"firstname": "emmanuel",
"lastname": "ogwal",
"username": "emma",
"password": "emmal123",
"email": "ogwal@gmail.com",
"role": "@kk22"
}
invalid_password ={
"firstname": "emmanuel",
"lastname": "ogwal",
"username": "emma",
"password": "emmal123",
"email": "ogwal@gmail.com",
"role": "user"
}
invalid_email ={
"firstname": "emmanuel",
"lastname": "ogwal",
"username": "emma",
"password": "123",
"email": "ogwalgmail.com",
"role": "user"
}

