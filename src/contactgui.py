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
        self.show_all()



if __name__ == '__main__':
    cd = ContactDialog(Crud.READ)
    cd.run()