#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import gi
try:
    gi.require_version("Gtk", "3.0")
except Exception as exception:
    print(exception)
    exit(1)
from gi.repository import Gtk

from enum import Enum
from contact import Contact


class Crud(Enum):
    CREATE = 0
    READ = 1
    UPDATE = 2
    DELETE = 3


class ContactDialog(Gtk.Dialog):
    def __init__(self, crud, contact=None):
        Gtk.Dialog.__init__(self)
        if crud == Crud.CREATE:
            title = "Add"
            self._crud = crud
        elif crud == Crud.DELETE:
            title = "Delete"
            self._crud = crud
        elif crud == Crud.UPDATE:
            title = "Edit"
            self._crud = crud
        else:
            title = "Show"
            self._crud = Crud.READ
        self.add_button("Ok", Gtk.ResponseType.OK)
        self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        grid = Gtk.Grid()
        grid.set_row_homogeneous(True)
        grid.set_row_spacing(10)
        grid.set_column_spacing(10)
        grid.set_margin_start(10)
        grid.set_margin_end(10)
        grid.set_margin_top(10)
        grid.set_margin_bottom(10)
        self.get_content_area().add(grid)
        grid.attach(Gtk.Label.new("Name:"), 0, 0, 1, 1)
        self._name = Gtk.Entry()
        grid.attach(self._name, 1, 0, 1, 1)
        grid.attach(Gtk.Label.new("Email:"), 0, 1, 1, 1)
        self._email = Gtk.Entry()
        grid.attach(self._email, 1, 1, 1, 1)
        grid.attach(Gtk.Label.new("Mobile:"), 0, 2, 1, 1)
        self._mobile = Gtk.Entry()
        grid.attach(self._mobile, 1, 2, 1, 1)

        if contact:
            self._name.set_text(contact._name)
            self._email.set_text(contact._email)
            self._mobile.set_text(contact._mobile)
            self._contact = contact
        else:
            self._contact = None
        self.show_all()

    def get_contact(self):
        if self._contact:
            self._contact._name = self._name.get_text()
            self._contact._email = self._email.get_text()
            self._contact._mobile = self._mobile.get_text()
        else:
            self._contact = Contact.new(self._name.get_text(),
                                        self._email.get_text(),
                                        self._mobile.get_text())
        return self._contact


if __name__ == '__main__':
    cd = ContactDialog(Crud.READ)
    cd.run()
