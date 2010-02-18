# Open Drosophila Lab
# Copyright (C) 2010  Brandon Thomas Suit
#	http://possibilistic.org
#	mailto:[echelon,brandon.suit]@gmail.com
#
# (potentially) For Southern Polytechnic State University
#	http://www.spsu.edu
#
# Open Drosophila Lab is an open source reimplementation of Virtual FlyLab,
# a for-pay resource by the California State University and Benjamin Cummings.
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU Affero General Public License as
#	published by the Free Software Foundation, either version 3 of the
#	License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU Affero General Public License for more details.
#
#	You should have received a copy of the GNU Affero General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
from allele import Allele
from trait import Trait
from defs import defs

from chromoset import HaploSet, DiploSet
from gamete import Gamete

class Individual(object):

	def __init__(self, chromos = None, sex = None):
		"""Constructor. Sex is optionally specifiable."""

		if not sex:
			sex = 'm'

		if not chromos:
			chromos = DiploidSet()

		if sex != 'm' and sex != 'f':
			raise Exception, "Invalid sex"

		if type(chromos) != DiploSet:
			raise Exception, "Invalid chromos"

		self.chromos = chromos
		self.sex = sex

	def isMale(self):
		"""Return true if individual is male, false if it is female."""
		# TODO: chromosome-based determinance
		return (self.sex == 'm')

	def mateMany(self, o, numOffspring = 1000):

		# Vary the number of offspring slightly 
		diff = int(random.gauss(0, 12))
		numOffspring += diff

		progeny = []
		for i in range(numOffspring):
			progeny.append(self.mate(other))

		return progeny

	def getGamete(self):

		# XXX: Males do not cross over.
		# XXX: Produce 4, but only return 1. 

		nsex = 'f'
		hap = HaploSet()

		# XXX: Males do not cross over.
		# Also, there's a 50/50 chance for male returning 'X' or 'Y' chromosome.		
		if self.isMale():

			for i in range(4):
				rand = random.randint(0, 1)
				if i == 0 and rand == 1:
					gamSex = 'm'
				hap[i] = self.chromos[rand] 

			if random.randint(0, 1):
				nsex = 'm'

		gam = Gamete(hap, nsex)

		return gamete

	def mate(self, o):
		"""Mate the individual with another from the opposite sex."""
		if self.sex == o.sex:
			raise Exception, "Cannot mate two members of the same sex."

		g1 = self.getGamete()
		g2 = o.getGamete()

		return g1.fuze(g2)




	####### ========= TODO FIXME UPDATE THESE TODO FIXME =========== ###########
	####### ========= TODO FIXME UPDATE THESE TODO FIXME =========== ###########
	####### ========= TODO FIXME UPDATE THESE TODO FIXME =========== ###########

	def setHomozygousFor(self, allele, trait = None):
		"""Set the individual as homozygous for an allele of a trait."""
		# TODO: THIS IS GOING TO BREAK THE MATE METHOD!!!!!

		if type(trait) == Trait:
			allele = trait.getAllele(allele)
			return self.__doSetHomozygousFor(allele)

		if type(allele) == Allele:
			return self.__doSetHomozygousFor(allele)

		if type(allele) == str:
			allele = defs.getAllele(allele)
			return self.__doSetHomozygousFor(allele)

		return False # TODO: Raise exception? 

	def setHeterozygousFor(self):
		# TODO ? (self, allele, trait, chromoPairNum)
		pass

	def __doSetHomozygousFor(self, allele):
		"""Private method - sets homozygous for the allele."""
		if type(allele) != Allele:
			raise TypeError, \
				"Allele was not an object or could not be looked up in dict."

		abbr = allele.trait.abbr
		self.chromosomes[0][abbr] = allele
		self.chromosomes[1][abbr] = allele



	def isDead(self):
		"""Check for the presence of two lethal alleles."""
		return False # TODO


	def getGenotypeStr(self):
		# TODO: THIS IS A TEMPORARY METHOD
		st = "<"
		for gene in self.chromosomes[0].keys():
			st += str(self.chromosomes[0][gene]) + "/"
			st += str(self.chromosomes[1][gene]) + "; "
		st = st[:-2] + ">"
		return st


	#def __repr__(self):
	#	"""String representation of the individual"""
	#	sexes = ['Male', 'Female']
	#	ret = sexes[self.sex]
	#
	#	if not self.chromosomes[0]:
	#		ret += " <+>"
	#		return ret
	#
	#	ret += " <"
	#	for gene in self.chromosomes[0].keys():
	#		ret += str(self.chromosomes[0][gene].abbr) + "/"
	#		ret += str(self.chromosomes[1][gene].abbr) + "; "
	#
	#	ret = ret[:-2] + ">"
	#	return ret
	#
