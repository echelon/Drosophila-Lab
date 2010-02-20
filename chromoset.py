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

class HaploSet(object):

	"""A haploid set of chromosomes. That is, only one of each chromosome."""

	def __init__(self, chromos = None):

		if not chromos:
			chromos = [[]]*4

		if len(chromos) != 4:
			raise Exception, "Improper number of chromosomes"

		self.chromos = chromos

	# ============== Dict Access =================== #

	def __len__(self):
		return 4

	def __getitem__(self, key):
		return self.chromos[key]

	def __setitem__(self, key, val):
		self.chromos[key] = val

	def __contains__(self, item):
		return item in self.chromos

	# ============= Other ========================== #

	def __str__(self):
		ret = "<HaploSet: \n"
		for i in range(4):
			ret += "\t%d  " % (i+1)
			ret += str(self.chromos[i])
			ret += "\n"
		return ret + "    \>"



class DiploSet(object):

	"""A diploid set of chromosomes. That is, two of each chromosome."""

	def __init__(self, pair1 = None, pair2 = None):
		"""Supply both pairs of chromosomes, or have a null/wildtype set 
		generated."""

		if not pair1:
			pair1 = [[]]*4

		if not pair2:
			pair2 = [[]]*4
			
		if len(pair1) != 4 or len(pair2) != 4:
			raise Exception, "Improper number of chromosomes"

		self.chromos = range(2)
		self.chromos[0] = pair1
		self.chromos[1] = pair2

	def getPair1(self):
		return self.chromos[0]

	def getPair2(self):
		return self.chromos[1]

	def __len__(self):
		return 2

	def __getitem__(self, key):
		return self.chromos[key]

	def __setitem__(self, key, val):

		if type(val) == HaploSet:
			val = val.chromos

		self.chromos[key] = val


	def __str__(self):
		ret = "<DiploSet: \n"
		for i in range(4):
			ret += "\t%d  " % (i+1)
			ret += str(self.chromos[0][i])
			ret += "\t"
			ret += str(self.chromos[1][i])
			ret += "\n"
		return ret + "    \>"

