

class Gamete(object):

	def __init__(self, chromos, sex):

		if type(chromos) != list || len(chromos) != 4:
			raise Exception, "Chromosome length for gamete is wrong." 

		if sex != 'f' && sex != 'm':
			raise Exception, "Improper sex parameter."

		self.chromos = chromos
		self.sex = sex

	def fuze(self, gam):
		"""New individuals are produced by the fusion of two gametes."""

		# New individual info
		newChromos = [0]* 4
		newSex = 'm'

		# Two haploids --> diploid
		# XXX: DO NOT SUPPORT CHROMOSOME DUPLICATION / COPY ERRORS.
		# Chromosome structure for diploids is: chromos[chromoNum][copyNum]
		for i in range(len(newChromos)):
			newChromos[i][0] = self.chromos
			newChromos[i][1] = gam.chromos

		# X-balance sex system 
		xCnt = 0
		if gam.sex == 'f':
			xCnt += 1
		if self.sex == 'f':
			xCnt += 1

		if xCnt >= 2:
			newSex = 'f'

		return Indiv(newChromos, newSex)


