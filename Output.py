import json
import math

class Output:
	def __init__(self, values):
		self.values = json.loads(values)
		self.bigfivePercentage = []
		self.xLabelsMain = []
		self.bigfiveList = {}
		self.facetsList = {}

		traits = self.values["tree"]["children"][0]["children"][0]["children"]
		for trait in traits:
			self.xLabelsMain.append(trait["name"].encode("ascii"))
			self.bigfivePercentage.append(math.ceil(trait["percentage"]*10000)/100)
			self.xLabelsFacets = []
			self.facetsPercentage = []
			for facet in trait["children"]:
				self.xLabelsFacets.append(facet["name"].encode("ascii"))
				self.facetsPercentage.append(math.ceil(facet["percentage"]*10000)/100)
			self.facetsList[trait["name"].encode("ascii")] = {"graphTitle": "Facets" ,"xAxisLabels" : self.xLabelsFacets, "xAxisTitle" : "Facets", "yAxisTitle" : "Average percentile", "yAxisValues" : self.facetsPercentage}
		self.bigfiveList = {"graphTitle": "BigFive" ,"xAxisLabels" : self.xLabelsMain, "xAxisTitle" : "Traits", "yAxisTitle" : "Average percentile", "yAxisValues" : self.bigfivePercentage}
