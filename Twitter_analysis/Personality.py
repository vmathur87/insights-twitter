import httplib2 as http
from Credentials import Credentials

# -*- coding: utf-8 -*-

class Personality:
	def __init__(self):
		self.P = Credentials("personality_insights")
		
	def check(self, tweet_text, flag):
		headers = {
        'Accept': 'application/json',
        'Content-Type': 'text/plain; charset=UTF-8'
        }
		method = 'POST'
		body = tweet_text.encode('ascii', 'ignore')
		h = http.Http()
		h.add_credentials(self.P.username, self.P.password)
		url = self.P.url + "/v2/profile"
		response, content = h.request(
				url,
				method,
				body,
				headers)
		return content
