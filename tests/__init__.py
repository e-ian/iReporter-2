from config import TestingConfig
from api.v1 import app

redflag = {
    'created_On': '2018-12-19',
    'created_By': 'emma',
    'incident_Type': 'redflag',
    'location': 'mulago',
    'status': 'draft',
    'images': 'images',
    'comment': 'bribery in OPM'
}
edit_comment = {
    'created_On': '2018-12-19',
    'created_By': 'ian',
    'incident_Type': 'redflag',
    'location': 'mulago',
    'status': 'draft',
    'images': 'images',
    'comment': 'bribery in OPM'
}
redflag_draft = {
    'created_On': '2018-12-19',
    'created_By': 'emma',
    'incident_Type': 'redflag',
    'location': 'mulago',
    'status': 'resolved',
    'images': 'images',
    'comment': 'bribery in OPM'
}
empty_incident_type = {
    'created_On': '2018-12-19',
    'created_By': 'emma',
    'incident_Type': '',
    'location': 'mulago',
    'status': 'resolved',
    'images': 'images',
    'comment': 'bribery in OPM'
}
empty_image = {
    'created_On': '2018-12-19',
    'created_By': 'emma',
    'incident_Type': 'redflag',
    'location': 'mulago',
    'status': 'resolved',
    'images': '',
    'comment': 'bribery in OPM'
}
redflag_comment = {
    'created_On': '2018-12-22',
    'created_By': 'solomon',
    'incident_Type': 'redflag',
    'location': 'kikoni',
    'status': 'resolved',
    'images': 'images',
    'comment': 'bribery in OPM'
}

redflagempty = {
    'created_On': '2018-12-19',
    'created_By': 'emma',
    'incident_Type': 'redflag',
    'location': '',
    'status': 'resolved',
    'images': 'images',
    'comment': 'bribery in OPM'
}

invalid_date = {
    "created_On": "december/2/2018",
    "created_By": "emma",
    "incident_Type": "redflag",
    "location": "kisasi",
    "status": "resolved",
    "images": "images",
    "comment": "bribery in OPM"
}
empty_list = {

}
