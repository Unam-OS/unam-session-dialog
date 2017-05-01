#!/usr/bin/python3

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class init():
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file('unam-session-dialog.glade')
		self.win = self.builder.get_object('unam-session-dialog')
		self.win.connect('delete-event', Gtk.main_quit)

		self.btn_shutdown = self.builder.get_object('btn_shutdown')
		self.btn_shutdown.connect('clicked', self.btn_shutdown_click)

		self.btn_logout = self.builder.get_object('btn_logout')
		self.btn_logout.connect('clicked', self.btn_logout_click)

		self.btn_sleep = self.builder.get_object('btn_sleep')
		self.btn_sleep.connect('clicked', self.btn_sleep_click)

		self.btn_restart = self.builder.get_object('btn_restart')
		self.btn_restart.connect('clicked', self.btn_restart_click)

		self.label = self.builder.get_object('lbl_info')
		self.label.set_text('')

	### Button Events ###
	def btn_shutdown_click(self, button):
		self.label.set_text('Shutting down...')
		os.system("systemctl poweroff")

	def btn_logout_click(self, button):
		self.label.set_text('Logging out...')
		os.system("openbox --exit")

	def btn_sleep_click(self, button):
		self.label.set_text('Good night...')
		os.system("systemctl suspend")
		

	def btn_restart_click(self, button):
		self.label.set_text('Restarting...')
		os.system("systemctl restart")

	### SHOW APP ###
	def run(self):
		self.win.show_all()
		Gtk.main()

if __name__ == '__main__':
	usettings = init()
	usettings.run()
