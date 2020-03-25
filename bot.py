import os
from selenium import webdriver


def send(message):
	text_box = browser.find_element_by_class_name("_13mgZ")
	text_box.send_keys(message)

def bebidas():
    send("Bebidas")

def salgados(self):
	send('Salgados')

def cervejas(self):
	send("cervejas")

def tiragostos(self):
	send("tiragostos")