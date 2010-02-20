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

# Bristle
Allele('Forked', 'F',	br, 2, 10)
Allele('Shaven', 'SV',	br, 2, 20)
Allele('Singed', 'SN',	br, 2, 30)
Allele('Spineless', 'SS', br, 2, 40)
Allele('Stubble', 'SB',	br, 2, 50)

# Body Color
Allele('Black', 'BL',	bc, 3, 10)
Allele('Ebony', 'E',	bc, 3, 20)
Allele('Sable', 'S',	bc, 3, 30)
Allele('Tan', 'T',		bc, 3, 40)
Allele('Yellow', 'Y',	bc, 3, 40)

# Antennae
Allele('Aristapedia', 'AR', an, 4, 40)

# Eye Color
Allele('Brown', 'BW',	ec, 2, 60)
Allele('Purple', 'PR',	ec, 2, 70)
Allele('Sepia', 'SE',	ec, 2, 80)
Allele('White', 'W',	ec, 2, 90)

# Eye Shape
Allele('Bar', 'B',		es, 3, 60)
Allele('Eyeless', 'EY',	es, 3, 70)
Allele('Lobe', 'L',		es, 3, 80)
Allele('Star', 'ST',	es, 3, 90)

# Wing Size
Allele('Apterous', 'AP', sz, 4, 60)
Allele('Miniature', 'M', sz, 4, 70)
Allele('Vestigial', 'VG', sz, 4, 80)

# Wing Shape
Allele('Curly', 'CY', sh, 2, 100)
Allele('Curved', 'C', sh, 2, 110)
Allele('Dumpy', 'DP', sh, 2, 120)
Allele('Scalloped', 'SD', sh, 2, 130)

# Wing Vein
Allele('Crossveinless', 'CV', vn, 3, 100)
Allele('Radius Incomplete', 'RI', vn, 3, 110)

# Wing Angle
Allele('Dichaete', 'D', ag, 4, 140)

