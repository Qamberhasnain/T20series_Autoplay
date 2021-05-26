'''This code is created by Qamber Hasnain Student of Lovely Professional University\n Section:- K19EG\n Roll no.:- B64\n This will give you results of three matches and announce the winner of the series played between any two random teams selected from allteam list\n All the numbers taken are random but results will be logical.'''
import random

allteam=["BANGLADESH","INDIA","PAKISTAN","SRILANKA","AFGHANISTAN","ENGLAND","NEWZEALAND","SOUTH AFRICA","WINDIES","AUSTRALIA"]

tosswin=["BAT","BALL"]

team1=allteam[random.randint(0,(len(allteam)-1))]

team2=allteam[random.randint(0,(len(allteam)-1))]

# team1 team2 are for randomly choosing cricket team.
matchno=["1st ","2nd ","3rd "]

counter=0

team1win=0

team2win=0

#team1win and team2win are initial win

#match(p,q) main function of the code
def match(p,q):
 global team1win
 global team2win
 global counter
#global declaration to change their value inside function  
 x=random.randint(0,1)
 # random int
 y=tosswin[random.randint(0,1)]
 #randomly choosing bat ball 
 team1run=str(random.randint(80,280))
  #t1run lowest 80 highest 280 as afg scored 278 in t20
 rteam2run=str(random.randint(80,(int(team1run)+6)))
 #rt2run means relative to the team1 run if t1 bat first  . it is for not exceeding t1+6 runs when t2 bat lasts
 team2run=str(random.randint(80,280))
 rteam1run=str(random.randint(80,(int(team2run)+6)))
#similar to t1
 team1wicket=str(random.randint(0,10))
 team2wicket=str(random.randint(0,10))
 #wicket from 0-10
 if x:
 # if 0 false if 1 true gets priority p1
  print(matchno[counter]+" t20 \n")
  print (p+" Won the toss and elected to "+y+" first . \n ")
  
  if y=="BAT":
  #bat then t1 first
   print(team1+"   " + team1run +" - "+team1wicket+"    "+rteam2run+" - "+team2wicket+"   "+team2)
   if int(team1run) > int(rteam2run):
    print(team1 +" won by "+str(int(team1run) - int(rteam2run)) +" runs \n \n")
    team1win+=1
    #incrementing team1win if t1 wins to calculate who wins the series  
   elif int(rteam2run) > int(team1run):
     print(team2 +" won by "+str(10-int(team2wicket)) +" wickets \n \n")
     team2win += 1
   else:
     print("DRAW")
  else:
  #for choosing ball  
   print(team2+"   " + team2run +" - "+team2wicket+"    "+rteam1run+" - "+team1wicket+"   "+team1)
   if int(team2run) > int(rteam1run):
    print(team2 +" won by "+str(int(team2run) - int(rteam1run)) +" runs \n ")
    team2win +=1
   elif int(rteam1run) > int(team2run):
    print(team1 +" won by "+str(10-int(team1wicket)) +" wickets \n ")
    team1win +=1
   else:
     print("DRAW")
 else:
 #if 0 happens.
  print( matchno[counter] +"t20 \n")
  print (q+" Won the toss and elected to "+y +" first . \n \n")

  if y=="BAT":
   print(team2+"   " + team2run +" - "+team2wicket+"    "+rteam1run+" - "+team1wicket+"   "+team1)
   if int(team2run) > int(rteam1run):
    print(team2 +" won by "+str(int(team2run) - int(rteam1run)) +" runs \n \n")
    team2win +=1
   elif int(rteam1run) > int(team2run):
    print(team1 +" won by "+str(10-int(team1wicket)) +" wickets \n \n")
    team1win +=1
   else:
     print("DRAW")
  else:
   print(team1+"   " + team1run +" - "+team1wicket+"    "+rteam2run+" - "+team2wicket+"   "+team2)
   if int(team1run) > int(rteam2run):
    print(team1 +" won by "+str(int(team1run) - int(rteam2run)) +" runs \n \n")
    team1win+=1
   elif int(rteam2run) > int(team1run):
     print(team2 +" won by "+str(10-int(team2wicket)) +" wickets \n \n")
     team2win += 1
 counter+=1
   


x=1
while x<=3:
#calling function 3 times
 match(team1,team2)
 x+=1
 
if team1win >team2win:
#calculating who wins the series  
 print("HURRAH ! "+team1+" wins the series by "+str(team1win)+"-"+str(team2win))
else:
 print(" HURRAH! "+team2+" wins the series by "+str(team2win)+"-"+str(team1win))