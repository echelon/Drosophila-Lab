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

class Statistics(object):

	def __init__(self, gen):
		"""Input the generation (list of individuals)"""
		self.generation = gen


	def getStats(self):
		genotypes = {}
		popSize = float(len(self.generation))

		for indiv in self.generation:
			gt = indiv.getGenotypeStr()
			if gt not in genotypes:
				genotypes[gt] = 1
			else:
				genotypes[gt] += 1

		ratios = {}
		for gt, num in genotypes.items():
			ratios[gt] = num / popSize

		print "Population size is %f" % popSize
		print genotypes
		print ""
		print ratios
