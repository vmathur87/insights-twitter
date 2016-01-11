import json
import os

class Credentials:
	def __init__(self, servicename):
		self.services = os.getenv("VCAP_SERVICES")
		self.data = json.loads(self.services)
		self.servicename = servicename
		self.url = self.data[self.servicename][0]["credentials"]["url"]
		self.username = self.data[self.servicename][0]["credentials"]["username"]
		self.password = self.data[self.servicename][0]["credentials"]["password"]
