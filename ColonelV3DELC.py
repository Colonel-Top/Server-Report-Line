﻿# -*- coding: utf-8 -*-
import time
import psutil
import MySQLdb
import random
import string
import random
import os
import schedule
import sys
import os.path
import socket
from urllib2 import urlopen, URLError, HTTPError
socket.setdefaulttimeout( 23 )


from random import randint
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
print ("Running")
gdate = ""
now = datetime.now()

    #line_bot_api.push_message(group, TextSendMessage(text= "***********************")
    #line_bot_api.push_message(group, TextSendMessage(text= "Messenger API Connected")
    #print ("Messenger API Connected")
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
from linebot.models import StickerSendMessage
from linebot.models import TemplateSendMessage
from linebot.exceptions import LineBotApiError

#line_bot_api = LineBotApi('Q8BjDP5iRdj+FprSJXxyDk95z358K0355D7rTRTBuubd0z+0XFTanFHD+yPyR7uAIOKtdpbtv99HxxSgm49QEOxmYI/PrA5Hlt3l4TYVVoxPYPYRS4G/7eVMr8YldmlybqUabhXknXephfGwzB1GXgdB04t89/1O/w1cDnyilFU=')

#line_bot_api.push_message(associateid, TextSendMessage(text="การตัดดอกเบี้ยเสร็จเรียบร้อยค่ะ"))
#line_bot_api.push_message(group, TextSendMessage(text= "Google API Connected")
#print ("Google API Connected")
#line_bot_api.push_message(group, TextSendMessage(text= 'Debug:: Time runner begun')
# Login with your Google account
strws = ""
groups = ""
line_bot_api = LineBotApi('9+TH/yJxGzfQ/ZdMlMrmar3RzPjen29VHEw6t6ErubCB7eirHnU9GIyyA+FtU7OIug8tyiGNHpRrub3zg46yLMDPBYEcJyM1kApSNScPJX0KseMvh681J/NS5Ef+1uBpZRi3FBMtNGy17NX/fjxJbAdB04t89/1O/w1cDnyilFU=')
morning = ['Good morning','Good Morning','อรุณสวัสดิ์ค่ะ','สวัสดีตอนเช้าจ้าา','อรุณสวัสดิ์ยามเช้าครับ','อรุณสวัสดิ์วันใหม่ครับ','อรุณสวัสดิ์ครับ','Good morning']
afternoon = ['Good afternoon','Good Afternoon','สวัสดีตอนบ่ายครับ','Good afternoon','Good afternoon ครับ']
night = ['Good Evening','Good evening','สวัสดีตอนเย็นครับ']


colonel = 'Ufb00beda08083bcf402fbd2160b75574'

bot_status = 0
bot_mode = 0
preperform = 'Ca410257ec75147e5e6c78265f2b8616d'
def sendmsg(string,who):
    try:
        text_message = TextSendMessage(text=string)
        line_bot_api.push_message(who, text_message)
    except Exception as e:
        print (e)
def sendpic(imagetosend,who):
    try:
        #imagetosend = input("Image URL: ")
        image_message = ImageSendMessage(
            original_content_url=imagetosend,
            preview_image_url=imagetosend
        )
        line_bot_api.push_message(who, image_message)
    except Exception as e :
        print(e)
def sendsticker(ids,who):
    try:
        #print("Sticker Option")    
        '''print("1.Sleep\
                \n2.Smile Wink Yes\
                \n3.Oh Shit Face\
                \n4.Cutie Care me plz\
                \n5.Im so beautiful\
                \n6.Angry Red Face\
                \n7.You dead Sure\
                \n8.Ops Aghh\
                \n9.Crying Alone\
                \n10.I will got you hehe\
                \n11.Singing\
                \n12.Motivated\
                \n13.Cool Yes\
                \n14.Oh My god good as crying\
                \n15.Bare Bare\
                \n16.Crying hand on face\
                \n17.Hmm ? ! What u say ?")'''
        sticker_message = StickerSendMessage(
                package_id='1',
                sticker_id=ids
        )
        line_bot_api.push_message(who, sticker_message)
    except Exception as e:
        print(e)
def sendcurrenttime(who):
    textnow = datetime.now().strftime('%d-%m-%Y')
    textnow = "Today Date: "+textnow
    sendmsg(textnow,who)
    
def sendsecurity(who):
    #Send Date
    textnow = datetime.now().strftime('%d-%m-%Y')
    stringsend = "Colonel Technology V3 (DELC) Report Date: " + textnow
    #sendmsg(stringsend,who)
    
    #CHeck CPU Percentage
    p = psutil.Process(os.getpid())
    percent = round(psutil.cpu_percent(), 3)
    strpercent = float(percent)
    if(strpercent <=50):
        stringsend = stringsend + "\n\n" +"CPU "+str(strpercent) + "% Status: OK"
    elif(strpercent <= 70):
        stringsend = stringsend + "\n\n" + "CPU "+str(strpercent) + "% Status: HEAVY"
    elif(strpercent <= 85):
        stringsend = stringsend + "\n\n" + "CPU "+str(strpercent) + "% Status: WARNING"
    elif(strpercent <= 100):
        stringsend = stringsend + "\n\n" + "CPU "+str(strpercent) + "% Status: CRITICAL"
    #sendmsg(stringsend,who)
    
    #Check Disk Partition
    amount = 0
    for p in psutil.disk_partitions():
        u = psutil.disk_usage(p.mountpoint)
        perc = u.percent
        f = perc/100.0
        state = "OK"
        warning = 0.9
        critical = 0.95
        if f > warning: state="WARNING"
        if f > critical: state="CRITICAL"
        stringsend = stringsend + "\n\n" + "Disk"+ str(amount)+" "+str(f*100)+"%"+ " : "+state
        #sendmsg(stringsend,who)
    #Check Ram

    p = psutil.Process(os.getpid())
    memoryUse = psutil.virtual_memory().total / (1024.0 ** 2)
    mem = psutil.virtual_memory().percent
    state = "OK"
    if mem > 85:state = "WARNING"
    if mem > 90:state = "CRITICAL"
    stringsend = stringsend + "\n\n" +"Memory usage: " +str(mem)+"% : "+state
    #sendmsg(stringsend,who)
    
    #CHECK Website
    url = 'http://delc-edu.com/'
    try :
        response = urlopen( url )
    except HTTPError, e:
        print 'The server couldn\'t fulfill the request. Reason:', str(e.code)
        stringsend = stringsend + "\n\n" + "restarting mysql & nginx"
        os.system("service mysql restart")
        os.system("service nginx restart")
    except URLError, e:
        print 'We failed to reach a server. Reason:', str(e.reason)
    else :
        html = response.read()
        stringsend = stringsend + "\n\n" + "Website is Up, Respondable"
    #os.remove('tmp')
    stringsend = stringsend + "\n\n" +"Colonel Technology V3 \n(DELC) Reported"
    sendmsg(stringsend,who)
    sendmsg("=============",who)
        
       


schedule.every().day.at("09:17").do(sendsecurity,colonel)
schedule.every().day.at("19:17").do(sendsecurity,colonel)
schedule.every().day.at("00:17").do(sendsecurity,colonel)
print ('Start Running')

#schedule.every().day.at("07:30").do(sendgoodmorning,preperform)

'''
schedule.every().day.at("07:29").do(sendcurrenttime,colonel)


schedule.every().monday.at("09:00").do(sendmsg,"Notice: Lab Circuit 09:30 Incoming @ENGR314",colonel)
schedule.every().monday.at("13:00").do(sendmsg,"Notice: TA Lab JAVA CN302 13:30 Incoming @ENGR301",colonel)

schedule.every().tuesday.at("09:00").do(sendmsg,"Notice: Database Lecture 09:30 Incoming @ENGR304",colonel)
schedule.every().tuesday.at("13:00").do(sendmsg,"Notice: Operating System 13:30 Incoming @ENGR604",colonel)

schedule.every().wednesday.at("09:00").do(sendmsg,"Notice: Circuit Synthesis Lecture 09:30 Incoming + Abandoned @ENGR315",colonel)

schedule.every().thursday.at("09:00").do(sendmsg,"Notice: Digital Lecture 09:30 Incoming @ENGR315",colonel)
schedule.every().thursday.at("13:00").do(sendmsg,"Notice: Data Structure II Lecture 13:30 Incoming @ENGR315",colonel)

schedule.every().friday.at("08:30").do(sendmsg,"Notice: TU110 Lecture 09:00 Incoming + Passed @SC2051",colonel)
'''
#schedule.every().monday.at("09:00").do(sendsecurity,testdelc)
#schedule.every(5).seconds.do(sendsecurity,colonel)
while(True):
    
    schedule.run_pending()
    time.sleep(1)
