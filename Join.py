import subprocess
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
print(config['CLASSES']['period1_link'])
#config['CLASSES'] = {'ServerAliveInternal': '45'}

def joinmeeting(url):
    #todo if platform == windows, run this. Add if plat == mac and the correct command
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
    joinmeeting(str(config['CLASSES']['period1_link']))

def period2():
    joinmeeting(str(config['CLASSES']['period2_link']))

def period3():
    joinmeeting(str(config['CLASSES']['period3_link']))

def period4():
    joinmeeting(str(config['CLASSES']['period4_link']))

def period5():
    joinmeeting(str(config['CLASSES']['period5_link']))

def period6():
    joinmeeting(str(config['CLASSES']['period6_link']))

def period7():
    joinmeeting(str(config['CLASSES']['period7_link']))


# def law():
#     joinmeeting("https://auhsdschools.zoom.us/j/81548114514?uname=Charles+Algert#success")
#
# def chemistry():
#     joinmeeting("https://auhsdschools.zoom.us/j/7753695672?pwd=NTB1V1FRYTRnalBlYlBidnhXdDd2dz09#success")
#
# def english():
#     joinmeeting("https://auhsdschools.zoom.us/j/89099587841?uname=Charles+Algert#success")
#
#
# def spanish():
#   joinmeeting("https://auhsdschools.zoom.us/j/3163825343?uname=Charles+Algert#success")
#
#
# def math():
#     joinmeeting("https://auhsdschools.zoom.us/j/6602696666?pwd=aE1vQVVvd1c4SDNTRThITGxaYjJ1QT09&uname=Charles+Algert#success")
#
#
# def art():
#     joinmeeting("https://auhsdschools.zoom.us/j/85814123045?pwd=c25rUmdFcWhrZ00ydGVEK3hwNDdidz09&uname=Charles+Algert#succes")

