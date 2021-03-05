import sqlite3
from sqlite3 import Error


class RecordsHandler:
    def __init__(self, db_file):
        self.sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Records (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        age text NOT NULL,
                                        origin text NOT NULL
                                    ); """

        self.create_connection(db_file)

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        self.create_table(self.sql_create_projects_table)

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def create_table(self, create_table_sql):
        """create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
            self.conn.commit()
        except Error as e:
            print(e)

    def add_record(self, name="", email="", age="", origin=""):
        sqlquery = "INSERT INTO Records (name, email, age, origin) VALUES ('%s', '%s', '%s', '%s')"
        val = (name, email, age, origin)
        query = sqlquery % val
        try:
            c = self.conn.cursor()
            c.execute(query)
            self.conn.commit()
        except Error as e:
            print(e)

    def delete_record(self, record_id=-1):
        sqlquery = "DELETE FROM Records WHERE id='%s'"
        val = record_id
        query = sqlquery % val
        try:
            c = self.conn.cursor()
            c.execute(query)
            self.conn.commit()
        except Error as e:
            print(e)

    def look(self, email="", age=""):
        sqlquery = "SELECT * FROM Records WHERE email='%s' AND age='%s'"
        val = (email, age)
        query = sqlquery % val

        results = []
        try:
            c = self.conn.cursor()
            c.execute(query)
            results.extend(c.fetchall())
        except Error as e:
            print(e)

        return results

    def list_all(self):
        query = "SELECT * FROM Records"
        results = []
        try:
            c = self.conn.cursor()
            c.execute(query)
            results.extend(c.fetchall())
        except Error as e:
            print(e)

        # loop through the rows
        for row in results:
            print(row)
    
    def delete_all(self):
        sqlquery = "DELETE FROM Records"
        try:
            c = self.conn.cursor()
            c.execute(sqlquery)
            self.conn.commit()
        except Error as e:
            print(e)
