import sqlite3

conn = sqlite3.connect('employee.db')

cur = conn.cursor()

##query = 'create table employee (id integer primary key, first_name varchar(20),last_name varchar(20))'
##
##cur.execute(query)


##insert_query = 'insert into employee (id, first_name, last_name) values (?, ?, ?)'
##cur.execute(insert_query, (10, 'Ritik', 'Jain'))


## Delete the rows

#query = '''create table person (first_name varchar(20) not null, last_name varchar(20),
#id varchar(20) primary key, age integer not null, gender varchar(1) not null, phone integer(10) not null, address text)'''


##query = 'create table employee (email varchar(20) primary key, pwd varchar(20), name varchar(30))'

##cur.execute(query)

def insert_data(cur):

    insert_query = 'insert into employee (email, pwd, name) values (?, ?, ?)'

    name = input('Enter your name: ')

    email = input('Enter the email id: ')

    pwd = input('Enter the password: ')
    try:
        cur.execute(insert_query, (email, pwd, name))

        print ('You are allowed to login!')
    except sqlite3.OperationalError as e:
        print (e)

    except Exception as e:
        print (e)

    finally:

        conn.commit()
    

def update_pwd(cur):

    update = 'update employee set pwd = ? where email = ?'

    email = input('Enter the email id:')

    pwd = input('Enter the password: ')
    try:
        cur.execute(update, (pwd, email))

        print ('Your password has been updated!')
    except sqlite3.DatabaseError as e:

        print(e)
    except sqlite3.OperationalError as e:
        print(e)

    except Exception as e:
        print(e)

    finally:

        conn.commit()
        


def login(cur):

    select_query = 'select * from employee where email = ? and pwd = ?'

    email = input('Enter the email id: ')

    pwd = input('Enter the password: ')

    try:
        cur.execute(select_query, (email, pwd))

        data = cur.fetchall()

        if (len(data) > 0):

            print ('You have been successfully logged in!')

            print('Welcome' + data[0][2] + ' in the application!')
        else:
            print ('Sorry you are not an application User!')
    except sqlite3.OperationalError as e:
        print (e)

    except sqlite3.DatabaseError as e:
        print (e)
    except Exception as e:
        print(e)


query = 'delete from employee where email = ?'

