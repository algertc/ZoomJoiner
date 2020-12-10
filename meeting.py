import Join

#file storing the functions to be run during the meeting

#todo if no other solution is found just try a neural network. "python image recognition nueral network" just steal someone elses NN and if it is identified as the breakout room popup get the pos
#todo might need to move the zoom meeting the the primary monitor after it is opened to get pyautogui to work https://stackoverflow.com/questions/16113237/specify-monitor-when-opening-file-bat
#todo you may need to thread the during meeting functions and the scheduler. OR check for new date within the class function and if datetime now != day then break. Will putting a break in the func here break out of the loop in the scheudler?
#todo join audio
#todo detect breakout room and leave even type in chat that you are having internet problems. Probably not possible but maybe send chat message with api
#todo leave after 15 minutes !!!!!!!!function already exists in testenv.py


def checkForBreakoutRoom():
    pass
def chemistry():
    Join.chemistry()

    #todo inside this function, check for breakout rooms and rull all during meeting tasks
    #todo DETECT BY WIRESHARK/FIDDLER??? Use zoom transcript or a speach to text and parse it for the words "breakout room"
    #todo transcript.py has a speech to text from here https://stackoverflow.com/questions/46966787/continuous-real-time-speech-to-text-with-watson-for-python
    #another speech to text solution https://www.ibm.com/blogs/watson/2016/07/getting-robots-listen-using-watsons-speech-text-service/
    #when a breakout room is detected, quit the app and send a system pop up / notification saying breakout room detected. Quitting!