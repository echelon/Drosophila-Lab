#!/usr/bin/env python2.6
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

"""

Tasks -

1) Hold multiple generations - 

	P, F1, F2, F3 ... 

2) Make sure same genotype (a/A == A/a) is easy to use in calculations. 

3) Create "chromosome", "gene", and/or "allele" classes?
	
	Perhaps a "GenePair" object that can easily convert a/A to A/a or some
	universal representation. (Check flylab to see what it does.)

		^^^^ Actually check it before coding anything!!!

4) How are wild-types handled?

	Are the genes that aren't being used being encoded at all? 
	Not encoding them could save machine resources, especially if this is hosted
	by django! 

5) Make it easy to extract parameters from the generations:

	* Each phenotype exhibited
		* The underlying genotypes behind those (which are hidden)


6) Encode dominance

	A > B > + > C etc. 

* Dominance, Recessiveness
* Epistasis
* Sex-linkage
* Recombination
* Genetic Mapping. 

======== GENES ========

(The following traits have Wild Type as well.)

[Bristle]
	Forked, Shaven, Singed, Spineless, Stubble

[Body Color]
	Black, Ebony, Sable, Tan, Yellow

[Antennae]
	Aristapedia

[Eye Color]
	Brown, Purple, Sepia, White

[Eye Shape]
	Bar, Eyeless, Lobe, Star

[Wing Size]
	Apterous, Miniature, Vestigial

[Wing Shape]
	Curly, Curved, Dumpy, Scalloped

[Wing Vein]
	Crossveinless, Incomplete
	
[Wing Angle]
	Dichaete

"""



from individual import Individual
from statistics import Statistics
from trait import Trait
from allele import Allele
from defs import defs

def main():

	generations = []

	chromosMale = [
		{'gene1': 'A', 'gene2:': 'b'},
		{'gene1': 'a', 'gene2:': 'b'}
	]
	chromosFemale = [
		{'gene1': 'A', 'gene2:': 'b'},
		{'gene1': 'a', 'gene2:': 'b'}
	]

	male = Individual('male')
	female = Individual('female')


	print male
	print female
	print ""

	male.setHomozygousFor("F")
	male.setHomozygousFor("BL")

	print male

	#offspring = male.mate(female)

	#for o in offspring:
	#	print o

	#s = Statistics(offspring)
	#s.getStats()

	print defs.getAllele("y")

	#print defs.traits
	#print ""
	#print defs.alleles


if __name__ == '__main__': main()
