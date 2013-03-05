import praw
import re

class tldrParser:

	def getTldrs(self,nos):

		print "Fetching "+str(nos)+" tldrs"

		r = praw.Reddit(user_agent='tldr links fetcher by /u/shrayas')
		submissions = r.get_subreddit('tldr')

		if nos == -1:
			nos = None

		tldrLinks = []

		count = 1
		for submission in submissions.get_hot(limit=int(nos)):
			
			print "Processing tldr "+str(count)+" of "+str(nos)
			title = submission.title
			text = submission.selftext

			linkTexts = re.findall("\[([^]]*)\]\ *\(",text);
			links = re.findall("\]\ *\(([^)]*)\)",text);

			tempTldrLinks = [(lt+"|"+l) for lt,l in zip(linkTexts,links)]

			tldrLinks.extend(tempTldrLinks)

			print "no. of links = "+str(len(tldrLinks))

			if count == nos:
				break

			count = count + 1

		print "Fetched "+str(len(tldrLinks))+" number of links"
		return tldrLinks

'''
if __name__ == "__main__":
	
	myParser = tldrParser();
	myParser.getTldrs(-1);
'''
