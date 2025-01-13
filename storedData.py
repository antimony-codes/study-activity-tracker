import os
import pandas as pd

# for tracking apps

def save_tracking_app(app_name):
    with open('trackingApps.txt', 'a') as appdata:
        appdata.write(app_name + '\n')
        
def delete_tracking_app(app_name):
    file = open('trackingApps.txt', 'r')
    lines = file.readlines()
    file.close()
    file = open('trackingApps.txt', 'w')
    for line in lines:
        if app_name not in line:
            file.write(line)
            
def reset_tracking_app():
    file = open('trackingApps.txt', 'w')  
    file.close()


# for tracking websites

def save_tracking_website(website_name):
    with open('trackingWebsites.txt', 'a') as websitedata:
        websitedata.write(website_name + '\n')
        
def delete_tracking_website(website_name):
    file = open('trackingWebsites.txt', 'r')
    lines = file.readlines()
    file.close()
    file = open('trackingWebsites.txt', 'w')
    for line in lines:
        if website_name not in line:
            file.write(line)
            
def reset_tracking_website():
    file = open('trackingWebsites.txt', 'w')  
    file.close()
    
    
# for blocked websites

def save_blocked_website(website_name):
    with open('blockedWebsites.txt', 'a') as websitedata:
        websitedata.write(website_name + '\n')
        
def delete_blocked_website(website_name):
    file = open('blockedWebsites.txt', 'r')
    lines = file.readlines()
    file.close()
    file = open('blockedWebsites.txt', 'w')
    for line in lines:
        if website_name not in line:
            file.write(line)
            
def reset_blocked_website():
    file = open('blockedWebsites.txt', 'w')  
    file.close()
    
    
# for to do list
def save_task(website_name):
    with open('todolist.txt', 'a') as websitedata:
        websitedata.write(website_name + '\n')
        
def delete_task(website_name):
    file = open('todolist.txt', 'r')
    lines = file.readlines()
    file.close()
    file = open('todolist.txt', 'w')
    for line in lines:
        if website_name not in line:
            file.write(line)
            
def reset_task():
    file = open('todolist.txt', 'w')  
    file.close()