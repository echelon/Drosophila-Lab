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

class Allele(object):

	def __init__(self, name, abbr, trait, image = None):

		from trait import Trait

		if type(trait) != Trait:
			raise TypeError, "Trait must be a Trait object."

		self.name = name
		self.abbr = abbr
		self.trait = trait

		trait.addAllele(self)

	def __repr__(self):
		"""String representation of Allele."""
		if self.trait:
			return "Allele %s <%s/%s>" % (self.abbr, self.trait.name, self.name)
		return "Allele %s <NoTrait/%s>" % (self.abbr, self.name)
