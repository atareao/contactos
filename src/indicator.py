#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import sys
try:
    gi.require_version('AppIndicator3', '0.1')
    gi.require_version('Gtk', '3.0')
except Exception as exception:
    print(exception)

from gi.repository import AppIndicator3
from gi.repository import Gtk
from addressgui import AddressDialog

class Indicator:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            'contacts', 'contacts',
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_menu(self.build_menu())
        self.indicator.set_label('', '')
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.set_icon()

    def set_icon(self):
        # TODO: add path
        #self.indicator.set_icon_theme_path(path)
        self.indicator.set_icon_full('contactos', '')

    def build_menu(self):
        menu = Gtk.Menu()
        menu_addressbook = Gtk.MenuItem.new_with_label("Address Book")
        menu_addressbook.connect('activate', self.on_menu_addressbook_activate)
        menu.append(menu_addressbook)

        menu.append(Gtk.SeparatorMenuItem())

        menu_quit = Gtk.MenuItem.new_with_label('Quit')
        menu_quit.connect('activate', self.quit)
        menu.append(menu_quit)

        menu.show_all()
        return menu

    def on_menu_addressbook_activate(self, widget):
        ad = AddressDialog()
        ad.run()

    def quit(self, widget):
        Gtk.main_quit()
        sys.exit(0)

def main():
    Indicator()
    Gtk.main()

if __name__ == '__main__':
    main()
