#!/usr/bin/env python3
import os
import time


uInput = 0
headings = "<h1>"
paragraphs = "<p>"
heading_close = "</h1>"

print ("This Program Converts Any HTML File In this Directory Named document.html To A text File")

print ("Made By Mohamedhany")


uInput = input('Do You Want To Continue? (yes/no):')

if uInput == "no":
    print ("Aborting")
    time.sleep(3)
    exit()

if uInput == "yes": 
    print ("Checking Files...")

    try:
        f = open('document.html')
        f.close
    except FileNotFoundError:
        print ('\x1b[7;31;40m' + "ERR 404: No Valid HTML Files Were Found In this Directory" + '\x1b[0m')
        print ("exiting in 8 secs")
        time.sleep(8)
        exit()
    
    print ("Reading Files..")
    f = open('document.html')
    for line in f:
        if headings in line:
            print (line.replace("<h1>", " "))
            
        
        if paragraphs in line:
            print (line.replace("<p>", " "))
    
    print ("Done.")
    time.sleep(5)
    exit()
            
    
    
