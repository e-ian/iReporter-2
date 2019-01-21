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
empty_comment = {
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
