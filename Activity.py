import win32gui
import uiautomation as auto
import time
import datetime
from datetime import time
import os
import csv


def getCurrentActivity():
    win = win32gui.GetForegroundWindow()
    fullName = str(win32gui.GetWindowText(win))
    if "https://" in fullName or "http://" in fullName:
        fullName = "Pop-up Window"
    activityName = fullName.split(' - ')[-1]

    return win,activityName,fullName


def getWebsite(win):
    try:
        control = auto.ControlFromHandle(win)
        edit = control.EditControl()
        # print(edit.GetValuePattern().Value)
        website = str(edit.GetValuePattern().Value).split('/')[0]
    except:
        website = "-"
    
    return website


def ifFileExists():
    return os.path.exists('ActivityData.csv')


def setDataFile():
    flag = ifFileExists()
    if flag:
        flag = not os.stat("ActivityData.csv").st_size == 0

    with open('ActivityData.csv','a',newline="") as data:
        writer = csv.writer(data)
        if not flag:
            print("Initializing the file to store data....")
            writer.writerow(["Date","Activity Name","isWebBrowser","Website","Start Time","End Time","Total Time(h:m:s)","total_time"])
            time.sleep(2)


def writeData(todayDate,activityName,isWebBrowser,website,startTime,endTime):
    setDataFile()
    
    def time_convert(x):
        h,m,s = map(float, x.split(':'))
        # time_in_hours = h + (5/3 * m), apply when database has longer usage of websites
        # print(time_in_hours)
        # using temporary seconds time
        return h*60 + m + s*0
    
    
    with open('ActivityData.csv','a',newline="") as data:
        writer = csv.writer(data)
        writer.writerow([todayDate,activityName,isWebBrowser,website,startTime,endTime,(endTime-startTime), (endTime-startTime).seconds//60%60])


def start_tracking():
    os.system('cls')
    todayDate = datetime.date.today()
    startTime = datetime.datetime.now()
    last_activity = ""
    last_website = ""
    

    webBrowsers = ["Google Chrome","Mozilla Firefox"]

    setDataFile()
    while True:
        try:
            win,activityName,fullName = getCurrentActivity()
            endTime = datetime.datetime.now()
            website = "-"
            if activityName in webBrowsers:
                website = getWebsite(win)
                if fullName.split(" - ")[0]=="New Tab":
                    website = "google.com"
            
            if last_activity == "":
                last_activity = activityName
                if activityName in webBrowsers:
                    last_website = website
            
            elif activityName != last_activity or (activityName in webBrowsers and website!=last_website) or datetime.date.today()!=todayDate:
                #print(last_activity + " " + str(endTime - startTime))

                if last_activity in webBrowsers:
                    #print(last_website)
                    writeData(todayDate,last_activity,1,last_website,startTime,endTime)
                else:
                    writeData(todayDate,last_activity,0,"-",startTime,endTime)

                last_website = website
                startTime = endTime
                last_activity = activityName
                todayDate = datetime.date.today()
        except KeyboardInterrupt:
            print("Do you want to quit? (Y or y to quit)")
            choice = input("Choice : ")
            if choice.lower() == "y":
                if last_activity in webBrowsers:
                    #print(last_website)
                    writeData(todayDate,last_activity,1,last_website,startTime,endTime)
                    last_website = website
                else:
                    writeData(todayDate,last_activity,0,"-",startTime,endTime)
                print("Exiting!")
                break
            else:
                print("Continuing!")
                continue
        except UnicodeEncodeError:
            last_activity = ""
            startTime = endTime
            continue
    