from  config import TestingConfig
from api.v1 import app

redflag = {
        'createdOn' : '2018-12-19',
        'createdBy' : 'emma',
        'incidenttype' : 'redflag',
        'location' : 'mulago',
        'status' : 'resolved',
        'Images' : 'Images',
        'comment' :'bribery in OPM'
}

edit_comment ={'location' : 'kampala'}
redflagempty = {
    'createdOn' : '2018-12-19',
    'createdBy' : 'emma',
    'incidenttype' : 'redflag',
    'location' : '',
    'status' : 'resolved',
    'Images' : 'Images',
    'comment' :'bribery in OPM'
}

invalid_date = {
    'createdOn' : 'december/2/2018',
    'createdBy' : 'emma',
    'incidenttype' : 'redflag',
    'location' : 'kisasi',
    'status' : 'resolved',
    'Images' : 'Images',
    'comment' :'bribery in OPM'
}
empty_list = {

}