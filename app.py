from flask import Flask
from flask import jsonify
from flask import request
from bs4 import BeautifulSoup
from newspaper import Article

import os
import requests


# HN=newspaper.build('https://news.ycombinator.com/')

app = Flask(__name__)

@app.route("/")
def news():
	freshNews = []
	search = request.args.get('s')
	r  = requests.get("http://www.breitbart.com?s=" + request.args.get('s'))
	data = r.text
	# print(data)
	soup = BeautifulSoup(data)
	articles = soup.find_all('h2', {'class': 'title'})
	for article in articles:
		if len(freshNews) == 20:
			return jsonify(freshNews)
		try:
			link = article.find('a')
			print(link.get("href"))
			item = Article("http://www.breitbart.com" + link.get("href"))
			item.download()
			item.parse()
			freshNews.append({
				"title": item.title,
				"content": item.text,
				"link": "http://www.breitbart.com" + link.get("href")
				})


		except Exception as e:
			4+4
			print(">>>>>>>>> ERROR?!")
	print("nope...")
	return data



if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
