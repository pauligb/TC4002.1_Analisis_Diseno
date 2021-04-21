import logging
import sqlite3
from sqlite3 import Error

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

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

        self.conn = sqlite3.connect(db_file)
        logging.info('Connection established to ' + db_file)

        self.create_table(self.sql_create_projects_table)

    def close_connection(self):
        if self.conn:
            self.conn.close()
            logging.info('Connection closed')

    def create_table(self, create_table_sql):
        """create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        c = self.conn.cursor()
        c.execute(create_table_sql)
        self.conn.commit()
        logging.info('Creating Records table')

    def add_record(self, name="", email="", age="", origin=""):
        sqlquery = "INSERT INTO Records (name, email, age, origin) VALUES ('%s', '%s', '%s', '%s')"
        val = (name, email, age, origin)
        query = sqlquery % val

        c = self.conn.cursor()
        c.execute(query)
        self.conn.commit()
        logging.info('New record added')

    def delete_record(self, record_id=-1):
        sqlquery = "DELETE FROM Records WHERE id='%s'"
        val = record_id
        query = sqlquery % val

        c = self.conn.cursor()
        c.execute(query)
        self.conn.commit()
        logging.info('Record with id ' + str(record_id) + ' deleted.')

    def look(self, email="", age=""):
        sqlquery = "SELECT * FROM Records WHERE email='%s' AND age='%s'"
        val = (email, age)
        query = sqlquery % val

        results = []

        c = self.conn.cursor()
        c.execute(query)
        results.extend(c.fetchall())

        return results

    def list_all(self):
        query = "SELECT * FROM Records"
        results = []

        c = self.conn.cursor()
        c.execute(query)
        results.extend(c.fetchall())

        # loop through the rows
        for row in results:
            print(row)

    def delete_all(self):
        sqlquery = "DELETE FROM Records"

        c = self.conn.cursor()
        c.execute(sqlquery)
        self.conn.commit()
