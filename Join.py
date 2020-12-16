import subprocess
import configparser
import Zoom_Functions
import time


config = configparser.ConfigParser()
config.read("config.ini")


def joinmeeting(url):
    cmd = "zoom --url=" + str(url)
    subprocess.run(cmd)
    '''
    Send shell commands using subprocess to open the meeting directly
    Command format: subprocess.run("zoom --url=https://auhsdschools.zoom.us/j/85814123045?pwd=c25rUmdFcWhrZ00ydGVEK3hwNDdidz09&uname=Charles+Algert#succes")
    '''


#todo right now the scheduler is using the miramonte block schedule. Figure out how to import shedule times
#todo ADD TO GITHUB BEFORE FIXING SCHEDULER

#todo !!!!!!! Use config file with classes and urls that user can enter. Function will just be period1 and it will access item 1 in the config

#todo rename this file to "join" so the import format will be join.law()

#todo Create a meeting.py file and call from everything else? we need something that is always running to put the breakout room check in. Doing it within the functions is inefficient and bloaty


def period1():
    Zoom_Functions.login()
    joinmeeting(str(config['CLASSES']['period1_link']))
    time.sleep(260)
    Zoom_Functions.ConnectAndMute()

def period2():
    Zoom_Functions.login()
    joinmeeting(str(config['CLASSES']['period2_link']))
    time.sleep(260)
    Zoom_Functions.ConnectAndMute()

def period3():
    Zoom_Functions.login()
    joinmeeting(str(config['CLASSES']['period3_link']))
    time.sleep(260)
    Zoom_Functions.ConnectAndMute()

def period4():
    Zoom_Functions.login()
    joinmeeting(str(config['CLASSES']['period4_link']))
    time.sleep(260)
    Zoom_Functions.ConnectAndMute()

def period5():
    Zoom_Functions.login()
    joinmeeting(str(config['CLASSES']['period5_link']))
    time.sleep(260)
    Zoom_Functions.ConnectAndMute()

def period6():
    Zoom_Functions.login()
    joinmeeting(str(config['CLASSES']['period6_link']))
    time.sleep(260)
    Zoom_Functions.ConnectAndMute()

def period7():
    Zoom_Functions.login()
    joinmeeting(str(config['CLASSES']['period7_link']))
    time.sleep(260)
    Zoom_Functions.ConnectAndMute()

def demo():
    Zoom_Functions.login()
    joinmeeting("DEMOLINK")
    time.sleep(30)
    Zoom_Functions.ConnectAndMute()
demo()
