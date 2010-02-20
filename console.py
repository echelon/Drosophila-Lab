#!/usr/bin/env python2.6

"""Import libraries into console easily."""

from chromoset import HaploSet, DiploSet
from individual import Individual, Indiv
from gamete import Gamete
from gene import Trait, Allele
#from sex import Male, Female

def clear():
	print "\n"*40


a, b = range(2)
def create():
	a = Indiv()

	setA = [
		'bl', 'y', 's', 't', # Body colors

		'b', 'pr', 'ss', 'sv'
	]
	for x in setA:
		a.setAs(x)

	globals()['a'] = a
	globals()['z'] = a

	globals()['b'] = Indiv(sex='m')

	return a

create()



