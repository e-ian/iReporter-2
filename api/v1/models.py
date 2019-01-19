""" Module database """
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class Database(object):
    """class to define databases for ireporter """
    def __init__(self):
        """ constructor method for connecting to the database """
        if os.getenv("Testingenv") == "EnvTests":
            dbname = "testingdb"
        else:
            dbname = "iReporterdb"
        self.conn = psycopg2.connect(dbname=dbname, user="postgres", host="localhost", password="ogwal123", port="5432")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.dict_cursor = self.conn.cursor(cursor_factory=RealDictCursor)

        print(dbname)

    def create_user_table(self):
        """ creates table for users in database """
        user_table = "CREATE TABLE IF NOT EXISTS users(user_id serial PRIMARY KEY, \
        firstname varchar(50), lastname varchar(50) username varchar(50), password varchar(256), \
        email varchar(30), role varchar(15))"

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