from flask import Flask, render_template, request
import requests

app = Flask(__name__)

items = [
    {"id": 1, "title": "instagram", "website": "https://www.instagram.com"},
    {"id": 2, "title": "youtube", "website": "https://www.youtube.com"},
    {"id": 3, "title": "twitter", "website": "https://www.twitter.com"},
    {"id": 4, "title": "facebook", "website": "https://www.facebook.com"},
    {"id": 5, "title": "twitch", "website": "https://www.twitch.com"},
    {"id": 6, "title": "reddit", "website": "https://www.reddit.com"},
    {"id": 7, "title": "pinterest", "website": "https://www.pinterest.com"},
    {"id": 8, "title": "tumblr", "website": "https://www.youtube.com"},
    {"id": 9, "title": "linkedin", "website": "https://www.linkedin.com"},
]

@app.route('/', methods=['GET', 'POST'])
def check_websites():
    if request.method == 'POST':
        username = request.form['username']
        handle_set_url(username)
    return render_template('index.html', items=items)

def handle_set_url(url):
    for item in items:
        a = item['website'] + "/" + url
        check_website_exists(a, item['id'] - 1)

def check_website_exists(website_url, index):
    print(website_url)
    try:
        response = requests.head(website_url)
        if response.ok:
            set_website_exists(index, "❌ Unavailable")
        else:
            set_website_exists(index, "✅ Available")
    except requests.exceptions.RequestException as error:
        set_website_exists(index, "✅ Available")

def set_website_exists(index, status):
    items[index]['websiteExists'] = status

if __name__ == '__main__':
    app.run(debug=True)
