from setuptools import setup

setup(
		name = "tldr",
		version = "0.0.1",
		description = "A simple parser to parse /r/tldr",
		author_email = "username: shrayasr, domain: gmail.com",
		url = "https://github.com/shrayas/reddit-tldr",
		install_requires = [
			"web",
			"praw"
		]
)
