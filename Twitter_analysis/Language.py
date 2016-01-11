import requests
from Credentials import Credentials

class Language:
	def __init__(self):
		self.LI = Credentials("language_translation")
	
	def en(self,tweet_text):
		self.tweet_text = tweet_text
		url = self.LI.url + "/v2/identify?text=" + self.tweet_text
		response = requests.get(url, auth=(self.LI.username, self.LI.password))
		lang = response.text
		if lang[0] == 'es':
			tweet_text = self.translate("es")
		elif lang[0] == 'pt':
			tweet_text = self.translate("pt")
		elif lang[0] == 'ar':
			tweet_text = self.translate("ar")
		elif lang[0] == 'fr':
			tweet_text = self.translate("fr")
		
		return tweet_text
			
	def translate(self, lang):
		url = self.LI.url + "/v2/translate?source=" + lang + '&target=en&text=' + self.tweet_text
		response = requests.get(url, auth=(self.LI.username, self.LI.password))
		trans_text = response.text
		return trans_text
