import sys
from math import atan, floor


flag=0
temp=0
counter=0.0
xlst=[]
ylst=[]
myfile = "angle.txt"


line = sys.stdin.readline()
line = sys.stdin.readline()
line = sys.stdin.readline()
line = sys.stdin.readline()
line = sys.stdin.readline()
line = sys.stdin.readline()
line = sys.stdin.readline()
line = sys.stdin.readline()
line = sys.stdin.readline()
counter3 = 0;
while True:
    counter3 = counter3+1;
    line = sys.stdin.readline()
    if line:
        (x, y) =[float(s) for s in line.split(',')]
        x=x*1080
        y=1920-(y*1920)
        
        if(x !=0 and x > temp-5):
            # this is the setup
            temp = x
            xlst.append(x)
            ylst.append(y)
            
            counter=counter+1
        elif (x != 0 and x < temp-5):
            # time to get the angle
            xp=x
            yp=y
            yt=0
            xt=0
            # Damn type checking
            counter = counter // 2
            counter = floor(counter)
            counter = int(counter)

            for i in range(1, counter):
                xt=xlst.pop()
                yt=ylst.pop()
            
            o=yp-yt
            a=xp-xt
            angle=atan(o/a)*(180/3.14)
            print(angle)
            
            angle = int(angle)
            if angle < 0:   
                angle = angle * -1
            data = "%s" % (angle)
            cou= "%s" % (counter3)

            print(angle)

            file = open(myfile, 'w')
            file.write(cou)
            file.write('\n')
            file.write(data)
            file.close()

             
            #clean up to restart
            temp = 0
            del xlst[:]
            del ylst[:]
            counter=0
    else:
        continue



