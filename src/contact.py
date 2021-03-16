#!/usr/bin/env python3
#-*- coding: utf-8 -*-


class Contact:
    def __init__(self):
        self._id = None
        self._name = None
        self._email = None
        self._mobile = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email.lower()

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        self._mobile = mobile

    @classmethod
    def new(self, name, email, mobile):
        contact = Contact()
        contact.id = None
        contact.name = name
        contact.email = email
        contact.mobile = mobile
        return contact

    @classmethod
    def toContact(self, id, name, email, mobile):
        contact = Contact()
        contact.id = id
        contact.name = name
        contact.email = email
        contact.mobile = mobile
        return contact

    def __str__(self):
        return "Id: {}\nName: {}\nEmail: {}\nMobile: {}".format(
            self.id, self.name, self.email, self.mobile)

    def __eq__(self, other):
        if isinstance(other, Contact):
            return self.email == other.email
        return False
