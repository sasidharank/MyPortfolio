from django.shortcuts import render
from .models import contact, visitors, visitormails
import requests, json, yagmail



def index(req):
    if req.method == "POST":
        fname = req.POST.get('firstname')
        lname = req.POST.get('lastname')
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + fname + '&lastName=' + lname + '')
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        sending = {'jokes': joke}
        c = visitors(first_name=fname, last_name=lname)
        c.save()

        return render(req, 'mysite/index.html', sending)

    else:
        fname = 'Sasi'
        lname = 'dharan'
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + fname + '&lastName=' + lname + '')
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        sending = {'jokes': joke}
        return render(req, 'mysite/index.html', sending)


def portfolio(req):
    return render(req, 'mysite/portfolio.html')


def Contact(req):
    if req.method == "POST":

        email = req.POST.get('email')
        subject = req.POST.get('subject')
        message = req.POST.get('message')

        c = contact(email=email, subject=subject, message=message)
        c.save()

        return render(req, 'mysite/thank.html')
    else:
        return render(req, 'mysite/contact.html')


def automail(req):
    return render(req, 'mysite/automail.html')


def sendmail(req):
    if req.method == "POST":
        to = req.POST.get('visitoremail')
        yagmail.register('yours@gmail.com', 'yourpassword')
        yag = yagmail.SMTP('reachsasidharank@gmail.com')
        subject = 'Automated🤖Mail'

        contents = ["<h1>👋Hello there!</h1><p>#You can write me here#</p>http://tiny.cc/allaboutsasi/contact"]
        yag.send(to=to, subject=subject, contents=contents)
        c = visitormails(email=to)
        c.save()

        return render(req, 'mysite/automailthank.html')

    else:
        return render(req, 'mysite/automail.html')
