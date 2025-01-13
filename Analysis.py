import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import *


data = pd.read_csv('ActivityData.csv')


# getting today's and lastweek's dates
today = str(date.today())
week = []
for i in range (7):
  day = (date.today() - timedelta(days = i)).strftime('%Y-%m-%d')
  week.append(day)
lastweek = tuple(week)

# user input for different activity tracking

def add_tracking_apps():
    with open('trackingApps.txt', 'r') as file:
        lines = []
        for line in file:
            line = line.strip()
            lines.append(line)
        return lines
      
def add_tracking_websites():
    with open('trackingWebsites.txt', 'r') as file:
        lines = []
        for line in file:
            line = line.strip()
            lines.append(line)
        return lines

trackingApps = add_tracking_apps()
trackingWebsites = add_tracking_websites()

# extracting rows containing today's date And the week's dates
daily_data = data[data['Date'].str.contains(today)]
# print(daily_data.head())
weekly_data = data[data['Date'].str.contains('|'.join(lastweek))]
# print(weekly_data.head())


# sorting by websites: user input given by trackingApps and trackingWebsites

daily_app_data = daily_data[daily_data['Activity Name'].str.contains('|'.join(trackingApps))]

# website data needs some manipulation to remove NaN and - values
daily_website_data = daily_data[daily_data['isWebBrowser'] == 1]
daily_website_data = daily_website_data[daily_website_data['Website'] != '-']
daily_website_data.dropna(how = 'any', inplace = True)
daily_website_data = daily_website_data[daily_website_data['Website'].str.contains('|'.join(trackingWebsites))]

weekly_app_data = weekly_data[weekly_data['Activity Name'].str.contains('|'.join(trackingApps))]

# website data manipulation
weekly_website_data = weekly_data[weekly_data['isWebBrowser'] == 1]
weekly_website_data = weekly_website_data[weekly_website_data['Website'] != '-']
weekly_website_data.dropna(how = 'any', inplace = True)
weekly_website_data = weekly_website_data[weekly_website_data['Website'].str.contains('|'.join(trackingWebsites))]

# daily analysis for apps
def app_daily():
  temp_daily = daily_app_data.groupby(['Activity Name'])['total_time'].sum()
  sns.barplot(y=temp_daily.values,x=temp_daily.index.values)
  plt.title("Total time spent in different apps")
  plt.xlabel("App Name")
  plt.ylabel('Total time spent in different apps (min)')
  plt.xticks(rotation = 15)
  plt.show()
  
def website_daily():
  temp_daily = daily_website_data.groupby(['Website'])['total_time'].sum()
  sns.barplot(y=temp_daily.values,x=temp_daily.index.values)
  plt.title("Total time spent in different websites")
  plt.xlabel("Website Name")
  plt.ylabel('Total time spent in different websites (min)')
  plt.xticks(rotation = 15)
  plt.show()
  
def app_weekly():
  temp_weekly = weekly_app_data.groupby(['Activity Name'])['total_time'].sum()
  sns.set_palette('viridis')
  sns.barplot(y=temp_weekly.values,x=temp_weekly.index.values)
  plt.title('Weekly Analysis of target apps')
  plt.xlabel("App name")
  plt.ylabel("Time spent in minutes")
  plt.xticks(rotation = 15)
  plt.show()

def website_weekly():
  temp_weekly = weekly_website_data.groupby(['Website'])['total_time'].sum()
  sns.set_palette('viridis')
  sns.barplot(y=temp_weekly.values,x=temp_weekly.index.values)
  plt.title('Weekly Analysis of target websites')
  plt.xlabel("Website Name")
  plt.ylabel("Time spent in minutes")
  plt.xticks(rotation = 15)
  plt.show()
