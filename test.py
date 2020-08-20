import os
import pyttsx3 as py
x=1
flag=1
while(flag):
    if x == 1 :
        py.speak("enter your choice")
        x=12
    else:
        py.speak("enter your choice again or enter exit")
    i=input("enter your choice : ")
    if ("run" in i ) or ("launch" in i) or ("open" in i) or ("do" in i):
        if ("vlc" in i) or ("media player" in  i):
            py.speak("enter file name with extension")
            f=input("enter file name with extension : ")
            os.system("vlc {}".format(f))
        elif ("clean" in i) and  ("disk" in  i):
            os.system("cleanmgr")
        elif ("disk" in i) and  ("fragmentation" in  i):
            os.system("Defrag")
        elif ("calculator" in i) or ("maths" in  i) or  ("addition" in i ) or ("substration" in i ):
            os.system("calc")
    elif ("exit" in i ) or ("stop" in i ):
        flag=0
    else:
        py.speak("enter your choice ")
else:
    print("thank u for visiting")
