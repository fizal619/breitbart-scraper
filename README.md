# BREITBART SCRAPER

Fun little hack to attempt scraping the first 20 results from breitbart. Not sure if this will get my heroku taken down _(hopefully not)_.
Not disclosing the url here, send me an email or slack me if you want access to the api or deploy it on your own heroku account!

## Deploying

Make sure you have the [heroku cli tools](https://devcenter.heroku.com/articles/heroku-cli) installed and you're logged in. 

* Clone this repo down. 
* `cd` into the folder. 
* `heroku create`
* `git push heroku master`
* `heroku ps`

All should be good. 

## Editing

If you'd like to work on this all the dependencies are in the `requirements.txt` file. I believe all you do is `pip install -r requirements.txt` and it should autoinstall all of them. 

## Usage

Once you got it deployed and ready just send a `GET` request to `http://<app-name>.herokuapp.com?s=<something>`. And it responds with JSON. If it doesn't find any articles it responds with the HTML of whatever page it encountered to help troubleshooting. 

```
[
	{
		"content": "On Monday evening, Kansas Republican Mike Pompeo was confirmed as the next director of the C.I.A. by....",
		"link": "http://www.breitbart.com/big-government/2017/01/23/despite-democrat-obstruction-u-s-senate-confirms-mike-pompeo-as-next-director-of-cia/",
		"title": "Despite Democrat Obstruction U.S. Senate Confirms Mike Pompeo as Next Director of CIA"
	}
]
``` 


> Happy Hacking! 
