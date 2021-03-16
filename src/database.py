#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sqlite3

class Database:
    def __init__(self, filename):
        self._filename = filename

    def execute(self, query):
        lastrowid = None
        try:
            con = sqlite3.connect(self._filename)
            cur = con.cursor()
            cur.execute(query)
            lastrowid = cur.lastrowid
            con.commit()
        except Exception as exception:
            print(exception)
        finally:
            if cur:
                cur.close()
            if con:
                con.close()
        return lastrowid

    def select(self, query):
        ans = []
        try:
            con = sqlite3.connect(self._filename)
            cur = con.cursor()
            cur.execute(query)
            ans = cur.fetchall()
        except Exception as exception:
            print(exception)
        finally:
            if cur:
                cur.close()
            if con:
                con.close()
        return ans

