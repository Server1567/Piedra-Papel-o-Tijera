#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

# Variables globales
f1 = None
f2 = None
f3 = None
F1 = None
F2 = None
F3 = None

print '                                                             '
print '------------------PIEDRA, PAPEL O TIJERA---------------------'
print '                                                             '

def select():
	option = raw_input("Piedra, Papel o Tijera? -> ")
	if option == "Piedra" or option == "piedra":
		global f1
		f1 = "Piedra"
		print "Tu: Piedra"

	elif option == "Papel" or option == "papel":
		global f2
		f2 = "Papel"
		print "Tu: Papel"

	elif option == "Tijera" or option == "tijera":
		global f3
		f3 = "Tijera"
		print "Tu: Tijera"

	else:
		print "Asegurate de escribir bien tu opcion :/"
select()

# piedra, papel o tijera

def random():
	r = randint(0,2)

	if r == 0:
		global F1
		F1 = "Piedra"
		print "El: Piedra"

	elif r == 1:
		global F2
		F2 = "Papel"
		print "El: Papel"

	elif r == 2:
		global F3
		F3 = "Tijera"
		print "El: Tijera"

	else:
		print "Hubo un error :("
random()

def finish():
	global f1
	global f2
	global f3
	global F1
	global F2
	global F3

	if f1 == "Piedra" and F1 == "Piedra":
		print "************ TIE *****************"

	elif f1 == "Piedra" and F2 == "Papel":
		print "************ YOU LOSS *****************"

	elif f1 == "Piedra" and F3 == "Tijera":
		print "************ YOU WINN *****************"

	elif f2 == "Papel" and F1 == "Piedra":
		print "************ YOU WINN *****************"

	elif f2 == "Papel" and F2 == "Papel":
		print "************ TIE *****************"

	elif f2 == "Papel" and F3 == "Tijera":
		print "************ YOU LOSS *****************"

	elif f3 == "Tijera" and F1 == "Piedra":
		print "************ YOU LOSS *****************"

	elif f3 == "Tijera" and F2 == "Papel":
		print "************ YOU WINN *****************"

	elif f3 == "Tijera" and F3 == "Tijera":
		print "************ TIE *****************"

	else:
		print "************ SYSTEM ERROR SERVER1567 *****************"
finish()
