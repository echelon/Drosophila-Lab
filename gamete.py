from chromoset import HaploSet, DiploSet

###
# Usage
#	g1 = Gamete(HaploSet([...])) # TODO: Do away with sex parameter
#	g2 = Gamete(HaploSet([...]))
#
#	indiv = g1.fuze(g2)

class Gamete(object):

	"""This class represents a haploid gamete."""

	def __init__(self, genome):

		if type(genome) != HaploSet:
			raise Exception, "Genome must be haploid."

		self.genome = genome

	def fuze(self, gam):
		"""New individuals are produced by the fusion of two gametes."""

		from individual import Individual

		if type(gam) != Gamete:
			raise Exception, "Gamete must fuze with another gamete."

		# New individual info
		newGenome = DiploSet()

		# Two haploids --> diploid
		# XXX: DO NOT SUPPORT CHROMOSOME DUPLICATION / COPY ERRORS.
		newGenome[0] = self.genome
		newGenome[1] = gam.genome

		return Individual(newGenome)

	def __repr__(self):

		return "<%s gamete>" % self.sex.upper()

