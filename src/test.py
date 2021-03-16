#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import unittest
import os
from dbcontact import DbContact

class TestDb(unittest.TestCase):
    def setUp(self):
        self._filename = 'test.db'
        if os.path.exists(self._filename):
            os.remove(self._filename)
        self._db = DbContact(self._filename)

    def tearDown(self):
        if os.path.exists(self._filename):
            os.remove(self._filename)

    def test_new(self):
        contact = self._db.new('lorenzo', 'lorenzo@atareao.es', '12345678')
        self.assertIsNotNone(contact)

    def test_search_by_name(self):
        name = 'Lorenzo'
        email = 'lorenzo@atareao.es'
        mobile = '12345678'
        contact = self._db.new(name, email, mobile)
        contacts = self._db.search_by_name(name)
        self.assertIs(len(contacts), 1)
        self.assertEqual(contacts[0].name, name)

    def test_search_by_email(self):
        name = 'Lorenzo'
        email = 'lorenzo@atareao.es'
        mobile = '12345678'
        contact = self._db.new(name, email, mobile)
        contacts = self._db.search_by_email(email)
        self.assertIs(len(contacts), 1)
        self.assertEqual(contacts[0].email, email)

    def test_search_by_mobile(self):
        name = 'Lorenzo'
        email = 'lorenzo@atareao.es'
        mobile = '12345678'
        contact = self._db.new(name, email, mobile)
        contacts = self._db.search_by_mobile(mobile)
        self.assertIs(len(contacts), 1)
        self.assertEqual(contacts[0].mobile, mobile)

    def test_exits(self):
        name = 'Lorenzo'
        email = 'lorenzo@atareao.es'
        mobile = '12345678'
        contact = self._db.new(name, email, mobile)
        exists = self._db.exists(contact)
        self.assertTrue(exists)

    def test_delete(self):
        name = 'Lorenzo'
        email = 'lorenzo@atareao.es'
        mobile = '12345678'
        contact = self._db.new(name, email, mobile)
        exists = self._db.exists(contact)
        self.assertTrue(exists)
        self._db.delete(contact.id)
        self.assertFalse(self._db.exists(contact))

if __name__ == '__main__':
    unittest.main()

