from datetime import datetime
import Join
import time
import configparser
import subprocess
import psutil
import pywinauto

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
    #Programatically kills then starts and signs into zoom all using the api
    from pywinauto import Desktop, Application

    #First lets kill zoom to ensure consistency
    subprocess.call("taskkill /IM \"Zoom.exe\" /F")  #If this breaks, you could use $> tasklist | more and grep the output to a file then parse it for the word "zoom" to get the process ID and kill it that way.
    subprocess.call("taskkill /IM \"msedge.exe\" /F")
    #launch zoom with win32 api
    app = Application(backend="uia").start("zoom --login")
    main_win = app.window(title='Zoom')
    #todo find the log out wrapper and log the user out


    #if the app opens to the "zoom cloud meetings" welcome screen, lets sign in
    try:
        # defines this screen: "JoinMeetingANDSignIn_Screen.png" as the window
        JoinMeetingANDSignIn_Screen = app.window(title='Zoom Cloud Meetings')
        time.sleep(0.5)
        #selects the control identifier for the "sign in" button and activates it
        startscreen = JoinMeetingANDSignIn_Screen.child_window(title="Sign In", control_type="Button")
        startscreen.click()

    except:
        pass


    try:
        SigninWithGoogleScreen = app.window(title='Zoom Cloud Meetings')
        signInWithGoogle = SigninWithGoogleScreen.child_window(title="Sign In with Google", control_type="Button")
        signInWithGoogle.click()

        #SigninWithGoogleScreen.print_control_identifiers()

    except:
        pass

    if "msedge.exe" in (p.name() for p in psutil.process_iter()):
        print("ture")
        #processID = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'Sign In - Google Accounts' in p.info['name']]
        #print(processID)
        time.sleep(1)
        #pywinauto.application.findwindows.find_element("Edge")
        edge = Application(backend="uia").connect(title='Edge')
        #edge = Application().connect(title="Edge")
        #mainwin_edge = edge.window(title='Sign In - Google Accounts and')




    #todo return control identifiers or write to file and read the file

    # try:
    #     #todo IF control identifiers has attribute "child_window(title="Sign In", control_type="Button")" :
    #     time.sleep(1)
    #     signIn.click()
    #     #time.sleep(0.3)
    #     time.sleep(1)
    #     #todo check IF control identifiers has attribute "title="Sign In with Google", control_type="Button"
    #     signInWithGoogle = main_win.child_window(title="Sign In with Google", control_type="Button")
    #     signInWithGoogle.click()
    #     #todo check if browser has opened
    #
    # except:
    #     #todo possibly try again before printing error. Make a counter and print on the second time through
    #     print("SigninError")

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
                        #TODO IF: the header for login with google exists in the window, quit zoom, run login(), then run the join again
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


