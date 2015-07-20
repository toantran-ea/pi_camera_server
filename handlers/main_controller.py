import webapp2
from webapp2_extras import json


class MainController(webapp2.RequestHandler):
	def get(self):
		response = {"message": "main controller"}
		self.response.write(json.encode(response))
	