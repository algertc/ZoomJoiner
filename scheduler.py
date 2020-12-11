from datetime import datetime
import Join
import time
import configparser
import subprocess


#load the config
config = configparser.ConfigParser()
config.read("config.ini")


#Sets the days of the week to their value in datetime
monday = 0
tuesday = 1
wednesday = 2
thursday = 3
friday = 4
saturday = 5
sunday = 6
##

#holiday exceptions
#miramonte holiday calendar: https://www.acalanes.k12.ca.us/Page/560#calendar704/20201101/month
Holidays = ["12/21/20", "12/22/20", "12/23/20", "12/24/20", "12/25/20", "12/26/20", "12/27/20", "12/28/20", "12/28/20", "12/29/20", "12/30/20", "12/31/20", "1/1/21", "2/12/21", "2/13/21", "3/29/21", "3/30/21", "4/1/21", "4/2/21"]
Finals_Week1 = ["12/15/20", "12/16/20", "12/17/20", "12/18/20"]
Finals_Week2 = ["5/24/21", "5/25/21", "5/26/21", "5/27/21", "5/28/21"]
#------------------------------------------------------------------------------------------------------------------------------####

def login():
    #Programatically signs into zoom using the api
    from pywinauto import Desktop, Application
    app = Application(backend="uia").start("zoom --login")
    main_win = app.window(title='Zoom Cloud Meetings')
    signIn = main_win.child_window(title="Sign In", control_type="Button")
    try:
        signIn.click()
        time.sleep(0.3)
    except:
        try:
            signInWithGoogle = main_win.child_window(title="Sign In with Google", control_type="Button")
            signInWithGoogle.click()

        except:
            print("SigninError")
    #main_win.print_control_identifiers()
login()

def maain():
    while True:
        #store the date
        date = datetime.now().strftime("%D")

        #todo make sure the user is logged in
        #login()

    #make sure today is not a holiday or final day
        if date in Holidays == False and date in Finals_Week1 == False and date in Finals_Week2 == False:

            while True:

                #detects a new day and breaks out of the loop to update the date variable
                if datetime.now().strftime("%D") != date:
                    break

                # tuesday/thursday schedule
                if datetime.today().weekday() == tuesday or datetime.today().weekday() == thursday:
                    if datetime.now().strftime("%H:%M") == config['SCHEDULE']['period1_startTime']:
                        Join.period1() #todo Meeting.py then meeting.chem. Meeting.chem will handle the breakout rooms and stuff
                        #sleep time makes sure you dont join multiple times
                        time.sleep(60)

                    elif datetime.now().strftime("%H:%M") == config['SCHEDULE']['period2_startTime']:
                        Join.period2()
                        time.sleep(60)

                    elif datetime.now().strftime("%H:%M") == config['SCHEDULE']['period3_startTime']:
                        Join.period3()
                        time.sleep(60)

                    elif datetime.now().strftime("%H:%M") == config['SCHEDULE']['period7_startTime']:
                         Join.period7()
                         time.sleep(60)



                #wednesday/friday schedule
                if datetime.today().weekday() == wednesday or datetime.today().weekday() == friday:
                    """
                    This section is for people that have to attend an academy regularly:
                    if datetime.now().strftime("%H:%M") == "09:00":
                        Join.<addFuncForYourClass>
                        time.sleep(60)
                    """
                    if datetime.now().strftime("%H:%M") == config['SCHEDULE']['period4_startTime']:
                        Join.period4()
                        #add delay to make sure you dont try to join multiple times
                        time.sleep(60)
                    elif datetime.now().strftime("%H:%M") == config['SCHEDULE']['period5_startTime']:
                        if str(config['CLASSES']['period5_link']) != "none":
                            Join.period5()
                            time.sleep(60)

                    elif datetime.now().strftime("%H:%M") == config['SCHEDULE']['period6_startTime']:
                        if str(config['CLASSES']['period6_link']) != "none":
                            Join.period6()
                            time.sleep(60)


