
class HaploSet(object):

	"""A haploid set of chromosomes. That is, only one of each chromosome."""

	def __init__(self, chromos = None):

		if not chromos:
			chromos = [[]]*4

		if len(chromos) != 4:
			raise Exception, "Improper number of chromosomes"

		self.chromos = chromos

	def __len__(self):
		return 4

	def __getitem__(self, key):
		return self.chromos[key]

	def __setitem__(self, key, val):
		self.chromos[key] = val

	def __str__(self):
		ret = "<HaploSet: \n"
		for i in range(4):
			ret += "\t%d  " % (i+1)
			ret += str(self.chromos[i])
			ret += "\n"
		return ret + "    \>"



class DiploSet(object):

	"""A diploid set of chromosomes. That is, two of each chromosome."""

	def __init__(self, pair1 = None, pair2 = None):
		"""Supply both pairs of chromosomes, or have a null/wildtype set 
		generated."""

		if not pair1:
			pair1 = [[]]*4

		if not pair2:
			pair2 = [[]]*4
			
		if len(pair1) != 4 or len(pair2) != 4:
			raise Exception, "Improper number of chromosomes"

		self.chromos = range(2)
		self.chromos[0] = pair1
		self.chromos[1] = pair2

	def getPair1(self):
		return self.chromos[0]

	def getPair2(self):
		return self.chromos[1]

	def __len__(self):
		return 2

	def __getitem__(self, key):
		return self.chromos[key]

	def __setitem__(self, key, val):

		if type(val) == HaploSet:
			val = val.chromos

		self.chromos[key] = val

	def __str__(self):
		ret = "<DiploSet: \n"
		for i in range(4):
			ret += "\t%d  " % (i+1)
			ret += str(self.chromos[0][i])
			ret += "\t"
			ret += str(self.chromos[1][i])
			ret += "\n"
		return ret + "    \>"

