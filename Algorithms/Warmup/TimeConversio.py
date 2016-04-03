import sys

if name == "_main_":
    time = raw_input().strip().split(':')
    if time[2][2] == 'A':
        if time[0]=='12':
            print ('00:'+time[1]+':'+time[2])[:-2]
        else:
            print (':'.join(time))[:-2]    
    else:
        if time[0]=='12':
            print (':'.join(time))[:-2] 
        else:
            hour = int(time[0])+12
            print (str(hour) + ":" + time[1] + ":" + time[2])[:-2]
