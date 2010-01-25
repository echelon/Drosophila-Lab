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
#

class Trait(object):

	def __init__(self, name, abbr, desc = None):

		self.name = name
		self.abbr = abbr # Simplifies external dictionary lookup of Trait
		self.description = desc

		self.alleles = {}

	def addAllele(self, allele):
		"""Add an allele for this trait.
		Can only add each allele once. 
		Additionally sets trait pointer on the allele."""

		from allele import Allele

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
				

