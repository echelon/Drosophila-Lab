# Open Drosophila Lab
# Copyright (C) 2010  Brandon Thomas Suit
#	http://possibilistic.org
#	mailto:[echelon|brandon.suit]@gmail.com
#
# (potentially) For Southern Polytechnic State University
#	http://www.spsu.edu
#
# Open Drosophila Lab promotes the learning of basic non-Mendelian inheritance
# and gene mapping by engaging students in designing genetic crosses. It is an 
# open source reimplementation of Virtual FlyLab, a for-pay resource created by 
# California State University and publisher Benjamin Cummings. 
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
from gene import Trait, Allele
import defs

from chromoset import HaploSet, DiploSet
from gamete import Gamete

class Individual(object):

	def __init__(self, chromos = None, sex = None):
		"""Individual CTOR. 

		* If a diploset of chromosomes is specified, the individual will use
		  these as its genes. 
		* If sex is specified, it will force the sex of the individual and 
		  REMOVE any sex chromosomes, resetting them to WILDTYPE.

		For now, these parameters are mutually exclusive.
		"""

		if type(sex) == str:
			sex = sex.lower()

		if sex and (sex != 'm' and sex != 'f'):
			raise Exception, "Invalid sex specified."

		if chromos and type(chromos) != DiploSet:
			raise Exception, "Invalid DiploSet provided for individual"

		if sex and chromos:
			raise Exception, "Cannot supply both DiploSet and sex parameter."

		self.chromos = chromos
		self.sex = None

		if not sex:
			sex = 'f'

		# Set up the object based on input
		if chromos:
			self.__calcSex()
		else:
			self.chromos = DiploSet()
			self.__setSex(sex)


	# ======================================================== #
	#                Gender-related methods                    #
	# ======================================================== #

	def isFemale(self):
		"""Test if individual is female."""
		if not self.sex:
			self.__calcSex()
		return (self.sex == 'f')

	def getSex(self):
		"""Return sex string."""		
		if not self.sex:
			self.__calcSex()
		return self.sex

	def __setSex(self, sex):
		"""Used by the constructor to set the sex of the individual.
		Removes any genes set for Chromosome I, resetting any traits present to 
		wild type."""

		if type(sex) != str:
			raise Exception, "Sex parameter must be a string."

		sex = sex.lower()

		if sex != 'm' and sex != 'f':
			raise Exception, "Invalid sex specified."

		self.sex = sex

		# Remove all genes from both pairs of Chromosome I
		# This *must* be done to ensure no errors in sex-linkage crop up
		self.chromos[0][0] = []
		self.chromos[1][0] = []

		# For consistency, First Chromo I is always X, Second is either X or Y
		self.chromos[0][0].append('xch')
		if sex == 'm':
			self.chromos[1][0].append('ych')
		else:
			self.chromos[1][0].append('xch')

	def __calcSex(self):
		"""Calculate sex based on X-balance system and cache the result.
		This is used for the drosophila the user does not manually create (the 
		progeny).
		"""

		# Implementation of X-balance system of sex determinancy
		cnt = 0
		if 'xch' in self.chromos[0][0]:
			cnt += 1
		if 'xch' in self.chromos[1][0]:
			cnt += 1

		if cnt >= 2:
			self.sex = 'f'
		else:
			self.sex = 'm'


	# ======================================================== #
	#              Gene-setting related methods                #
	# ======================================================== #

	def setAs(self, alleleAbbr):
		"""Set HOMOZYGOUS for the allele, unless lethal.
		Supply the allele abbreviation for lookup."""
		
		# TODO: Don't set homozygous if lethal or hemizygous

		alleleAbbr = alleleAbbr.upper()

		allele = Allele.get(alleleAbbr)
		chromo = allele.onChromo

		if chromo in [2, 3, 4]:
			self.chromos[0][chromo-1].append(alleleAbbr)
			self.chromos[1][chromo-1].append(alleleAbbr)


	def setHomozygousFor(self, allele):
		"""Set the individual as homozygous for an allele of a trait."""

		if type(allele) == str:
			allele = defs.getAllele(allele)

		return self.__doSetHomozygousFor(allele)


	def __doSetHomozygousFor(self, allele):
		"""Private method - sets homozygous for the allele."""
		if type(allele) != Allele:
			raise TypeError, \
				"Allele was not an object or could not be looked up in dict."

		abbr = allele.trait.abbr
		self.chromosomes[0][abbr] = allele
		self.chromosomes[1][abbr] = allele

	def setWildtypeFor(self, trait):
		"""Basically unsets any allele of a trait, returning to NULL/wildtype
		state."""

		pass


	# ======================================================== #
	#              Representation, etc. methods                #
	# ======================================================== #

	def __repr__(self):
		ret = "<individual %s\n" % self.getSex()
		ret += str(self.chromos)
		return ret


	# ======================================================== #
	#                  Mating of individuals                   #
	# ======================================================== #






	# =============== TODO / FIXME / UPDATE ================== #

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

class Indiv(Individual):
	"""This is a shortcut name for use in the console only."""

	def setWildFor(self, trait):
		return self.setWildtypeFor(trait)


