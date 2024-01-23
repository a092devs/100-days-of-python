import requests
import smtplib
from os import environ
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv("config.env", override=True)

EMAIL = environ.get("FROM_EMAIL")
PASSWORD = environ.get("FROM_PASSWORD")
TO_EMAIL = environ.get("TO_EMAIL")

blog_url = "https://api.npoint.io/f62984d9b3959809e56a"
blog_resp = requests.get(blog_url)
all_posts = blog_resp.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/index.html")
def index():
    return render_template("index.html", posts=all_posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/post/<int:p_id>")
def post(p_id):
    return render_template("post.html", post=all_posts[int(p_id) - 1])


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="EMAIL", password="PASSWORD")
            connection.sendmail(
                from_addr="EMAIL",
                to_addrs="EMAIL",
                msg=f"Subject:New Message Received!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:p_id>")
def get_post(p_id):
    return render_template("post.html", post=all_posts[int(p_id) - 1])


if __name__ == "__main__":
    app.run(debug=True)
