import web
import json
import re
from tldr import tldrParser

urls = (
		'/tldr','index',
		'/tldr/tldrs/(\d*)','tldrs'
)

app = web.application(urls,globals())

class index:
	def GET(self):
		return "Welcome to tldr app"

class tldrs:

	def GET (self,nos):
		if not nos:
			nos = 10

		redditTldrParser = tldrParser();

		listOfTldrs = redditTldrParser.getTldrs(nos)

		a = []
		for tldr in listOfTldrs:
			tldrParts = re.split("\|",tldr)
			o = {}
			o['text']=tldrParts[0]
			o['link']=tldrParts[1]
			a.append(o)

		return json.dumps(a)

if __name__ == "__main__":
	app.run()
