
# ZoomJoiner 
![enter image description here](https://charliealgert.com/Zoom.png)

This is a program to automatically join and leave your zoom classes. Windows only due to its windows API dependencies. Sorry Mac users AUHSD bock schedule is preloaded, just paste in your class links and system username in the config!


# Dependencies

The file explorer is accessible using the button in left corner of the navigation bar. You can create a new file by clicking the **New file** button in the file explorer. You can also create folders by clicking the **New folder** button.

 
# Directions

 - Add Zoom binary to your PATH environment variable
 - Your default browser must be chromium for cookie reasons.   //Find a chromium installer here: https://bit.ly/389xxAN
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
 
