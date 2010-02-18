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

from trait import Trait
from allele import Allele

class defs(object):
	"""Simply an accessor to the traits and alleles.
	Do not instantiate. 

		traits, alleles = defs.traits, defs.alleles

		trait = defs.getAllele("D") # Returns "Dichaete"

		trait = defs.getWildtype("BR") # Returns the Bristle wildtype
	"""

	# Dictionary lookup by abbreviation for all traits and alleles
	traits = {}
	alleles = {}
	wildtypeAlleles = {}

	def __init__(self):
		raise Exception, "Cannot instantiate defs class."

	@classmethod
	def addTrait(cls, trait):
		cls.traits[trait.abbr] = trait

	@classmethod
	def addAllele(cls, allele):
		print "Adding allele"
		cls.alleles[allele.abbr] = alleles

	@classmethod
	def addWildtype(cls, wildtype):
		cls.wildtypeAlleles[wildtype.abbr] = wildtype

	@classmethod
	def getAllele(cls, abbr):
		"""Look up the allele by its abbreviation. NOTE: Cannot look up +!"""
		if abbr == '+':
			return False

		abbr = abbr.upper()
		for al in cls.alleles.values():  # TODO: Dict, not loop
			if al.abbr == abbr:
				return al

		return False

	@classmethod
	def getWildtype(cls, abbr):
		"""Look up the wildtype for a trait by the trait's abbreviation."""
		abbr = abbr.lower()

		trait = None
		for tr in cls.traits.values():	# TODO: Dict, not loop
			if tr.abbr == abbr:
				trait = tr

		if not trait:
			return False

		return trait.getWildtype()


# TODO: Just creating these should register them with the dictionary. 
# XXX: Note - the dictionary keys here are NOT NOT NOT abbreviations used 
t = {
	'bristle' :		Trait('Bristle', 'br'),
	'body_color':	Trait('Body Color', 'bc'),
	'antennae':		Trait('Antennae', 'an'),
	'eye_color':	Trait('Eye Color', 'ec'),
	'eye_shape':	Trait('Eye Shape', 'es'),
	'wing_size':	Trait('Wing Size', 'wsz'),
	'wing_shape':	Trait('Wing Shape', 'wsh'),
	'wing_vein':	Trait('Wing Vein', 'wv'),
	'wing_angle':	Trait('Wing Angle', 'wa'),
}


# TODO: For all non-wildtype, a dictionary should be created for lookup. 
a = {
	# Bristle
	'bristle+':		Allele('Wild Type', '+', t['bristle']),
	'forked':		Allele('Forked', 'F', t['bristle']),
	'Shaven':		Allele('Shaven', 'SV', t['bristle']),
	'Singed':		Allele('Singed', 'SN', t['bristle']),
	'Spineless':	Allele('Spineless', 'SS', t['bristle']),
	'Stubble':		Allele('Stubble', 'SB', t['bristle']),
	# Body Color
	'body_color+':	Allele('Wild Type', '+', t['body_color']),
	'black':		Allele('Black', 'BL', t['body_color']),
	'ebony':		Allele('Ebony', 'E', t['body_color']),
	'sable':		Allele('Sable', 'S', t['body_color']),
	'tan':			Allele('Tan', 'T', t['body_color']),
	'yellow':		Allele('Yellow', 'Y', t['body_color']),
	# Antennae
	'antennae+':	Allele('Wild Type', '+', t['antennae']),
	'aristapedia':	Allele('Aristapedia', 'AR', t['antennae']),
	# Eye Color
	'eye_color+':	Allele('Wild Type', '+', t['eye_color']),
	'brown':		Allele('Brown', 'BW', t['eye_color']),
	'purple':		Allele('Purple', 'PR', t['eye_color']),
	'sepia':		Allele('Sepia', 'SE', t['eye_color']),
	'white':		Allele('White', 'W', t['eye_color']),
	# Eye Shape
	'eye_shape+':	Allele('Wild Type', '+', t['eye_shape']),
	'bar':			Allele('Bar', 'B', t['eye_shape']),
	'eyeless':		Allele('Eyeless', 'EY', t['eye_shape']),
	'lobe':			Allele('Lobe', 'L', t['eye_shape']),
	'star':			Allele('Star', 'ST', t['eye_shape']),
	# Wing Size
	'wing_size+':	Allele('Wild Type', '+', t['wing_size']),
	'apterous':		Allele('Apterous', 'AP', t['wing_size']),
	'miniature':	Allele('Miniature', 'M', t['wing_size']),
	'vestigial':	Allele('Vestigial', 'VG', t['wing_size']),
	# Wing Shape
	'wing_shape+':	Allele('Wild Type', '+', t['wing_shape']),
	'curly':		Allele('Curly', 'CY', t['wing_shape']),
	'curved':		Allele('Curved', 'C', t['wing_shape']),
	'dumpy':		Allele('Dumpy', 'DP', t['wing_shape']),
	'scalloped':	Allele('Scalloped', 'SD', t['wing_shape']),
	# Wing Vein 
	'wing_vein+':	Allele('Wild Type', '+', t['wing_vein']),
	'crossveinless': Allele('Crossveinless', 'CV', t['wing_vein']),
	'incomplete':	Allele('Radius Incomplete', 'RI', t['wing_vein']),
	# Wing Angle
	'wing_angle+':	Allele('Wild Type', '+', t['wing_angle']),
	'dichaete':		Allele('Dichaete', 'D', t['wing_angle']),
}




def testGetPhenotype():
	pass

