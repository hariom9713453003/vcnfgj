from flask import Flask, jsonify, request
from time import gmtime
import time
import flask
import subprocess
import sys, os
import requests
import random
import urllib
import cv2
import pytesseract

app = Flask(__name__)

global expire_time
global count
global expire_time1
global count1
global expire_time11
global count11
real_time = int(time.time())
expire_time = real_time + 60
count = 0
expire_time1 = real_time + 60
count1 = 0
expire_time11 = real_time + 60
count11 = 0

@app.route("/getCaptcha")
def get_cap():
    global img_var
    global expire_time
    global count
    real_time = int(time.time())
    if real_time > expire_time or count == 0:
        val = random.randint(100000,999999)
        age = time.strftime("%a %b %d %Y %I:%M:%S %Z", time.gmtime()).replace(" ","%20")
        stnd = "+0530"# (India Standard Time)"
        url = "https://electoralsearch.in/Home/GetCaptcha?image=true&id="+age+stnd+""
        header = "Cookie: __RequestVerificationToken=tysOL3OVluTVex7aQKmWLhAGhlrg1-0klx3YdekKrqBPgOjHqVq1oZpDkavwsvcfFRmRZ1hjw9jufUtCsNKPN41d-CH8jfw8AsnVK6tpWjo1; ServerAffinity=53ce6a2839080d44a20632f7d508af421d55ec1a84537bf06c26103e24c3507b; runOnce=true; electoralSearchId=pbt5evaxm1yxa1bu2kylgh53; s=; _ga=GA1.2.254212312.1589213368; _gid=GA1.2.569711653.1589213368"
        cmd = f'curl --output "/home/skprxprb/public_html/Captcha1/captcha'+str(val)+'.jpeg" -H "'+header+'" "'+url+'"'
        print(cmd)
        os.system(cmd)
        count = 1
        expire_time = real_time + 90
        img_var = "Captcha1/captcha"+str(val)+".jpeg"
        #print("/home/skprxprb/public_html/captcha"+str(val)+".jpeg")
        return img_var
    else:
        return img_var

@app.route("/getaadhCaptcha")
def get_aadh_cap():
    global img_var1
    global expire_time1
    global count1
    real_time = int(time.time())
    if real_time > expire_time1 or count1 == 0:
        val = "12345"
        url = "http://103.94.204.46:8080/GenerateAadharCaptcha.ashx"
        res = requests.get("http://skprints.online/code.php")
        #print(res.text)
        header = "Cookie: "+res.text
        #header = "Cookie: __RequestVerificationToken=tysOL3OVluTVex7aQKmWLhAGhlrg1-0klx3YdekKrqBPgOjHqVq1oZpDkavwsvcfFRmRZ1hjw9jufUtCsNKPN41d-CH8jfw8AsnVK6tpWjo1; ServerAffinity=53ce6a2839080d44a20632f7d508af421d55ec1a84537bf06c26103e24c3507b; runOnce=true; electoralSearchId=pbt5evaxm1yxa1bu2kylgh53; s=; _ga=GA1.2.254212312.1589213368; _gid=GA1.2.569711653.1589213368"
        cmd = f'curl --output "/home/skprxprb/public_html/Captcha1/aadhar/aadharcaptcha'+str(val)+'.jpeg" -H "'+header+'" "'+url+'"'
        #print(cmd)
        os.system(cmd)
        count1 = 1
        expire_time1 = real_time + 10
        img_var1 = "Captcha/aadhar/aadharcaptcha"+str(val)+".jpeg"

        """ Image Proccessing part is done here """ 
        img = cv2.imread("/home/skprxprb/public_html/"+img_var1+"")

        text = pytesseract.image_to_string(img)
        #print("/home/skprxprb/public_html/captcha"+str(val)+".jpeg")
        fp = open("/home/skprxprb/public_html/Captcha1/aadhar/aadharcaptcha.text","w+")
        fp.write(text.replace(" ", ""))
        fp.close()
        return text.replace(" ","")
    else:
        img = cv2.imread("/home/skprxprb/public_html/Captcha1/aadhar/aadharcaptcha12345.jpeg")

        text = pytesseract.image_to_string(img)
        return text.replace(" ","")

@app.route("/getaadhCaptcha1")
def get_aadh_cap1():
    global img_var11
    global expire_time11
    global count11
    real_time = int(time.time())
    if real_time > expire_time11 or count11 == 0:
        val = "123451"
        #url = "http://103.94.204.46:8080/GenerateAadharCaptcha.ashx"
        url = "http://kamgarsetu.mp.gov.in/GenerateAadharCaptcha.ashx"
        res = requests.get("http://skprints.online/code1.php")
        #print(res.text)
        header = "Cookie: "+res.text
        #print(header)
        #header = "Cookie: __RequestVerificationToken=tysOL3OVluTVex7aQKmWLhAGhlrg1-0klx3YdekKrqBPgOjHqVq1oZpDkavwsvcfFRmRZ1hjw9jufUtCsNKPN41d-CH8jfw8AsnVK6tpWjo1; ServerAffinity=53ce6a2839080d44a20632f7d508af421d55ec1a84537bf06c26103e24c3507b; runOnce=true; electoralSearchId=pbt5evaxm1yxa1bu2kylgh53; s=; _ga=GA1.2.254212312.1589213368; _gid=GA1.2.569711653.1589213368"
        cmd = f'curl --output "/home/skprxprb/public_html/Captcha1/aadhar/aadharcaptcha'+str(val)+'.jpeg" -H "'+header+'" "'+url+'"'
        #print(cmd)
        os.system(cmd)
        count11 = 1
        expire_time11 = real_time + 10
        img_var11 = "Captcha1/aadhar/aadharcaptcha"+str(val)+".jpeg"

        #"" Image Proccessing part is done here ""
        img = cv2.imread("/home/skprxprb/public_html/"+img_var11+"")
        #print(img)
        text = pytesseract.image_to_string(img)
        #print("/home/skprxprb/public_html/captcha"+str(val)+".jpeg")
        fp = open("/home/skprxprb/public_html/Captcha1/aadhar/aadharcaptcha1.text","w+")
        fp.write(text.replace(" ", ""))
        fp.close()
        return text.replace(" ","")
    else:
        img = cv2.imread("/home/skprxprb/public_html/Captcha1/aadhar/aadharcaptcha123451.jpeg")

        text = pytesseract.image_to_string(img)
        return text.replace(" ","")

@app.route("/getData")
def get_voter_data():
    Epic_no = request.args.get("epic_no")
    captcha = request.args.get("captcha")
    #print(Epic_no)
    #print(captcha)
    url = f"https://electoralsearch.in/Home/searchVoter?epic_no={Epic_no}&page_no=1&results_per_page=10&reureureired=ca3ac2c8-4676-48eb-9129-4cdce3adf6ea&search_type=epic&txtCaptcha={captcha}"
    header = {"Cookie": "__RequestVerificationToken=tysOL3OVluTVex7aQKmWLhAGhlrg1-0klx3YdekKrqBPgOjHqVq1oZpDkavwsvcfFRmRZ1hjw9jufUtCsNKPN41d-CH8jfw8AsnVK6tpWjo1; ServerAffinity=53ce6a2839080d44a20632f7d508af421d55ec1a84537bf06c26103e24c3507b; runOnce=true; electoralSearchId=pbt5evaxm1yxa1bu2kylgh53; s=; _ga=GA1.2.254212312.1589213368; _gid=GA1.2.569711653.1589213368"}
    res = requests.get(url, headers=header)
    #print(res.text)
    return jsonify(res.text)


if __name__ == "__main__":
    app.run("103.83.81.250",2054, debug=True)
