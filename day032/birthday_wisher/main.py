import smtplib, random
import datetime as dt
import pandas as pd

email = "my_email_was_here"
password = "my_pass_was_here"

now = dt.datetime.now()
day = now.day
month = now.month
name = ""

df = pd.read_csv("birthdays.csv")
bday_dict = df.to_dict(orient="records")

for bday in bday_dict:
    if bday["month"] == month and bday["day"] == day:
        name = bday["name"]
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            mail = letter.read()
            mail = mail.replace("[NAME]", name)
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(email, password)
                connection.sendmail(from_addr=email,
                                    to_addrs=f"{bday['email']}",
                                    msg=f"Subject:HAPPY BIRTHDAY\n\n{mail}")