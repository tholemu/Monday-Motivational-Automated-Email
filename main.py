import smtplib
import datetime as dt
import random

MY_EMAIL = "bowlers@yahoo.com"
MY_PASSWORD = "xxxxxxxxx"

now = dt.datetime.now()
weekday = now.weekday()
#create if/then statement to verify it is Monday, if it is then perform the code
if weekday == 1:
    with open("quotes.txt") as quote_file:
      all_quotes = quote_file.readlines()
      quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
      connection.starttls()
      connection.login(MY_EMAIL, MY_PASSWORD)
      connection.sendmail(
          from_addr=MY_EMAIL, 
          to_addr=MY_EMAIL, 
          msg=f"Subject: Monday Motivation\n\n {quote}"
      )
