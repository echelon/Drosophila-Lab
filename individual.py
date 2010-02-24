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
from defs import CHROMOSOME_LENGTHS

from chromoset import HaploSet, DiploSet
from chromosome import Chromo

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

		if sex and chromos:
			raise Exception, "Cannot supply both DiploSet and sex parameter."

		if sex and (sex != 'm' and sex != 'f'):
			raise Exception, "Invalid sex specified."

		if chromos and type(chromos) != DiploSet:
			raise Exception, "Invalid DiploSet provided for individual"


		self.chromos = chromos
		self.sex = None 		# Cache of X-balance sex

		if not sex:
			sex = 'f'

		# Set up the object based on input
		if chromos:
			self.__cacheSex()
		else:
			self.chromos = DiploSet()
			self.__setSex(sex)


	# ======================================================== #
	#                Gender-related methods                    #
	# ======================================================== #

	def isFemale(self):
		"""Test if individual is female."""
		if not self.sex:
			self.__cacheSex()
		return (self.sex == 'f')

	def getSex(self):
		"""Return sex string."""		
		if not self.sex:
			self.__cacheSex()
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
		# For consistency, First Chromo I is always X, Second is either X or Y

		self.chromos[0][0] = Chromo(kind='x')

		if sex == 'm':
			self.chromos[1][0] = Chromo(kind='y')
		else:
			self.chromos[1][0] = Chromo(kind='x')

	def __cacheSex(self):
		"""Calculate sex based on X-balance system and cache the result.
		This is used for the drosophila the user does not manually create (the 
		progeny).
		"""

		# Implementation of X-balance system of sex determinancy
		cnt = 0
		if self.chromos[0][0].isX():
			cnt += 1
		if self.chromos[1][0].isX():
			cnt += 1

		if cnt >= 2:
			self.sex = 'f'
		else:
			self.sex = 'm'


	# ======================================================== #
	#          Manual Gene-setting related methods             #
	# ======================================================== #

	def reset(self):
		"""Reset the individual to wildtype, only preserve sex."""
		self.__cacheSex() # Make sure sex is cached

		for i in range(4):
			self.chromos[0][i] = Chromo()
			self.chromos[1][i] = Chromo()

		self.__setSex(self.sex)

	def setAs(self, allele):
		"""Set HOMOZYGOUS for the allele, unless lethal or sex-linked.
		Supply the allele abbreviation for lookup.
		Returns False if the allele couldn't be set (x-linked lethal for males.)
		"""
		if type(allele) == str:
			allele = Allele.get(allele.upper())

		if type(allele) != Allele:
			raise Exception, "Must supply allele or allele abbreviation."

		if self.numCopies(allele) > 0:
			raise Exception, "Cannot set allele if already present."

		chromo = allele.onChromo
		lethal = allele.isLethal()		

		if chromo not in [2, 3, 4, 'x', 'X']:
			raise Exception, \
				"Allele supplied is not on a valid chromosome."

		# Autosomal genes
		if chromo in [2, 3, 4]:
			self.chromos[0][chromo-1].append(allele)
			if not lethal:
				self.chromos[1][chromo-1].append(allele)

			return

		# X-linked genes
		if not self.sex:
			self.__cacheSex()

		# Can't manually create X-linked lethal males!
		if self.sex == 'm' and lethal:
			return

		self.chromos[0][0].append(allele)

		if self.sex == 'f' and not lethal:
			self.chromos[1][0].append(allele)

		return

	def setWildFor(self, trait):
		"""Basically unsets any allele of a trait, returning to the 
		NULL/wildtype state."""
		if type(trait) == str:
			trait = Trait.get(traitAbbr.upper())

		if type(trait) != Trait:
			raise Exception, "Must supply Trait or trait abbreviation."

		# Not very efficient -- don't rely on this
		for al in trait.alleles.values():
			for i in range(4):
				if al.abbr in self.chromos[0][i]:
					self.chromos[0][i].remove(al)
				if al.abbr in self.chromos[1][i]:
					self.chromos[1][i].remove(al)


	# ======================================================== #
	#            Mating of individuals / Meiosis               #
	# ======================================================== #
	
	def mate(self, other, num = 1, vary = False): 
		"""Mate the individual with another from the opposite sex."""

		if self.sex == other.sex:
			raise Exception, "Cannot mate two members of the same sex."

		# Vary the number of offspring slightly 
		if vary:
			diff = int(random.gauss(0, 12))
			num += diff

		# Produce all but double-lethal offspring
		progeny = []
		for i in range(num):
			indiv = self.__doMate(other)
			if indiv.isDead():
				continue
			progeny.append(indiv)

		return progeny

	def __doMate(self, o):
		"""Create a single offspring."""

		newGenome = DiploSet()

		# Two haploid gametes --> diploid
		# DOES NOT SUPPORT CHROMOSOME DUPLICATION / COPY ERRORS.
		newGenome[0] = self.getGamete()
		newGenome[1] = o.getGamete()

		# For consistency's sake, y chromo should always be on second pair
		if newGenome[0][0].isY():
			temp = newGenome[0][0]
			newGenome[0][0] = newGenome[1][0]
			newGenome[1][0] = temp

		return Individual(newGenome)


	def getGamete(self):
		"""Create a gamete from the individual."""

		# XXX TODO: Produce 4, but only return 1.  Do actual meiosis.
		# XXX XXX XXX: Ensure these are being *copied!*

		hap = HaploSet()

		# XXX TODO FIXME: Female crossover!!
		# XXX XXX: Verify this is correct crossover! 
		# XXX: Needs correct probabilities, etc.
		# XXX: Double crossover!!
		if self.isFemale():
			sis = range(2)
			for i in range(4):
				sis[0] = self.chromos[0][i].getCopy()
				sis[1] = self.chromos[1][i].getCopy()
				sis[0].crossover(sis[1])
				hap[i] = sis[random.randint(0, 1)]

		# Males do not cross over.
		# Note the 50/50 chance for a male returning the 'X' or 'Y' chromosome.		
		if not self.isFemale():
			for i in range(4):
				hap[i] = self.chromos[random.randint(0, 1)][i].getCopy()

		return hap


	# ======================================================== #
	#                 Genotype and Lethality                   #
	# ======================================================== #

	def numCopies(self, allele):
		"""Return the number of copies of the allele."""
		if type(allele) == str:
			allele = Allele.get(allele.upper())

		if type(allele) != Allele:
			raise Exception, "Must supply Allele or allele abbreviation."

		chromo = allele.onChromo
		cnt = 0

		# Autosomal
		if chromo in [2, 3, 4]:
			if allele in self.chromos[0][chromo-1]:
				cnt += 1
			if allele in self.chromos[1][chromo-1]:
				cnt += 1

			return cnt

		# Sex-linked
		if allele in self.chromos[0][0]:
			cnt += 1

		if not self.isFemale():
			return cnt

		if allele in self.chromos[0][1]:
			cnt += 1

		return cnt

	def isDead(self):
		"""The individual is dead if it has any two lethal allele copies."""

		lethals = Allele.getLethals() 

		for al in lethals:
			num = self.numCopies(al)
			if num > 1:
				return True

			# Hemizygous males
			if type(al.onChromo) == str and num > 0 and not self.isFemale(): 
				return True

		return False


	# ======================================================== #
	#           Phenotype (Dominance/Recessiveness)            #
	# ======================================================== #

	def getPhenotype(self):
		"""Get a phenotype list for the individual based on dominance/
		recessiveness."""
		ret = ""
		alleles = {}
		pheno = []

		for x in self.chromos[0] + self.chromos[1]:
			for al in x:
				if al.abbr not in alleles:
					alleles[al.abbr] = 1
				else:
					alleles[al.abbr] += 1

		for abbr, num in alleles.items():
			if num > 1:
				pheno.append(abbr)
				continue
			if abbr in Allele.dominants:
				pheno.append(abbr)
				continue

		pheno.sort()
		return pheno

	def getPhenotypeStr(self):
		"""Get a phenotype string for the individual based on dominance/
		recessiveness."""
		return '/'.join(self.getPhenotype())


	# ======================================================== #
	#              Representation, etc. methods                #
	# ======================================================== #

	def __repr__(self):
		ret = "<individual %s\n" % self.getSex()
		ret += str(self.chromos)
		return ret


# =============================
# Console time-saving shortcuts
# =============================

class Indiv(Individual):
	def getPheno(self):
		return self.getPhenotype()

def Male():
	return Indiv(sex='m')

def Female():
	return Indiv(sex='f')

