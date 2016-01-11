from django.shortcuts import render
from django.http import HttpResponse
from Twitter_insights import Twitter_insights
from Output import Output
import json

def getquery(request):
	return render(request, 'index.html')
	
def analysis(request):
	if 'Query_text' in request.GET and request.GET['Query_text']:
		query = request.GET['Query_text']
		errors = []
		bigfive = []
		facets = []
		T = Twitter_insights()
		flag, count = T.getcount(query)
		if flag == 0:
			error = 'Sorry, too few tweets for analysis. Please try another search term.'
			return render(request, 'index.html', {'error': error})
		else:
			pos_json, neg_json = T.processtweets(count)
			if pos_json == 0 and neg_json == 0:
				error = 'Not enough tweets to judge personality'
				return render(request, 'index.html', {'error': error})
			elif neg_json == 0 and pos_json != 0:
				errors.append('Not enough negative tweets')
				Out1 = Output(pos_json)
				bigfive.append(Out1.bigfiveList)
				facets.append(Out1.facetsList)
			elif pos_json == 0 and neg_json != 0:
				errors.append('Not enough positive tweets')
				Out2 = Output(neg_json)
				bigfive.append(Out2.bigfiveList)
				facets.append(Out1.facetsList)
			else:
				Out1 = Output(pos_json)
				bigfive.append(Out1.bigfiveList)
				facets.append(Out1.facetsList)
				Out2 = Output(neg_json)
				bigfive.append(Out2.bigfiveList)
				facets.append(Out1.facetsList)
		print facets
		return render(request, 'index.html', {'errors': errors, 'bigfive': bigfive, 'facets': facets})
	else:
		error = "Please submit a search term"
		return render(request, 'index.html', {'error': error})
		
def myapp(request):
	errors = ["Not enough negative tweets"]
	bigfive = [{'xAxisLabels': ['Agreeableness', 'Conscientiousness', 'Extraversion', 'Emotional range', 'Openness'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'BigFive', 'xAxisTitle': 'Traits', 'yAxisValues': [0.41932266624920267, 0.7109600683461904, 0.14775173440020764, 0.10165046847928146, 0.7907209579918685]}, {'xAxisLabels': ['Agreeableness', 'Conscientiousness', 'Extraversion', 'Emotional range', 'Openness'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'BigFive', 'xAxisTitle': 'Traits', 'yAxisValues': [0.028935966018141825, 0.2786663444576054, 0.08149653347501289, 0.32567678163417163, 0.6864913755383365]}]
	facets = [{'Emotional range': {'xAxisLabels': ['Fiery', 'Prone to worry', 'Melancholy', 'Immoderation', 'Self-consciousness', 'Susceptible to stress'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.19511027470553158, 0.17668029632600646, 0.49615311853746863, 0.18955965113145373, 0.0963090942619217, 0.14972226444957087]}, 'Openness': {'xAxisLabels': ['Adventurousness', 'Artistic interests', 'Emotionality', 'Imagination', 'Intellect', 'Authority-challenging'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.9605730749458231, 0.22631757583165416, 0.061698526467978146, 0.9835884161638595, 0.9861197328712418, 0.9473445283121789]}, 'Extraversion': {'xAxisLabels': ['Activity level', 'Assertiveness', 'Cheerfulness', 'Excitement-seeking', 'Outgoing', 'Gregariousness'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.01804968805408629, 0.47165979677297576, 0.04208930059597496, 0.225358911587107, 0.07590228973972282, 0.07653291393614692]}, 'Agreeableness': {'xAxisLabels': ['Altruism', 'Cooperation', 'Modesty', 'Uncompromising', 'Sympathy', 'Trust'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.10045784713417218, 0.2715675083827832, 0.016719523935230497, 0.012154185407731274, 0.9277284497239447, 0.0328446881430627]}, 'Conscientiousness': {'xAxisLabels': ['Achievement striving', 'Cautiousness', 'Dutifulness', 'Orderliness', 'Self-discipline', 'Self-efficacy'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.6546508823880159, 0.38602356010710426, 0.07382423329213549, 0.00938658551659899, 0.4137013819069507, 0.6350176044423563]}}, {'Emotional range': {'xAxisLabels': ['Fiery', 'Prone to worry', 'Melancholy', 'Immoderation', 'Self-consciousness', 'Susceptible to stress'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.19511027470553158, 0.17668029632600646, 0.49615311853746863, 0.18955965113145373, 0.0963090942619217, 0.14972226444957087]}, 'Openness': {'xAxisLabels': ['Adventurousness', 'Artistic interests', 'Emotionality', 'Imagination', 'Intellect', 'Authority-challenging'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.9605730749458231, 0.22631757583165416, 0.061698526467978146, 0.9835884161638595, 0.9861197328712418, 0.9473445283121789]}, 'Extraversion': {'xAxisLabels': ['Activity level', 'Assertiveness', 'Cheerfulness', 'Excitement-seeking', 'Outgoing', 'Gregariousness'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.01804968805408629, 0.47165979677297576, 0.04208930059597496, 0.225358911587107, 0.07590228973972282, 0.07653291393614692]}, 'Agreeableness': {'xAxisLabels': ['Altruism', 'Cooperation', 'Modesty', 'Uncompromising', 'Sympathy', 'Trust'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.10045784713417218, 0.2715675083827832, 0.016719523935230497, 0.012154185407731274, 0.9277284497239447, 0.0328446881430627]}, 'Conscientiousness': {'xAxisLabels': ['Achievement striving', 'Cautiousness', 'Dutifulness', 'Orderliness', 'Self-discipline', 'Self-efficacy'], 'yAxisTitle': 'Average percentile', 'graphTitle': 'Facets', 'xAxisTitle': 'Facets', 'yAxisValues': [0.6546508823880159, 0.38602356010710426, 0.07382423329213549, 0.00938658551659899, 0.4137013819069507, 0.6350176044423563]}}]
	return render(request, 'new_index.html', {'errors': errors, 'bigfive': bigfive, 'facets': facets})
