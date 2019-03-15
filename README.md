# Microsoft Teams Private Notifications for Windows 10
A Python script that creates a toast message when a new message pops-up in Microsoft Teams. It hides the message preview to prevent others from reading messages on the screen during meetings:

![Microsoft Teams Toast Message](images/Microsoft_Teams_Notification.png)

## Installation
Download the main-standalone.py script. Make sure you have Python 3.7 or newer installed on your system.

Install the win10toast Python Library from jithurjacob (see his [Github](https://github.com/jithurjacob/Windows-10-Toast-Notifications))
```
pip install pypiwin32
pip install setuptools
pip install win10toast
```

Create a scheduled task in Windows 10 that uses an "At log on" trigger for your user account. Use the following action:

- **Action**: Start a program
- **Program/script**: pythonw
- **Add arguments**: .\main-standalone.py
- **Start in**: The location of the script on your local disk. Make sure your user account has access to it.

Run the Task Scheduler task and ask someone to send you a message or have a chat with the Teams Bot.

## Requirements

### System Requirements
Windows 10 with Python 3.7 or newer installed

### Requirements to run the script
```
pypiwin32
setuptools
```

## To-do
- Adjust the script to run as a Windows Service. Currently the script needs to run under user context for the Toast Messages to work. That's why it needs to be triggered from a Scheduled Task.
- The script is a bit 'quick and dirty' as it gathers the status from the log file. It would be nice to integrate with the Teams Client SDK.

## Credits
- win10toast Python Library from jithurjacob (see his [GitHub project](https://github.com/jithurjacob/Windows-10-Toast-Notifications))