import requests
from flask import Flask, render_template

BLOG_URL = "https://api.npoint.io/92d0ac6f5b3f9c756882"
app = Flask(__name__)

@app.route('/')
def get_blog():
    resp = requests.get(BLOG_URL)
    all_posts = resp.json()
    return render_template('index.html', posts=all_posts)

@app.route('/post/<int:post_id>')
def find_post(post_id):
    resp = requests.get(BLOG_URL)
    all_posts = resp.json()
    if post_id == 1:
        return render_template('post1.html', posts=all_posts)
    if post_id == 2:
        return render_template('post2.html', posts=all_posts)
    if post_id == 3:
        return render_template('post3.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)