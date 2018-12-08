#!/usr/bin/python

'''
Pydoo
A todo program made for quickness and easability
Harrison Witt @altwitt
techanimist.com 
'''

import sys
from datetime import datetime

# Global Variables
title = '''  

________________________________________________
================================================
                           ,,                    
                         `7MM                    
                           MM                    
`7MMpdMAo.`7M`   `MF` ,M**bMM  ,pW*Wq.   ,pW*Wq. 
  MM   `Wb  VA   ,V ,AP    MM 6W`   `Wb 6W`   `Wb
  MM    M8   VA ,V  8MI    MM 8M     M8 8M     M8
  MM   ,AP    VVV   `Mb    MM YA.   ,A9 YA.   ,A9
  MMbmmd`     ,V     `Wbmd*MML.`Ybmd9`   `Ybmd9` 
  MM         ,V                                  
.JMML.    OOb*                                   

....so you do quick!
===============================================
===============================================

'''

# Use as partition
line_break = "================================"

# Getting the time and date
i = datetime.now()
thetime = i.strftime('%I.%M%p')
thedate = i.strftime('%m.%d.%Y')

# Functions
def get_tasks():
    '''Retrieves and parses the formatted groups and tasks
    from pydoo.txt'''

    c,w,h = [],[],[]

    with open("pydoo.txt","rt") as p:
        glist = p.read()
        text = glist.split("|")

    for i in text:
            g = i[0]
            if g  == 'c':
                i = i[1:]
                c.append(i)
            elif g  == 'w':
                i = i[1:]
                w.append(i)
            elif g  == 'h':
                i = i[1:]
                h.append(i)

    tasks = [c,h,w]
    return tasks

def which_group(str_group):
    '''Takes the user input string and associates it
    with a group list'''
    
    if str_group == "c":
        grp = codeG
    if str_group == "w":
        grp = workG
    if str_group == "h":
        grp = homeG

    return grp

def list_groups():
    '''Prints the groups and their tasks'''

    print("CODING GROUP{}".format(line_break))
    ccnt = 1

    for i in codeG:
        print("{0}: {1}".format(ccnt, i))
        ccnt += 1

    print("WORK GROUP{}".format(line_break))
    wcnt = 1

    for i in workG:
        print("{0}: {1}".format(wcnt, i))
        wcnt += 1

    print("HOME GROUP{}".format(line_break))
    hcnt = 1

    for i in homeG:
        print("{0}: {1}".format(hcnt, i))
        hcnt += 1

def add_task():
    '''Adds a task from the selected group'''

    groupQ = raw_input("Add to which group : ")
    group = which_group(groupQ)
    task = raw_input("Write task:  ")
    group.append(task)

def remove_task():
    '''Removes a task from the selected group'''

    cnt = 1
    groupQ = raw_input("Which group would you like to remove from? ")
    group = which_group(groupQ)

    if groupQ == "c":
        groupQ = "Code"
    elif groupQ == "w":
        groupQ = "Work"
    elif groupQ == "h":
        groupQ == "Home"
    else:
        print("You didn't enter a valid command")

    print(line_break)
    print(line_break)
    print("Tasks in the {} group: ".format(groupQ))

    for i in group:
        print("{0}: {1}".format(cnt, i))
        cnt += 1

    print(line_break)
    print(line_break)
    num = raw_input("Write the number of the task you would like to remove: ")
    cnt = 1

    while cnt <= len(group):
        if int(num) < cnt:
            cnt += 1
        else:
            group.pop(int(num)-1)
        break

def qloop():
    '''Flow control for list options'''
    if cmd == "q":
        save = raw_input("Save your list? y or n: ")
        if save == "y":
            put_tasks()
        sys.exit()
    elif cmd == "l":
        list_groups()
    elif cmd == "a":
        add_task()
    elif cmd == "r":
        remove_task()

def put_tasks():
    '''Send the saved list back to pydoo.txt'''
    with open("pydoo.txt","wt") as t:
        for i in codeG:
            if codeG[0] == i:
                t.write("c" + i)
            else:
                t.write("|c" + i)
           # t.write("\n")
        for i in workG:
            t.write("|w" + i)
           # t.write("\n")
        for i in homeG:
            t.write("|h" + i)
           # t.write("\n")

if __name__ == "__main__":
    tasks = get_tasks()
    codeG = tasks[0]
    homeG = tasks[1]
    workG = tasks[2]

    print title
    
    while True:
        print("\n")
        cmd = raw_input("(l)ist, (a)dd, (r)emove, or (q)uit: ")
        print("\n")
        qloop()
    
