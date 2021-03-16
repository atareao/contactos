#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from contact import Contact
from database import Database

class DbContact:
    def __init__(self, filename):
        self._filename = filename
        self._db = Database(filename)
        sql = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            mobile TEXT)
        """
        self._db.execute(sql)

    def new(self, name, email, mobile):
        sql = 'INSERT INTO contacts (name, email, mobile) VALUES ("{}", "{}", "{}")'.format(name, email, mobile)
        id = self._db.execute(sql)
        return self.get(id)

    def get(self, id):
        sql = 'SELECT * FROM contacts WHERE id={}'.format(id)
        ans = self._db.select(sql)
        return Contact.toContact(*ans[0]) if len(ans) > 0 else None

    def delete(self, id):
        sql = 'DELETE FROM contacts WHERE id={}'.format(id)
        self._db.execute(sql)

    def search_by_mobile(self, mobile):
        result = []
        sql = 'SELECT * FROM contacts WHERE LOWER(mobile) like "%{}%"'.format(mobile.lower())
        for item in self._db.select(sql):
            result.append(Contact.toContact(*item))
        return result

    def search_by_email(self, email):
        result = []
        sql = 'SELECT * FROM contacts WHERE LOWER(email) like "%{}%"'.format(email.lower())
        for item in self._db.select(sql):
            result.append(Contact.toContact(*item))
        return result

    def search_by_name(self, name):
        result = []
        sql = 'SELECT * FROM contacts WHERE LOWER(name) like "%{}%"'.format(name.lower())
        for item in self._db.select(sql):
            result.append(Contact.toContact(*item))
        return result

    def exists(self, contact):
        sql = 'SELECT * FROM contacts WHERE LOWER(email) like "{}"'
        if isinstance(contact, Contact):
            email = contact.email.lower()
        else:
            email = contact.lower()
        return len(self._db.select(sql.format(email))) > 0

