""" Module database """
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from config import app_config



class Database:
    """class to define databases for ireporter """

    def __init__(self):
        """ constructor method for connecting to the database """
        if os.getenv("Testingenv") == "EnvTests":
            dbname = "testingdb"
            user = "postgres"
            pwd = "alimanu"
            host = "localhost"
            port = "5432"

        elif app_config['production'] == 'production':
            dbname = "da51826nqt75f"
            user = "bmwdqpkfurzqev"
            pwd = "b4ee0a501e7c5132bc0b157a36436af9696f2cb1e4470d53503c2aefd953ee8f"
            host = "ec2-54-83-50-174.compute-1.amazonaws.com"
            port = "5432"
        elif app_config['development'] == 'development':
            dbname = "ireporterdb"
            user = "postgres",
            pwd = "alimanu",
            host = "localhost",
            port = "5432"
        # if os.getenv("Testingenv") == "EnvTests":
        #     dbname = "testingdb"
        # else:
        #     dbname = "ireporterdb"
            
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,            
            password=pwd,
            host=host,
            port=port)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        self.create_users_table()
        self.create_redflags_table()
        self.create_interventions_table()

        print("Connected to {}".format(dbname))

    def create_users_table(self):
        """ creates table for users in database """
        user_table = "CREATE TABLE IF NOT EXISTS users(user_id serial PRIMARY KEY, \
        firstname varchar(50), lastname varchar(50), username varchar(50), password varchar(256), \
        email varchar(30), role varchar(50))"

        self.cur.execute(user_table)

    def create_redflags_table(self):
        """ creates table for redflags in database """
        redflags_table = "CREATE TABLE IF NOT EXISTS redflags(redflag_id serial PRIMARY KEY, \
        created_on TIMESTAMP DEFAULT NOW(), created_by varchar(50), incident_type varchar(50), \
        location varchar(50), status varchar(20), image varchar(50), comment varchar(100))"

        self.cur.execute(redflags_table)

    def create_interventions_table(self):
        """creates table for interventions in database"""
        interventions_table = "CREATE TABLE IF NOT EXISTS interventions(intervention_id serial PRIMARY KEY, \
        created_on TIMESTAMP DEFAULT NOW(), created_by varchar(50), incident_type varchar(50), \
        location varchar(50), status varchar(20), image varchar(50), comment varchar(100))"

        self.cur.execute(interventions_table)
