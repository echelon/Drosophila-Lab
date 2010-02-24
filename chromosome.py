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

from copy import copy

from gene import Allele, Trait
from defs import CHROMOSOME_LENGTHS

class Chromo(list):
	"""This class represents a chromosome or chromatid.
	It is an extension of the list data structure."""

	def __init__(self, kind=None):
		"""Chromo CTOR."""

		self.type = None	# None, X or Y

		if kind in [2, 3, 4]:
			self.type = kind
		elif kind in ['x', 'X', 'f', 'F']:
			self.type = 'x'
		elif kind in ['y', 'Y', 'm', 'M']:
			self.type = 'y'

		# TODO

	def isX(self):
		return self.type == 'x'

	def isY(self):
		return self.type == 'y'

	def crossover(self, o):
		"""Crossover with another chromatid. 
		Both chromatids are altered in-place"""

		ky = lambda x: x.mapPos

		self.sort(key=ky)
		o.sort(key=ky)

		pass # TODO

	def getCopy(self):
		"""Get a copy of the chromosome."""
		return copy(self)

	#def __copy__(self):
	#	pass # TODO


