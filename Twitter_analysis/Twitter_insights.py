import requests
import json
from Credentials import Credentials
from Personality import Personality as P
from Language import Language as Lang

# -*- coding: utf-8 -*-

size = 250

class Twitter_insights:
	def __init__(self):
		self.base_url = "https://cdeservice.mybluemix.net:443/api/v1/messages/"
		self.T = Credentials("twitterinsights")
		
	def getcount(self, query):
		self.query = query
		url = self.base_url + "count?q=" + self.query
		data = self.getdata(url)
		count = data["search"]["results"]
		if count < size:
			return (0, 0)
		else:
			return (1, count)
		
	def processtweets(self, count):
		url = self.base_url + "search?q=" + self.query
		startcount = count-size+1
		new_url = url + '&from=' + str(startcount) + '&size=' + str(size)
		data = self.getdata(new_url)
		tweets = data["tweets"]
		pos_text = ''
		neg_text = ''
		for tweet in tweets:
			try:
				sentiment = tweet["cde"]["content"]["sentiment"]["polarity"]
				temp_text = tweet["message"]["body"]
			except:
				sentiment = "NEUTRAL"
			if sentiment == "POSITIVE":
				temp_text = Lang().en(temp_text)
				pos_text += temp_text
			elif sentiment == "NEGATIVE":
				temp_text = Lang().en(temp_text)
				neg_text += temp_text
		pos_text = pos_text.replace("\n",' ')
		neg_text = neg_text.replace("\n",' ')
		if len(pos_text.split(' ')) > 200:
			pos_json = P().check(pos_text,1)
		else:
			pos_json = 0
		if len(neg_text.split(' ')) > 200:
			neg_json = P().check(neg_text,2)
		else:
			neg_json = 0
		return (pos_json, neg_json)

	def getdata(self, url):
		response = requests.get(url, auth=(self.T.username, self.T.password))
		data = response.json()
		return data
