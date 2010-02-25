#!/usr/bin/env python2.6

"""Import libraries into console easily."""

from chromoset import HaploSet, DiploSet
from individual import Individual
from individual import Indiv, Male, Female # Shortcuts
from gene import Trait, Allele
from defs import CHROMOSOME_LENGTHS
from chromosome import Chromo
from statistics import getStats

def clear():
	print "\n"*40


a, b, c = range(3)


def countSex(indivs):
	"""Count the sex in a list of individuals."""
	male = 0
	female = 0

	for indiv in indivs:
		if indiv.isFemale():
			female += 1
		else:
			male += 1

	print "Male: %d, Female: %d, Total: %d" % (male, female, len(indivs))

def create():
	a = Male()
	b = Female()

	a.setAs('pr')

	globals()['a'] = a
	globals()['b'] = b

create()



