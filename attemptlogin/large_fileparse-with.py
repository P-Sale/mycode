#!/usr/bin/python3

loginfail = 0
successful = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
            print("ip address of failure: ", line.split(" ")[-1])
        elif "-] Authorization failed" in line:
            successful += 1
print("login fails: ", loginfail)
print("successful logins: ", successful)
