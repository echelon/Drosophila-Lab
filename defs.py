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

traits = {
	'bristle' :		Trait('Bristle'),
	'body_color':	Trait('Body Color'),
	'antennae':		Trait('Antennae'),
	'eye_color':	Trait('Eye Color'),
	'eye_shape':	Trait('Eye Shape'),
	'wing_size':	Trait('Wing Size'),
	'wing_shape':	Trait('Wing Shape'),
	'wing_vein':	Trait('Wing Vein'),
	'wing_angle':	Trait('Wing Angle'),
}

alleles = {
	# Bristle
	'bristle+':		Allele('Wild Type', '+', traits['bristle']),
	'forked':		Allele('Forked', 'F', traits['bristle']),
	'Shaven':		Allele('Shaven', 'SV', traits['bristle']),
	'Singed':		Allele('Singed', 'SN', traits['bristle']),
	'Spineless':	Allele('Spineless', 'SS', traits['bristle']),
	'Stubble':		Allele('Stubble', 'SB', traits['bristle']),
	# Body Color
	'body_color+':	Allele('Wild Type', '+', traits['body_color']),
	'black':		Allele('Black', 'BL', traits['body_color']),
	'ebony':		Allele('Ebony', 'E', traits['body_color']),
	'sable':		Allele('Sable', 'S', traits['body_color']),
	'tan':			Allele('Tan', 'T', traits['body_color']),
	'yellow':		Allele('Yellow', 'Y', traits['body_color']),
	# Antennae
	'antennae+':	Allele('Wild Type', '+', traits['antennae']),
	'aristapedia':	Allele('Aristapedia', 'AR', traits['antennae']),
	# Eye Color
	'eye_color+':	Allele('Wild Type', '+', traits['eye_color']),
	'brown':		Allele('Brown', 'BW', traits['eye_color']),
	'purple':		Allele('Purple', 'PR', traits['eye_color']),
	'sepia':		Allele('Sepia', 'SE', traits['eye_color']),
	'white':		Allele('White', 'W', traits['eye_color']),
	# Eye Shape
	'eye_shape+':	Allele('Wild Type', '+', traits['eye_shape']),
	'bar':			Allele('Bar', 'B', traits['eye_shape']),
	'eyeless':		Allele('Eyeless', 'EY', traits['eye_shape']),
	'lobe':			Allele('Lobe', 'L', traits['eye_shape']),
	'star':			Allele('Star', 'ST', traits['eye_shape']),
	# Wing Size
	'wing_size+':	Allele('Wild Type', '+', traits['wing_size']),
	'apterous':		Allele('Apterous', 'AP', traits['wing_size']),
	'miniature':	Allele('Miniature', 'M', traits['wing_size']),
	'vestigial':	Allele('Vestigial', 'VG', traits['wing_size']),
	# Wing Shape
	'wing_shape+':	Allele('Wild Type', '+', traits['wing_shape']),
	'curly':		Allele('Curly', 'CY', traits['wing_shape']),
	'curved':		Allele('Curved', 'C', traits['wing_shape']),
	'dumpy':		Allele('Dumpy', 'DP', traits['wing_shape']),
	'scalloped':	Allele('Scalloped', 'SD', traits['wing_shape']),
	# Wing Vein 
	'wing_vein+':	Allele('Wild Type', '+', traits['wing_vein']),
	'crossveinless': Allele('Crossveinless', 'CV', traits['wing_vein']),
	'incomplete':	Allele('Radius Incomplete', 'RI', traits['wing_vein']),
	# Wing Angle
	'wing_angle+':	Allele('Wild Type', '+', traits['wing_angle']),
	'dichaete':		Allele('Dichaete', 'D', traits['wing_angle']),

}


def testGetPhenotype():

	pass
