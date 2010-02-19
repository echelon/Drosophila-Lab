from chromoset import HaploSet, DiploSet

###
# Usage
#	g1 = Gamete(HaploSet([...])) # TODO: Do away with sex parameter
#	g2 = Gamete(HaploSet([...]))
#
#	indiv = g1.fuze(g2)

class Gamete(object):

	"""This class represents a haploid gamete."""

	def __init__(self, genome, sex):

		if type(genome) != HaploSet:
			raise Exception, "Genome must be haploid."

		if sex != 'f' and sex != 'm':
			raise Exception, "Improper sex parameter."

		self.genome = genome
		self.sex = sex

	def fuze(self, gam):
		"""New individuals are produced by the fusion of two gametes."""

		from individual import Individual

		if type(gam) != Gamete:
			raise Exception, "Gamete must fuze with another gamete."

		# New individual info
		newGenome = DiploSet()
		newSex = 'm'

		# Two haploids --> diploid
		# XXX: DO NOT SUPPORT CHROMOSOME DUPLICATION / COPY ERRORS.
		newGenome[0] = self.genome
		newGenome[1] = gam.genome

		# X-balance sex system 
		# XXX: Sex chromosome information is passed in by a string
		xCnt = 0
		if gam.sex == 'f':
			xCnt += 1
		if self.sex == 'f':
			xCnt += 1

		if xCnt >= 2:
			newSex = 'f'

		return Individual(newGenome, newSex)

	def __repr__(self):

		return "<%s gamete>" % self.sex.upper()

