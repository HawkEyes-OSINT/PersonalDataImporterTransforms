import sqlite3
import support
from unidecode import unidecode

"""
Retreive data from the database
Tables:
names, addresses, emails, passwords, phones, sm_urls, usernames
"""
def from_name(name):
    tables = {'addresses': [], 
              'emails': [],
              'usernames': [], 
              'passwords': [], 
              'phones': [], 
              'sm_urls': []}

    # format name
    name_ls = name.split(' ')
    if len(name_ls) < 2 or len(name_ls) > 3:
        return None
    else:
        name = ' '.join([value.strip() for value in name_ls])
        name = unidecode(name.title())

    # cursor prep
    conn = sqlite3.connect(support.db_path())
    cur = conn.cursor()
    
    # retrieve uid
    cur.execute(support.nameValue.format(name))
    uid_ls = cur.fetchall()

    # extract data
    for table in tables:
        for uid in uid_ls:
            cur.execute(support.queryID.format(table, uid[0]))
            res = cur.fetchall()
            tables[table] = tables[table] + res

    return tables

def from_email(email):
    tables = {'names': [],
              'addresses': [],
              'usernames': [], 
              'passwords': [], 
              'phones': [], 
              'sm_urls': []}

    # format email
    email = unidecode(email.strip().lower())

    # cursor prep
    conn = sqlite3.connect(support.db_path())
    cur = conn.cursor()
    
    # retrieve uid
    cur.execute(support.queryValue.format('emails', email))
    uid_ls = cur.fetchall()

    # extract data
    for table in tables:
        for uid in uid_ls:
            if table == 'names':
                cur.execute(support.nameID.format(uid[0]))
            else:
                cur.execute(support.queryID.format(table, uid[0]))
            res = cur.fetchall()
            tables[table] = tables[table] + res

    return tables

def from_phone(phone):
    tables = {'names': [],
              'addresses': [],
              'usernames': [], 
              'passwords': [], 
              'emails': [], 
              'sm_urls': []}

    # format phone
    phone = ''.join([char for char in phone if char.isdigit()])

    # cursor prep
    conn = sqlite3.connect(support.db_path())
    cur = conn.cursor()
    
    # retrieve uid
    cur.execute(support.queryValue.format('phones', phone))
    uid_ls = cur.fetchall()

    # extract data
    for table in tables:
        for uid in uid_ls:
            if table == 'names':
                cur.execute(support.nameID.format(uid[0]))
            else:
                cur.execute(support.queryID.format(table, uid[0]))
            res = cur.fetchall()
            tables[table] = tables[table] + res

    return tables

def from_url(url):
    tables = {'names': [],
              'addresses': [],
              'usernames': [], 
              'passwords': [], 
              'emails': [], 
              'phones': []}

    # cursor prep
    conn = sqlite3.connect(support.db_path())
    cur = conn.cursor()
    
    # retrieve uid
    cur.execute(support.queryValue.format('sm_urls', url))
    uid_ls = cur.fetchall()

    # extract data
    for table in tables:
        for uid in uid_ls:
            if table == 'names':
                cur.execute(support.nameID.format(uid[0]))
            else:
                cur.execute(support.queryID.format(table, uid[0]))
            res = cur.fetchall()
            tables[table] = tables[table] + res

    return tables

def from_username(username):
    tables = {'names': [],
              'addresses': [],
              'sm_urls': [], 
              'passwords': [], 
              'emails': [], 
              'phones': []}

    # cursor prep
    conn = sqlite3.connect(support.db_path())
    cur = conn.cursor()
    
    # retrieve uid
    cur.execute(support.queryValue.format('usernames', username))
    uid_ls = cur.fetchall()

    # extract data
    for table in tables:
        for uid in uid_ls:
            if table == 'names':
                cur.execute(support.nameID.format(uid[0]))
            else:
                cur.execute(support.queryID.format(table, uid[0]))
            res = cur.fetchall()
            tables[table] = tables[table] + res

    return tables

def from_password(password):
    tables = {'names': [],
              'addresses': [],
              'usernames': [], 
              'sm_urls': [], 
              'emails': [], 
              'phones': []}

    # cursor prep
    conn = sqlite3.connect(support.db_path())
    cur = conn.cursor()
    
    # retrieve uid
    cur.execute(support.queryValue.format('passwords', password))
    uid_ls = cur.fetchall()

    # extract data
    for table in tables:
        for uid in uid_ls:
            if table == 'names':
                cur.execute(support.nameID.format(uid[0]))
            else:
                cur.execute(support.queryID.format(table, uid[0]))
            res = cur.fetchall()
            tables[table] = tables[table] + res

    return tables

"""
Test Code
"""
# print(from_name('rachel booker'))
# print(from_email('rachel@example.com'))
# print(from_phone('5079'))
# print(from_url('Sales'))
# print(from_username('booker12'))
# print(from_password('9012'))
