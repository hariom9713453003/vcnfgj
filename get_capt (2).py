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
from requests.structures import CaseInsensitiveDict

app = Flask(__name__)

global expire_time
global count
global expire_time1
global count1
global expire_time11
global count11
real_time = int(time.time())
expire_time = real_time + 90
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
        print(age)
        stnd = "+0530"# (India Standard Time)"
        url = "https://electoralsearch.in/Home/GetCaptcha?image=true&id="+age+stnd+""
        #header = "Cookie: __RequestVerificationToken=tysOL3OVluTVex7aQKmWLhAGhlrg1-0klx3YdekKrqBPgOjHqVq1oZpDkavwsvcfFRmRZ1hjw9jufUtCsNKPN41d-CH8jfw8AsnVK6tpWjo1; ServerAffinity=53ce6a2839080d44a20632f7d508af421d55ec1a84537bf06c26103e24c3507b; runOnce=true; electoralSearchId=pbt5evaxm1yxa1bu2kylgh53; s=; _ga=GA1.2.254212312.1589213368; _gid=GA1.2.569711653.1589213368"
        #cmd = f'curl --output "/home/skprxprb/public_html/Captcha/captcha'+str(val)+'.jpeg" -H "'+header+'" -H "'+h1+'"  -H "'+h2+'"  -H "'+h3+'" -H "'+h5+'" -H "'+h6+'" -H "'+h7+'" -H "'+h8+'" -H "'+h9+'" -H "'+h10+'" -H "'+h11+'" -H "'+h12+'" -H "'+h13+'" -H "'+h14+'" "'+url+'"'
        cmd = f'curl -k -X GET "{url}"-H "Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8" -H "Accept-Encoding: gzip, deflate, br" -H "Accept-Language: en-GB,en-US;q=0.9,en;q=0.8" -H "Connection: keep-alive" -H "Cookie: Electoral=456c6563746f72616c5365617263682d7365727665722d32; electoralSearchId=lo0woadtmaqbkptlj41fbm1e; Electoral=456c6563746f72616c5365617263682d7365727665722d32; runOnce=true; __RequestVerificationToken=c8aviTogu3_rQ432voma0tBV6dE6PP3ab6VKQ5joeef-YQEGfIA244CFB1I-JudbMEzLhlZEqACTr7kwhzIP877YZMwReB5noh5b57fJXrw1" -H "Host: electoralsearch.in" -H "Referer: https://electoralsearch.in/" -H "sec-ch-ua-mobile: ?0" -H "Sec-Fetch-Dest: image" -H "Sec-Fetch-Mode: no-cors" -H "Sec-Fetch-Site: same-origin" -o "/home/skprxprb/public_html/Captcha/captcha{val}.jpeg"'
        print(cmd)
        os.system(cmd)
        count = 1
        expire_time = real_time +90
        img_var = "Captcha/captcha"+str(val)+".jpeg"
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
        res = requests.get("http://skprints.xyz/codenew.php")
        #print(res.text)
        header = "Cookie: "+res.text
        #header = "Cookie: __RequestVerificationToken=tysOL3OVluTVex7aQKmWLhAGhlrg1-0klx3YdekKrqBPgOjHqVq1oZpDkavwsvcfFRmRZ1hjw9jufUtCsNKPN41d-CH8jfw8AsnVK6tpWjo1; ServerAffinity=53ce6a2839080d44a20632f7d508af421d55ec1a84537bf06c26103e24c3507b; runOnce=true; electoralSearchId=pbt5evaxm1yxa1bu2kylgh53; s=; _ga=GA1.2.254212312.1589213368; _gid=GA1.2.569711653.1589213368"
        cmd = f'curl --output "/home/skprxprb/public_html/Captcha/aadhar/aadharcaptcha'+str(val)+'.jpeg" -H "'+header+'" "'+url+'"'
        #print(cmd)
        os.system(cmd)
        count1 = 1
        expire_time1 = real_time + 10
        img_var1 = "Captcha/aadhar/aadharcaptcha"+str(val)+".jpeg"

        """ Image Proccessing part is done here """ 
        img = cv2.imread("/home/skprxprb/public_html/"+img_var1+"")

        text = pytesseract.image_to_string(img)
        #print("/home/skprxprb/public_html/captcha"+str(val)+".jpeg")
        fp = open("/home/skprxprb/public_html/Captcha/aadhar/aadharcaptcha.text","w+")
        fp.write(text.replace(" ", ""))
        fp.close()
        return text.replace(" ","")
    else:
        img = cv2.imread("/home/skprxprb/public_html/Captcha/aadhar/aadharcaptcha12345.jpeg")

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
        res = requests.get("http://skprints.xyz/code1.php")
        #print(res.text)
        header = "Cookie: "+res.text
        #print(header)
        #header = "Cookie: __RequestVerificationToken=tysOL3OVluTVex7aQKmWLhAGhlrg1-0klx3YdekKrqBPgOjHqVq1oZpDkavwsvcfFRmRZ1hjw9jufUtCsNKPN41d-CH8jfw8AsnVK6tpWjo1; ServerAffinity=53ce6a2839080d44a20632f7d508af421d55ec1a84537bf06c26103e24c3507b; runOnce=true; electoralSearchId=pbt5evaxm1yxa1bu2kylgh53; s=; _ga=GA1.2.254212312.1589213368; _gid=GA1.2.569711653.1589213368"
        cmd = f'curl --output "/home/skprxprb/public_html/Captcha/aadhar/aadharcaptcha'+str(val)+'.jpeg" -H "'+header+'" "'+url+'"'
        #print(cmd)
        os.system(cmd)
        count11 = 1
        expire_time11 = real_time + 10
        img_var11 = "Captcha/aadhar/aadharcaptcha"+str(val)+".jpeg"

        #"" Image Proccessing part is done here ""
        img = cv2.imread("/home/skprxprb/public_html/"+img_var11+"")
        #print(img)
        text = pytesseract.image_to_string(img)
        #print("/home/skprxprb/public_html/captcha"+str(val)+".jpeg")
        fp = open("/home/skprxprb/public_html/Captcha/aadhar/aadharcaptcha1.text","w+")
        fp.write(text.replace(" ", ""))
        fp.close()
        return text.replace(" ","")
    else:
        img = cv2.imread("/home/skprxprb/public_html/Captcha/aadhar/aadharcaptcha123451.jpeg")

        text = pytesseract.image_to_string(img)
        return text.replace(" ","")

@app.route("/getData")
def get_voter_data():
    Epic_no = request.args.get("epic_no")
    captcha = request.args.get("captcha")
    #print(Epic_no)
    #print(captcha)
    url = f"https://electoralsearch.in/Home/searchVoter?epic_no={Epic_no}&page_no=1&results_per_page=10&reureureired=ca3ac2c8-4676-48eb-9129-4cdce3adf6ea&search_type=epic&txtCaptcha={captcha}"
    #header = {"Cookie": "__RequestVerificationToken=tysOL3OVluTVex7aQKmWLhAGhlrg1-0klx3YdekKrqBPgOjHqVq1oZpDkavwsvcfFRmRZ1hjw9jufUtCsNKPN41d-CH8jfw8AsnVK6tpWjo1; ServerAffinity=53ce6a2839080d44a20632f7d508af421d55ec1a84537bf06c26103e24c3507b; runOnce=true; electoralSearchId=pbt5evaxm1yxa1bu2kylgh53; s=; _ga=GA1.2.254212312.1589213368; _gid=GA1.2.569711653.1589213368"}
    headers = CaseInsensitiveDict()
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
    headers["Cache-Control"] = "max-age=0"
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = "Electoral=456c6563746f72616c5365617263682d7365727665722d32; electoralSearchId=lo0woadtmaqbkptlj41fbm1e; Electoral=456c6563746f72616c5365617263682d7365727665722d32; runOnce=true; __RequestVerificationToken=c8aviTogu3_rQ432voma0tBV6dE6PP3ab6VKQ5joeef-YQEGfIA244CFB1I-JudbMEzLhlZEqACTr7kwhzIP877YZMwReB5noh5b57fJXrw1; s="
    headers["Host"] = "electoralsearch.in"
    headers["sec-ch-ua-mobile"] = "?0"
    headers["Sec-Fetch-Dest"] = "document"
    headers["Sec-Fetch-Mode"] = "navigate"
    headers["Sec-Fetch-Site"] = "none"
    headers["Sec-Fetch-User"] = "?1"
    headers["Upgrade-Insecure-Requests"] = "1"
    res = requests.get(url, headers=headers)
    #print(res.text)
    return jsonify(res.text)


if __name__ == "__main__":
    #app.run("ns1.skprints.online",2053, debug=True)
    app.run("103.83.81.250",2053, debug=True)
