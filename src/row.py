#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import gi
try:
    gi.require_version('Gtk', '3.0')
except Exception as exception:
    print(exception)
    exit(1)
from gi.repository import Gtk
from contact import Contact

class Row(Gtk.ListBoxRow):

    def __init__(self, contact):
        Gtk.ListBoxRow.__init__(self)
        box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 5)
        self.add(box)

        self._contact = contact

        self._name = Gtk.Label()
        box.add(self._name)
        self._email = Gtk.Label()
        box.add(self._email)
        self._mobile = Gtk.Label()
        box.add(self._mobile)

        self.update()
        self.show_all()

    def update(self):
        self._name.set_text(self._contact.name)
        self._email.set_text(self._contact.email)
        self._mobile.set_text(self._contact.mobile)

    def get_contact(self):
        return self._contact

    def set_contact(self, contact):
        self._contact = contact
        self.update()
