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
		self.chromos[0][0] = []
		self.chromos[1][0] = []

		# For consistency, First Chromo I is always X, Second is either X or Y
		self.chromos[0][0].append('xch')
		if sex == 'm':
			self.chromos[1][0].append('ych')
		else:
			self.chromos[1][0].append('xch')

	def __cacheSex(self):
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
	#          Manual Gene-setting related methods             #
	# ======================================================== #

	def setAs(self, alleleAbbr):
		"""Set HOMOZYGOUS for the allele, unless lethal or sex-linked.
		Supply the allele abbreviation for lookup.
		Returns False if the allele couldn't be set (x-linked lethal for males.)
		"""

		allele = Allele.get(alleleAbbr.upper())
		chromo = allele.onChromo
		lethal = allele.isLethal()		

		if chromo not in [2, 3, 4, 'x', 'X']:
			raise Exception, \
				"Allele supplied is not on a valid chromosome."

		# Autosomal genes
		if chromo in [2, 3, 4]:
			self.chromos[0][chromo-1].append(allele.abbr)
			if not lethal:
				self.chromos[1][chromo-1].append(allele.abbr)

			return True

		# X-linked genes
		if not self.sex:
			self.__cacheSex()

		# Can't manually create X-linked lethal males!
		if self.sex == 'm' and lethal:
			return False

		self.chromos[0][0].append(allele.abbr)

		if self.sex == 'f' and not lethal:
			self.chromos[1][0].append(allele.abbr)

		return True
				

	def setWildFor(self, traitAbbr):
		"""Basically unsets any allele of a trait, returning to NULL/wildtype
		state."""

		trait = Trait.get(traitAbbr.upper())

		# Not very efficient -- don't rely on this
		for al in trait.alleles.values():
			for i in range(4):
				if al.abbr in self.chromos[0][i]:
					self.chromos[0][i].remove(al.abbr)
				if al.abbr in self.chromos[1][i]:
					self.chromos[1][i].remove(al.abbr)

	def reset(self):
		"""Reset the individual to wildtype, only preserve sex."""
		self.__cacheSex() # Make sure sex is cached

		for i in range(4):
			self.chromos[0][i] = []
			self.chromos[1][i] = []

		self.__setSex(self.sex)


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
		if 'ych' in newGenome[0][0]:
			temp = newGenome[0][0]
			newGenome[0][0] = newGenome[1][0]
			newGenome[1][0] = temp

		return Individual(newGenome)


	def getGamete(self):
		"""Create a gamete from the individual."""

		# XXX TODO: Produce 4, but only return 1.  Do actual meiosis.

		hap = HaploSet()

		# XXX TODO FIXME: Female crossover!!
		if self.isFemale():
			for i in range(4):
				hap[i] = self.chromos[random.randint(0, 1)][i]

		# Males do not cross over.
		# Note the 50/50 chance for a male returning the 'X' or 'Y' chromosome.		
		if not self.isFemale():
			for i in range(4):
				hap[i] = self.chromos[random.randint(0, 1)][i]


		return hap


	# TODO
	def getCrossoverGamete(self):

		hap = HaploSet()

		for i in range(4):
			r = random.randint(0, 1) # Choose one copy at random
			sis1 = self.chromos[r][i]
			sis2 = self.chromos[r][i]

			sis1.sort(key=lambda x: x.mapPos)
			
		# TODO
			



	# ======================================================== #
	#                 Genotype and Lethality                   #
	# ======================================================== #

	def numCopies(self, alleleAbbr):
		"""Return the number of copies of the allele."""

		allele = Allele.get(alleleAbbr.upper())
		chromo = allele.onChromo

		cnt = 0

		# Autosomal
		if chromo in [2, 3, 4]:
			if allele.abbr in self.chromos[0][chromo-1]:
				cnt += 1
			if allele.abbr in self.chromos[1][chromo-1]:
				cnt += 1

			return cnt

		# Sex-linked
		if allele.abbr in self.chromos[0][0]:
			cnt += 1

		if not self.isFemale():
			return cnt

		if allele.abbr in self.chromos[0][1]:
			cnt += 1

		return cnt


	def isDead(self):
		"""The individual is dead if it has any two lethal allele copies."""

		lethals = Allele.getLethals() 

		for al in lethals:
			num = self.numCopies(al.abbr)
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
			for abbr in x:
				if abbr not in alleles:
					alleles[abbr] = 1
				else:
					alleles[abbr] += 1

		try:
			alleles.pop('xch')
			alleles.pop('ych')
		except KeyError:
			pass

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


	####### ========= TODO FIXME UPDATE THESE TODO FIXME =========== ###########
	####### ========= TODO FIXME UPDATE THESE TODO FIXME =========== ###########
	####### ========= TODO FIXME UPDATE THESE TODO FIXME =========== ###########

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



