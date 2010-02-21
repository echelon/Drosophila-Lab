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

from gene import Trait, Allele
from gene import Dominant, Recessive, Lethal, NonLethal

# ========================= #
#          TRAITS           #
# ========================= #

br = Trait('Bristle', 'BR')
bc = Trait('Body Color', 'BC')
an = Trait('Antennae', 'AN')
ec = Trait('Eye Color', 'EC')
es = Trait('Eye Shape', 'ES')
sz = Trait('Wing Size', 'SZ')
sh = Trait('Wing Shape', 'SH')
vn = Trait('Wing Vein', 'VN')
ag = Trait('Wing Angle', 'AG')

# ========================= #
#          ALLELES          #
# ========================= #

X, Y = ['x', 'y']

# References for gene mapping
# [1] http://www.ceebt.embo.org/projects/project13/material/project13.pdf

# Bristle
Allele('Forked', 'F',	  br, X, 56.3)
Allele('Shaven', 'SV',	  br, 4, 3.0)
Allele('Singed', 'SN',	  br, X, 21.0)
Allele('Spineless', 'SS', br, 3, 58.5)
Allele('Stubble', 'SB',	  br, 3, 58.2)

# Body Color
Allele('Black', 'BL',	bc, 2, 48.5)
Allele('Ebony', 'E',	bc, 3, 70.7)
Allele('Sable', 'S',	bc, X, 43.0)
Allele('Tan', 'T',		bc, X, 27.7)
Allele('Yellow', 'Y',	bc, X, 0.0)

# Antennae
Allele('Aristapedia', 'AR', an, 3, 47.7)

# Eye Color
Allele('Brown', 'BW',	ec, 2, 104.5)
Allele('Purple', 'PR',	ec, 2, 54.5)
Allele('Sepia', 'SE',	ec, 3, 26.0)
Allele('White', 'W',	ec, X, 1.5)

# Eye Shape
Allele('Bar', 'B',		es, X, 57.0)
Allele('Eyeless', 'EY',	es, 4, 2.0)
Allele('Lobe', 'L',		es, 2, 72.0)
Allele('Star', 'ST',	es, 2, 1.3)

# Wing Size
Allele('Apterous', 'AP',  sz, 2, 55.4)
Allele('Miniature', 'M',  sz, X, 36.1)
Allele('Vestigial', 'VG', sz, 2, 67.0)

# Wing Shape
Allele('Curly', 'CY',	  sh, 2, 6.1)
Allele('Curved', 'C',	  sh, 2, 75.5)
Allele('Dumpy', 'DP',	  sh, 2, 13.0)
Allele('Scalloped', 'SD', sh, X, 51.5)

# Wing Vein
Allele('Crossveinless', 'CV',	  vn, X, 13.7)
Allele('Radius Incomplete', 'RI', vn, 3, 48.4)

# Wing Angle
Allele('Dichaete', 'D', ag, 3, 41.0)


