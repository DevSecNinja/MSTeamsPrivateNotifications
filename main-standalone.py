import time
import os

from win10toast import ToastNotifier

def follow(logfile):
    logfile.seek(0, os.SEEK_END) # Go to the end of the file
    while True:
        line = logfile.readline()
        if not line:
            time.sleep(1) # Sleep briefly
            continue
        yield line

from os import path

icon_path = path.expandvars(r'%LOCALAPPDATA%\Microsoft\Teams\app.ico')
logfile_path = path.expandvars(r'%APPDATA%\Microsoft\Teams\logs.txt')

logfile = open (logfile_path)
loglines = follow (logfile)

for line in loglines:
    if "Available -> NewActivity" in line:
        print("-- Switching to NewActivity")
        print(line, end='')

        toaster = ToastNotifier()
        toaster.show_toast("Microsoft Teams Notification",
                "You have a new message",
                icon_path=icon_path,
                duration=5,
                threaded=True)
        while toaster.notification_active(): time.sleep(0.1)

    elif "NewActivity -> Available" in line:
        print("-- Switching to Available")
        print(line, end='')