import re
from datetime import date

from bottle import post, request

# Простой паттерн формата email (латиница, типичная структура local@domain.tld)
_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


@post("/home")
def my_form():
    quest = (request.forms.get("QUEST") or "").strip()
    mail = (request.forms.get("ADRESS") or "").strip()
    username = (request.forms.get("USERNAME") or "").strip()

    if not quest or not mail or not username:
        print("question:", quest)
        print("email:", mail)
        print("username:", username)
        return "Please fill in all fields: question, name, and email."

    if not _EMAIL_RE.match(mail):
        print("email:", mail)
        return "Invalid email format. Please enter a valid address."

    access_date = date.today().strftime("%Y-%m-%d")
    print("success, date:", access_date)
    return (
        "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s"
        % (username, mail, access_date)
    )
