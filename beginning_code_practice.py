import smtplib
import datetime as dt
import random



now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    EMAIL_FROM = "stoyan.py@gmail.com"
    PASSWORD = "**********"

    EMAIL_TO = "stoyan.py@yahoo.com"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=EMAIL_FROM, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL_FROM,
                        to_addrs=EMAIL_TO,
                        msg=f"Subject:A bit of motivation\n\n{quote}"
    )
    connection.close()
