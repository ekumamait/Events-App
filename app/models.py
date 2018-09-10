import psycopg2
 
class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='Ticket-Hub', host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def table(self):
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users(user_id SERIAL PRIMARY KEY, 
        first_name VARCHAR(100) NOT NULL, 
        age SMALLINT NOT NULL, last_name VARCHAR(100) NOT NULL, 
        user_email VARCHAR(120) NOT NULL, user_password VARCHAR(20) NOT NULL, date VARCHAR(100) NOT NULL) """
        self.cur.execute(create_user_table)
        self.conn.commit()

        create_events = """ CREATE TABLE IF NOT EXISTS Events(user_id SERIAL, 
        event_id SERIAL PRIMARY KEY, event_name VARCHAR(100) NOT NULL,
        event_location VARCHAR(20) NOT NULL, event_price VARCHAR(50) NOT NULL, 
        event_date VARCHAR(100) NOT NULL, FOREIGN KEY (user_id) REFERENCES Users (user_id)) """
        self.cur.execute(create_events)
        self.conn.commit()

        create_user_tickets = """ CREATE TABLE IF NOT EXISTS Tickets(user_id SERIAL PRIMARY KEY, 
        events_id SERIAL PRIMARY KEY, ticket_id SERIAL PRIMARY KEY, is_valid VARCHAR(100) NOT NULL, 
        verification_code VARCHAR(20) NOT NULL, FOREIGN KEY (event_id) REFERENCES Event (event_id), 
        FOREIGN KEY (user_id) REFERENCES Users (user_id)) """
        self.cur.execute(create_user_tickets)
        self.conn.commit()
        self.conn.close()

class Users():
    def __init__(self):
        self.conn = psycopg2.connect(dbname='my_diary', host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def insert_new_user(self, first_name, last_name, age, user_email, user_password, date):
        """A function to create a new user to the database"""
        create = """INSERT INTO Users(first_name, last_name, age, user_email, user_password, date) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');""".format(first_name, last_name, 
        age, user_email, user_password, date)
        self.cur.execute(create, (first_name, last_name, age, user_email, user_password, date))
        self.conn.commit()
        return True

    def get_user(self, User):
        if type(User) == int:
            create = """SELECT * FROM Users WHERE user_id='{0}'""".format(User)
        elif type(User) == type(''):
            create = """SELECT * FROM Users WHERE user_name='{0}'""".format(User)   
        self.cur.execute(create)
        User = self.cur.fetchall()
        return User 

    def get_all_user(self):
        create = """SELECT * FROM Users;"""
        self.cur.execute(create)
        return True 

class Events():
    def __init__(self):
        self.conn = psycopg2.connect(dbname='my_diary', host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def insert_new_event(self, user_id, is_valid, verification_code, date):
        create = """INSERT INTO Events(user_id, is_valid, verification_code, date) 
        VALUES ('{0}', '{1}', '{2}', '{3}')""".format(user_id, is_valid, verification_code, date)        
        self.cur.execute(create)
        self.conn.commit()
        return True 

    def get_event_by_id(self, event_id, user_id): 
        create = """SELECT * FROM Events WHERE event_id='{0}' AND user_id='{1}'""".format(event_id, user_id)
        self.cur.execute(create)
        events = self.cur.fetchall()      
        return events

    def get_all_events(self, user_id):
        create = """SELECT * FROM Events WHERE user_id='{}'""".format(user_id)
        self.cur.execute(create)
        events = self.cur.fetchall() 
        return events

class Tickets():
    def __init__(self):
        self.conn = psycopg2.connect(dbname='my_diary', host='localhost', user='postgres', password='incorrect')
        self.cur = self.conn.cursor()

    def insert_new_ticket(self, is_valid, verification_code, date, user_id, event_id):
        create = """INSERT INTO Tickets(is_valid, verification_code, date, user_id, event_id) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(is_valid, verification_code, date, user_id, event_id)        
        self.cur.execute(create)
        self.conn.commit()
        return True 

    def get_ticket_by_id(self, ticket_id, user_id): 
        create = """SELECT * FROM Tickets WHERE ticket_id='{0}' AND user_id='{1}'""".format(ticket_id, user_id)
        self.cur.execute(create)
        tickets = self.cur.fetchall()      
        return tickets

    def get_all_tickets(self, user_id):
        create = """SELECT * FROM Tickets WHERE user_id='{}'""".format(user_id)
        self.cur.execute(create)
        tickets = self.cur.fetchall() 
        return tickets
   
# import pdb;pdb.set_trace()