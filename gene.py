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

# =============================================================
#						ALLELE CLASS
# =============================================================

class Allele(object):

	# Static dictionary of all alleles instantiated 
	alleles = {}

	@classmethod
	def get(cls, abbr):
		return cls.alleles[abbr]

	@classmethod
	def exists(cls, abbr):
		return abbr in cls.alleles

	def __init__(self, name, abbr, trait, onChromo, mapPos, *effects):

		if type(trait) != Trait:
			raise TypeError, "Trait must be a Trait object." # TODO: String abbr ok

		if onChromo not in [2, 3, 4, 'x', 'X', 'y', 'Y']:
			raise AssertionError, "Chromosome location improperly specified."

		if mapPos < 0.0 or mapPos > 200.0:
			raise AssertionError, "Map position out of bounds"

		self.name = name
		self.abbr = abbr
		self.trait = trait
		self.onChromo = onChromo # TODO: Special case: 'X' or 'Y'
		self.mapPos = mapPos

		Allele.alleles[abbr] = self
		trait.addAllele(self)

	def __repr__(self):
		"""String representation of Allele."""
		if self.trait:
			return "%s <%s/%s>" % (self.name, self.trait.name, self.abbr)
		return "%s <NoTrait/%s>" % (self.name, self.abbr)


# =============================================================
#						TRAIT CLASS
# =============================================================

class Trait(object):

	"""Represents a trait which may have one or more alleles."""

	# Static dict of all traits created
	traits = {}

	@classmethod
	def get(cls, abbr):
		return cls.traits[abbr]

	@classmethod
	def exists(cls, abbr):
		return abbr in cls.traits

	def __init__(self, name, abbr, desc = None):
		"""Trait CTOR."""

		self.name = name
		self.abbr = abbr # Simplifies external dictionary lookup of Trait
		self.description = desc

		self.alleles = {}

		Trait.traits[abbr] = self

	def addAllele(self, allele):
		"""Add an allele for this trait.
		Can only add each allele once. 
		Additionally sets trait pointer on the allele."""

		if type(allele) != Allele:
			raise TypeError, "Must add an Allele object."

		if allele.abbr in self.alleles:
			raise Exception, \
				"Allele '%s' already exists for trait '%s'." % (
					allele.name, self.name
				)

		self.alleles[allele.abbr] = allele
		allele.trait = self

	def getAllele(self, abbr):
		"""Get an allele of the trait by its abbreviation."""
		if abbr not in self.alleles:
			return False

		return self.alleles[abbr]

	def __repr__(self):
		"""String representation of a Trait."""
		return "Trait <%s>" % self.name

