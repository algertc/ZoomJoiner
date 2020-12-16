import time
import subprocess
import psutil
import keyboard
from pywinauto import Desktop, Application

# super long clunky function that kills zoom and chromium then logs the user back in to ensure that autologout doesn't interfere with the program


def login():
    global app
    global main_win
    # Programatically kills then starts and signs into zoom all using the api
    subprocess.call("taskkill /IM \"Zoom.exe\" /F")  # If this breaks, you could use $> tasklist | more and grep the output to a file then parse it for the word "zoom" to get the process ID and kill it that way.
    subprocess.call("taskkill /IM \"chrome.exe\" /F")
    # launch zoom with win32 api
    app = Application(backend="uia").start("zoom --login")
    main_win = app.window(title='Zoom')

    # todo find the leave wrapper and leave meeting

    # if the app opens to the "zoom cloud meetings" welcome screen, lets sign in
    try:
        # defines this screen: "JoinMeetingANDSignIn_Screen.png" as the window
        JoinMeetingANDSignIn_Screen = app.window(title='Zoom Cloud Meetings')
        time.sleep(0.5)
        # selects the control identifier for the "sign in" button and activates it
        startscreen = JoinMeetingANDSignIn_Screen.child_window(title="Sign In", control_type="Button")
        startscreen.click()

    except:
        pass

    try:
        SigninWithGoogleScreen = app.window(title='Zoom Cloud Meetings')
        signInWithGoogle = SigninWithGoogleScreen.child_window(title="Sign In with Google", control_type="Button")
        signInWithGoogle.click()
        if "chrome.exe" in (p.name() for p in psutil.process_iter()):
            print("Chromium.exe process is running")
            # processID = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'Sign In - Google Accounts' in p.info['name']]
            # print(processID)
            time.sleep(4)
            # todo might need to select window first
            # keyboard.write(config['GOOGLE_CREDENTIALS']['email'])
            # keyboard.press("enter")
            # time.sleep(2)
            # keyboard.write(config['GOOGLE_CREDENTIALS']['password'])
            # keyboard.press("enter")
            time.sleep(2)
            keyboard.press("tab")
            time.sleep(0.3)
            keyboard.press("tab")
            time.sleep(0.6)
            keyboard.press("enter")
            time.sleep(0.4)
            keyboard.press("enter")
            #
            time.sleep(3)
            keyboard.press("tab")
            time.sleep(0.4)
            keyboard.press("tab")
            time.sleep(0.4)
            keyboard.press("enter")
            time.sleep(0.4)
            keyboard.press("enter")
            # pywinauto.application.findwindows.find_element("Edge")
            # chrome = Application(backend="uia").connect(path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            # chromewindow = chrome.top_window()

            # mainwin_edge = edge.window(title='Sign In - Google Accounts and')

        # todo return control identifiers or write to file and read the file

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

        # SigninWithGoogleScreen.print_control_identifiers()

    except:
        pass


    return app

def leaveMeeting():
    #todo IMPORTANT ---- IF the control identifier is there click it. Figure out how to store the control identifiers to a variable or file. File is likely better then use a file parsing lib
    #no need to set up the active window again since it has already been done in the login func
    #lets logout
    #inMeeting = Application.connect(path="C:\\Users\\alger\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    # write the control identifiers to a file
    time.sleep(18)
    #inMeeting.print_control_identifiers(filename="ctlIDS.txt")
    with open('ctlIDS.txt') as f:
        if 'replaceWithLeavemeeting button' in f.read():
            pass
            #click the button here
        #else
            # maybe loop?

def ConnectAndMute():
    time.sleep(240) #todo change to 3 minutes in case teacher is slow with breakout room
    keyboard.send("enter")
    time.sleep(0.3)
    keyboard.send("tab")
    time.sleep(0.3)
    keyboard.send("tab")
    time.sleep(0.3)
    keyboard.send("tab")
    time.sleep(0.3)
    keyboard.send("enter")

#login()
leaveMeeting()