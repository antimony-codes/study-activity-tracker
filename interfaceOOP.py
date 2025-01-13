from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import messagebox
import storedData, Analysis, Activity, WebsiteBlocker
from threading import Thread
import os
from datetime import datetime as dt
from datetime import time
import time

def blocking_function():
   os.system('python Trial.py')

# frame 1 widgets 
class Frame1:
   
   web_list = []
   app_list = []
   
   def tracking_function(self):
      Activity.start_tracking()
      
   def track(self):
      thread = Thread(target=self.tracking_function)
      thread.daemon = True
      thread.start()
      messagebox.showinfo('Confirmation', 'Tracking has started!')

   def name_save_button(self):
      name_var = name_entry.get()
      messagebox.showinfo("Confirmation", f"Goal Time is {name_var}")
      
      
   def add_app(self):        
      app_name = app_track_entry.get()
      app_listbox.insert(END, app_name)
      # self.app_list.append(app_name)
      storedData.save_tracking_app(app_name)
      app_track_entry.delete(0, 'end')
      
      
   def remove_app(self):
      app_name = app_listbox.get(ACTIVE)
      app_listbox.delete(ANCHOR)
      storedData.delete_tracking_app(app_name)
      # self.app_list.remove(app_name)
      
   def reset_applist(self):
      app_listbox.delete(1, END)
      storedData.reset_tracking_app()
      # self.app_list.clear()
      
   def add_web(self):
      web_name = web_track_entry.get()
      web_listbox.insert(END, web_name)
      # self.web_list.append(web_name)
      storedData.save_tracking_website(web_name)
      web_track_entry.delete(0, 'end')
      
   def remove_web(self):
      web_name = web_listbox.get(ACTIVE)
      web_listbox.delete(ANCHOR)
      storedData.delete_tracking_website(web_name)
      # self.web_list.remove(web_name)

   def reset_weblist(self):
      web_listbox.delete(1, END)
      storedData.reset_tracking_website()
      self.web_list.clear()
    
   def add_frame1_widgets(self, frame):
      self.frame = frame
      global name_entry, app_track_entry, app_list, app_listbox
      global web_track_entry, web_list, web_listbox
      
      name_label = Label(self.frame, text="Set a goal time (in mins): ").place(x=10, y=10)
      name_entry = Entry(self.frame)
      name_entry.place(x=220, y=10)
      save_name_button = Button(self.frame, width=7, height=1, text="Save", command=self.name_save_button)
      save_name_button.place(x=550, y=10)
      
      # app input
      Label(self.frame, text="Enter Application for tracking: ").place(x=10, y=70)
      app_track_entry = Entry(self.frame)
      app_track_entry.place(x=270, y=70)
      app_save_button = Button(self.frame, width=7, height=1, text='Save', command=self.add_app)
      app_save_button.place(x=550, y=110)
      app_del_button = Button(self.frame, width=7, height=1, text='Delete', command=self.remove_app)
      app_del_button.place(x=550, y=155)
      app_reset_button = Button(self.frame, width=7, height=1, text='Reset', command=self.reset_applist)
      app_reset_button.place(x=550, y=200)
      app_listbox = Listbox(self.frame, height=6, width=50)     
      app_listbox.place(x=10, y=110)
      app_listbox.insert(1, "Tracking Apps: ")
      
      with open('trackingApps.txt', 'r+') as appdata:
         lines = appdata.readlines()
         for line in lines:
            app_listbox.insert(END, line)

      # website input
      Label(self.frame, text="Enter Website for tracking: ").place(x=10, y=300)
      web_track_entry = Entry(self.frame)
      web_track_entry.place(x=270, y=300)
      web_save_button = Button(self.frame, width=7, height=1, text='Save', command=self.add_web)
      web_save_button.place(x=550, y=340)
      web_del_button = Button(self.frame, width=7, height=1, text='Delete', command=self.remove_web)
      web_del_button.place(x=550, y=385)
      web_reset_button = Button(self.frame, width=7, height=1, text='Reset', command=self.reset_weblist)
      web_reset_button.place(x=550, y=430)
      web_listbox = Listbox(self.frame, height=6, width=50)
      web_listbox.place(x=10, y=340)
      web_listbox.insert(1, "Tracking Websites: ")
      
      with open('trackingWebsites.txt', 'r+') as websitedata:
         lines = websitedata.readlines()
         for line in lines:
            web_listbox.insert(END, line)
            
      trackingButton = Button(self.frame, text='Start Tracking!', command=self.track)
      trackingButton.place(x=10, y=520)

      
      
# matplotlib charts here!
class Frame2:
   
   def add_frame2_widgets(self, frame):
      self.frame = frame
      var1 = IntVar()
      var2 = IntVar()
      var3 = IntVar()
      var4 = IntVar()
      var5 = IntVar()
      var6 = IntVar()
      var7 = IntVar()
      var8 = IntVar()
      var9 = IntVar()
      var10 = IntVar()

      app_list = open('trackingApps.txt','r').read().split('\n')
      web_list = open('trackingWebsites.txt','r').read().split('\n')
      
      def get_time_spent(app):
         time = name_entry.get()
         time = int(time)
         target_data = Analysis.daily_app_data[Analysis.daily_app_data['Activity Name'].str.contains(app)]
         obtained_value = target_data['total_time'].sum()
         step_value = (obtained_value  * 100) / time
         return step_value
      
      def web_time_spent(website):
         time = name_entry.get()
         time = int(time)
         target_data = Analysis.daily_website_data[Analysis.daily_website_data['Website'].str.contains(website)]
         obtained_value = target_data['total_time'].sum()
         step_value = (obtained_value  * 100) / time
         return step_value
         
      def update():
         var1.set(0)
         var2.set(0)
         var3.set(0)
         var4.set(0)
         var5.set(0)
         var6.set(0)
         var7.set(0)
         var8.set(0)
         var9.set(0)
         var10.set(0)
         
         app1_time = get_time_spent(app_list[0])
         app2_time = get_time_spent(app_list[1])
         app3_time = get_time_spent(app_list[2])
         app4_time = get_time_spent(app_list[3])
         app5_time = get_time_spent(app_list[4])
         
         web1_time = web_time_spent(web_list[0])
         web2_time = web_time_spent(web_list[1])
         web3_time = web_time_spent(web_list[2])
         web4_time = web_time_spent(web_list[3])
         web5_time = web_time_spent(web_list[4])
         
         
         pabar1.step(app1_time)
         pabar2.step(app2_time)
         pabar3.step(app3_time)
         pabar4.step(app4_time)
         pabar5.step(app5_time)
    
         pwbar1.step(web1_time)
         pwbar2.step(web2_time)
         pwbar3.step(web3_time)
         pwbar4.step(web4_time)
         pwbar5.step(web5_time)
      
      for i in range(len(app_list)):
         app_label = Label(self.frame, text=app_list[i])
         app_label.place(x=25, y=55+(i*40))
         
      pabar1 = Progressbar(self.frame, length=400, variable=var1)
      pabar1.place(x=200, y=60+(0*40))
      pabar2 = Progressbar(self.frame, length=400, variable=var2)
      pabar2.place(x=200, y=60+(1*40))
      pabar3 = Progressbar(self.frame, length=400, variable=var3)
      pabar3.place(x=200, y=60+(2*40))
      pabar4 = Progressbar(self.frame, length=400, variable=var4)
      pabar4.place(x=200, y=60+(3*40))
      pabar5 = Progressbar(self.frame, length=400, variable=var5)
      pabar5.place(x=200, y=60+(4*40))
         
      for i in range(len(web_list)):
         web_label = Label(self.frame, text=web_list[i])
         web_label.place(x=25, y=325+(i*40))
         
      pwbar1 = Progressbar(self.frame, length=400, variable=var6)
      pwbar1.place(x=200, y=330+(0*40))
      pwbar2 = Progressbar(self.frame, length=400, variable=var7)
      pwbar2.place(x=200, y=330+(1*40))
      pwbar3 = Progressbar(self.frame, length=400, variable=var8)
      pwbar3.place(x=200, y=330+(2*40))
      pwbar4 = Progressbar(self.frame, length=400, variable=var9)
      pwbar4.place(x=200, y=330+(3*40))
      pwbar5 = Progressbar(self.frame, length=400, variable=var10)
      pwbar5.place(x=200, y=330+(4*40))

      update_button = Button(self.frame, text='Update', command=update, height=1)
      update_button.place(x=525, y=5)
      Label(self.frame, text='TARGET APPLICATION PROGRESS').place(x=25, y=15)
      Label(self.frame, text='TARGET WEBSITE PROGRESS').place(x=25, y=285)

      Label(self.frame, text='Analysis of applications').place(x=25, y=550)
      daily_app_button = Button(self.frame, width=7, height=1, text='Today', command=Analysis.app_daily)
      daily_app_button.place(x=450, y=540)
      weekly_app_button = Button(self.frame, width=7, height=1, text='Weekly', command=Analysis.app_weekly)
      weekly_app_button.place(x=550, y=540)
      
      Label(self.frame, text='Analysis of websites').place(x=25, y=600)
      daily_website_button = Button(self.frame, width=7, height=1, text='Today', command=Analysis.website_daily)
      daily_website_button.place(x=450, y=590)
      weekly_website_button = Button(self.frame, width=7, height=1, text='Weekly', command=Analysis.website_weekly)
      weekly_website_button.place(x=550, y=590)
      
      
class Frame3:
   site_list = []
   
   def add_site(self):
      site_name = web_entry.get()
      site_listbox.insert(END, site_name)
      storedData.save_blocked_website(site_name)
      # self.site_list.append(site_name)
      web_entry.delete(0, 'end')
      
   def delete_site(self):
      site_delete_name = site_listbox.get(ACTIVE)
      site_listbox.delete(ANCHOR)
      storedData.delete_blocked_website(site_delete_name)
      # self.site_list.remove(site_delete_name)  
      
   def reset_sites(self):
      site_listbox.delete(0, END)
      storedData.reset_blocked_website()
      # self.site_list.clear()
   
   def set_time(self):
      start_time = from_time.get()
      meridian = from_time_AM.get()
      start_time = int(start_time)
      if meridian == "PM":
         start_time = start_time + 12
      end_time = to_time.get()
      end_time = int(end_time)
      meridian2 = to_time_AM.get()
      if meridian2 == 'PM':
         end_time = end_time + 12
         
      return start_time, end_time

 
   def blocking_function(self):
      os.system('python WebsiteBlocker.py')
   
   def start_block(self):
      # start_time, end_time = self.set_time()
      thread2 = Thread(target=self.blocking_function)
      thread2.daemon = True
      thread2.start()
      
   def unblocking_function(self):
      os.system('python Unblocker.py')
      
   def start_unblock(self):
      thread3 = Thread(target=self.unblocking_function)
      thread3.daemon = True
      thread3.start()
        
   def add_frame3_widgets(self, frame):
      global site_listbox, web_entry, from_time, to_time, from_time_AM, to_time_AM
      
      self.frame = frame
      Label(self.frame, text='Set blocking time: ').place(x=15, y=15)
      Label(self.frame, text='to ').place(x=325, y=15)
      time_set_button = Button(self.frame, text='Set Time', height=1, command=self.set_time)
      time_set_button.place(x=520, y=10)
      start_button = Button(self.frame, text='Start Blocking!', height=1, command=self.start_block)
      start_button.place(x=170, y=300)
      
      unblock_button = Button(self.frame, text='Unblock', command=self.unblocking_function)
      unblock_button.place(x=50, y=300)
      
      from_time = Spinbox(self.frame, from_=0, to=12, wrap=True, width=3)
      from_time.place(x=175, y=15)
      from_time_AM = Spinbox(self.frame, values=('AM', 'PM'), wrap=True, width=5, state='readonly')
      from_time_AM.place(x=225, y=15)
      
      to_time = Spinbox(self.frame, from_=0, to=12, wrap=True, width=3)
      to_time.place(x=375, y=15)
      to_time_AM = Spinbox(self.frame, values=('AM', 'PM'), wrap=True, width=5, state='readonly')
      to_time_AM.place(x=425, y=15)
      
      Label(self.frame, text='Enter site: ').place(x=50, y=90)
      web_entry = Entry(self.frame)
      web_entry.place(x=170, y=90)
      add_site_button = Button(self.frame, text='Block', height=1, width=7, command=self.add_site)
      add_site_button.place(x=500, y=130)
      delete_site_button = Button(self.frame, text='Unblock', height=1, width=7, command=self.delete_site)
      delete_site_button.place(x=500, y=180)
      reset_site_button = Button(self.frame, text='Reset', height=1, width=7, command=self.reset_sites)
      reset_site_button.place(x=500, y=230)
      site_listbox = Listbox(self.frame, height=6, width=40)
      site_listbox.place(x=50, y=130)

      with open('blockedWebsites.txt', 'r+') as websitedata:
         lines = websitedata.readlines()
         for line in lines:
            site_listbox.insert(END, line)
            
# to do list!         
class Frame4:
   
   def add_task(self):
      site_name = task_entry.get()
      task_listbox.insert(END, site_name)
      storedData.save_task(site_name)
      # self.site_list.append(site_name)
      task_entry.delete(0, 'end')
      
   def delete_task(self):
      site_delete_name = task_listbox.get(ACTIVE)
      task_listbox.delete(ANCHOR)
      storedData.delete_task(site_delete_name)
      # self.site_list.remove(site_delete_name)  
      
   def reset_task(self):
      task_listbox.delete(0, END)
      storedData.reset_task()
      # self.site_list.clear()
   
   def add_frame4_widgets(self, frame):
      
      global task_entry, task_listbox
      
      self.frame = frame
      Label(self.frame, text='Enter Task: ').place(x=50, y=90)
      task_entry = Entry(self.frame)
      task_entry.place(x=170, y=90)
      add_task_button = Button(self.frame, text='Add', height=1, width=7, command=self.add_task)
      add_task_button.place(x=500, y=130)
      delete_task_button = Button(self.frame, text='Delete', height=1, width=7, command=self.delete_task)
      delete_task_button.place(x=500, y=180)
      reset_task_button = Button(self.frame, text='Reset', height=1, width=7, command=self.reset_task)
      reset_task_button.place(x=500, y=230)
      task_listbox = Listbox(self.frame, height=15, width=45)
      task_listbox.place(x=20, y=130)

      with open('todolist.txt', 'r+') as websitedata:
         lines = websitedata.readlines()
         for line in lines:
            task_listbox.insert(END, line)
            
   
# pomodoro timer
class Frame5:
   
   def add_frame5_widgets(self, root):
      self.root = root
      self.work_duration = tk.StringVar(value="25")
      self.break_duration = tk.StringVar(value="5")

      self.work_label = tk.Label(root, text="Work Duration (minutes):")
      self.work_entry = tk.Entry(root, textvariable=self.work_duration)
      self.work_label.place(x=170, y=80)
      self.work_entry.place(x=270, y=120)

      self.break_label = tk.Label(root, text="Break Duration (minutes):")
      self.break_entry = tk.Entry(root, textvariable=self.break_duration)
      self.break_label.place(x=170, y=180)
      self.break_entry.place(x=270, y=220)
      
      self.start_button = tk.Button(root, text="Start Pomodoro", command=self.start_pomodoro, font = ('Segoe UI', 16))
      self.start_button.place(x=200, y=340)
   
   def start_pomodoro(self):
      try:
         work_minutes = int(self.work_duration.get())
         break_minutes = int(self.break_duration.get())
      except ValueError:
         messagebox.showerror("Error", "Please enter valid integer values for durations.")
         return
      
      pomodoro_window = tk.Toplevel(self.root)
      pomodoro_window.title("Pomodoro Timer")
      pomodoro_window.geometry("300x100")
      timer_label = tk.Label(pomodoro_window, text="Work Time: {} minutes".format(work_minutes), font=('Segoe UI', 16))
      timer_label.place(x=20, y=20)
      self.run_timer(pomodoro_window, work_minutes * 60)
      
   def run_timer(self, window, remaining_seconds):
      if remaining_seconds <= 0:
         window.destroy()
         messagebox.showinfo("Pomodoro Timer", "Time's up!")
         return
      
      minutes, seconds = divmod(remaining_seconds, 60)
      timer_text = "{:02d}:{:02d}".format(minutes, seconds)
      window.title("Pomodoro Timer - " + timer_text)
      
      # Update the timer label
      timer_label = window.winfo_children()[0]
      timer_label.config(text="Time Left: " + timer_text)

      # Update the timer after 1 second
      window.after(1000, self.run_timer, window, remaining_seconds - 1)
      
   

      
