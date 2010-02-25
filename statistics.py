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

def getStatisticsSex(offspring):
	pass

def getStats(offspring):
	"""Get statistics from offspring."""
	phenos = {}
	total = float(len(offspring))
	for o in offspring:
		ph = o.getPhenotypeStr()

		if ph not in phenos:
			phenos[ph] = 1
		else:
			phenos[ph] += 1

	print "Phenotype\tNum\tPercent\tRatio\n"
	for ph, num in phenos.items():
		percent = num/total * 100.0
		print "%s\t\t%d\t%.2f\n" % (ph, num, percent)

	print "Total offspring: %d" % int(total)
		

