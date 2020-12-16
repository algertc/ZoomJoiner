

# ZoomJoiner 
![enter image description here](https://charliealgert.com/Zoom.png)



[![](https://img.shields.io/badge/Platform-Windows-blue) ]()



![](https://img.shields.io/badge/Platform-Windows-blue) ![](https://img.shields.io/badge/Stable-No%20release-red) ![](https://img.shields.io/badge/License-GNU-brightgreen) ![](https://img.shields.io/badge/Discord-Wonton0651-blue)


This is a program to automatically join and leave your zoom classes. It does not use pyautogui and works only by using the windows API. This method is much more reliable than existing programs and does not require the screen resolution to be the same. This makes it highly distributable and overall just better than using a program to control the mouse and keyboard. Windows only due to its windows API dependencies. Sorry Mac users. AUHSD bock schedule is preloaded, just paste in your class links and system username in the config!


# Dependencies

 - Python 3.7
 - Windows
 - Chromium Browser
 - Zoom...
 - Sign in with google zoom account

 
# Directions

 - Add Zoom binary to your PATH environment variable
 - Your default browser must be chromium for cookie reasons.   //Find a chromium installer here: https://bit.ly/389xxAN
	 - In chromium navigate to accounts.google.com and log in once and save the credentials
 - Edit the config
	 - If you are in the AUHSD the period start times do not need to be edited
	 - Paste in your zoom links to the corrosponding period in the config.ini
	 - If you do not know your system username: In powershell or command prompt, type "whoami" and enter the name after the backslash in the **User** section
	 - Lastly, ensure that the number of periods is correct
 - **I recommend changing the extension to .pyw to make the program run in the background then compiling to an exe
 - Run the program and it will join your zooms!

# Upcomming features


 1. Integration with Mozilla deepspech
 2. Leave the meeting if a breakout room is detected
 3. Add an option to automatically send chat messages
 
