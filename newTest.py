#/usr/bin/env python2.6

from chromoset import HaploSet, DiploSet
from gamete import Gamete



def main():

	chromo = [{}]*4
	chromo[1] = ['a', 'b']

	g1 = Gamete(HaploSet(chromo), 'm')
	g2 = Gamete(HaploSet(chromo), 'f')

	g3 = g1.fuze(g2)

	print g3



if __name__ == '__main__': main()
