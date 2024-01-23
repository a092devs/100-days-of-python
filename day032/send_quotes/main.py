import datetime as dt
import smtplib
import random

email = "my_email_was_here"
password = "my_pass_was_here"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    # print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs="a092devs@email.com",
            msg=f"Subject:Wednesday Motivation\n\n{quote}",
        )
