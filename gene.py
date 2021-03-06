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

	# Static dictionary of all alleles {'abbr' => Allele}
	alleles = {}

	# Static dictionaries of all lethal/dominant alleles {'abbr' => Allele}
	# (For faster lookup.)
	dominants = {}
	lethals = {}

	# Map of allele chromosome positions {(ch#, mu) => Allele} 
	positions = {}

	@classmethod
	def get(cls, abbr):
		return cls.alleles[abbr.upper()]

	@classmethod
	def exists(cls, abbr):
		return abbr.upper() in cls.alleles

	@classmethod
	def getAll(cls):
		return self.alleles.values()

	@classmethod
	def getLethals(cls):
		return cls.lethals.values()

	@classmethod
	def getDominants(cls):
		return cls.dominants.values()

	@classmethod
	def list(cls):
		for tr in Trait.traits.values():
			print "%s" % tr.name
			for al in tr.alleles.values():
				print "\t(%s) %s" % (al.abbr, al.name)
			print ""

	def __init__(self, name, abbr, trait, onChromo, mapPos, *effects):
		"""Allele CTOR.
		onChromo can be ['x', 2, 3, 4]
		Effects can contain a string of "dominant" and/or "lethal".
		"""

		if type(trait) != Trait:
			raise TypeError, "Trait must be a Trait object." # TODO: String abbr ok

		if onChromo not in [2, 3, 4, 'x', 'X']:
			raise AssertionError, "Chromosome location improperly specified."

		if type(mapPos) != float or mapPos < 0.0 or mapPos > 200.0:
			raise AssertionError, "Map position out of bounds"

		self.name = name
		self.abbr = abbr
		self.trait = trait
		self.onChromo = onChromo # TODO: Special case: 'X' 
		self.mapPos = mapPos
		self.dominant = False
		self.lethal = False

		for e in effects:
			e = e.lower()
			if e == 'dominant':
				self.dominant = True
			elif e == 'lethal':
				self.lethal = True

		trait.addAllele(self)
		Allele.alleles[abbr] = self

		if self.lethal:
			Allele.lethals[abbr] = self

		if self.dominant:
			Allele.dominants[abbr] = self


	def __del__(self):
		"""Can't delete any alleles created."""
		import sys
		sys.exit("Fatal error: Cannot delete alleles.")

	def isDominant(self):
		return self.dominant

	def isLethal(self):
		return self.lethal

	def __repr__(self):
		"""String representation of Allele."""
		#return "%s <%s/%s>" % (self.name, self.trait.name, self.abbr)
		#return self.abbr
		return "%s@%.1f" % (self.abbr, self.mapPos)

	def __str__(self):
		ret = "\n%s (%s) allele\n" % (self.name, self.abbr)

		names = ['Trait', 'Chromosome', 'Map Units', 'Dominant', 'Lethal']
		vals = [self.trait.name, self.onChromo, self.mapPos, self.dominant,
				self.lethal]

		for i, name in enumerate(names): 
			ret += "    %s: %s\n" % (name, vals[i])

		return ret

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

	@classmethod
	def list(cls):
		for tr in cls.traits.values():
			print "(%s) %s" % (tr.abbr.lower(), tr.name)

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

