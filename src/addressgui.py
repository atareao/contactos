#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import gi
try:
    gi.require_version("Gtk", "3.0")
except Exception as exception:
    print(exception)
    exit(1)
from gi.repository import Gtk
from contactgui import ContactDialog, Crud
from row import Row
from dbcontact import DbContact


class AddressDialog(Gtk.Dialog):

    def __init__(self):
        Gtk.Dialog.__init__(self)
        self.add_button("Ok", Gtk.ResponseType.OK)
        self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        grid = Gtk.Grid()
        self.get_content_area().add(grid)
        grid.set_row_homogeneous(True)
        grid.set_row_spacing(10)
        grid.set_column_spacing(10)
        grid.set_margin_start(10)
        grid.set_margin_end(10)
        grid.set_margin_top(10)
        grid.set_margin_bottom(10)
        self._search = Gtk.Entry()
        grid.attach(self._search, 0, 0, 4, 1)
        button_search = Gtk.Button.new_with_label('Search')
        grid.attach(button_search, 5, 0, 1, 1)
        scrolled_window = Gtk.ScrolledWindow()
        grid.attach(scrolled_window, 0, 1, 4, 4)
        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 5)
        grid.attach(box, 5, 1, 1, 4)
        button_add = Gtk.Button.new_with_label('Add')
        button_add.connect('clicked', self.add)
        box.add(button_add)
        button_edit = Gtk.Button.new_with_label('Edit')
        button_edit.connect('clicked', self.edit)
        box.add(button_edit)
        button_delete = Gtk.Button.new_with_label('Delete')
        button_delete.connect('clicked', self.delete)
        box.add(button_delete)
        button_show = Gtk.Button.new_with_label('Show')
        button_show.connect('clicked', self.show)
        box.add(button_show)

        self._list = Gtk.ListBox()
        scrolled_window.add(self._list)
        
        self.load()

        self.show_all()

    def show(self, widget):
        selected_row = self._list.get_selected_row()
        if selected_row:
            contact = selected_row.get_contact()
            cd = ContactDialog(Crud.READ, contact)
            cd.run()
            cd.destroy()

    def add(self, widget):
        cd = ContactDialog(Crud.CREATE)
        if cd.run() == Gtk.ResponseType.OK:
            try:
                contact = self._db.new(cd.get_contact())
                if contact:
                    self._list.add(Row(contact))
            except Exception as exception:
                print(exception)
                self.show_message("Error", str(exception))

        cd.destroy()

    def edit(self, widget):
        selected_row = self._list.get_selected_row()
        if selected_row:
            contact = selected_row.get_contact()
            cd = ContactDialog(Crud.UPDATE, contact)
            if cd.run() == Gtk.ResponseType.OK:
                contact = cd.get_contact()
                selected_row.set_contact(contact)
            cd.destroy()

    def delete(self, widget):
        selected_row = self._list.get_selected_row()
        if selected_row:
            contact = selected_row.get_contact()
            cd = ContactDialog(Crud.DELETE, contact)
            if cd.run() == Gtk.ResponseType.OK:
                self._db.delete(contact.id)
                self._list.remove(selected_row)
            cd.destroy()

    def load(self):
        self._db = DbContact('database.db')
        for contact in self._db.list():
            self._list.add(Row(contact))

    def show_message(self, title, message):
        dialog = Gtk.MessageDialog()
        dialog.set_parent(self)
        dialog.set_title(title)
        dialog.set_markup(message)
        dialog.add_button('Ok', Gtk.ResponseType.OK)
        dialog.run()
        dialog.destroy()




if __name__ == '__main__':
    ad = AddressDialog()
    ad.run()
