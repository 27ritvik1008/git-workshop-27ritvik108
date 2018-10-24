                 				#FIRST PYTHON PROJECT......
					#	ROCK..:)...PAPER...:)....SCISSORS......:)

 # CREATED A LIST AND SEE WHAT IVE DONE....:)))
import random
import time            #WISH TO PRINT THINGS SLOOOOWLYYYY...
print("LETS PLAY ROCK.....PAPER.....SCISSORS......")
time.sleep(1)
k=int(input("HOW MANY GAMES DO U WISH TO PLAY \n"))
a=["rock","paper","scissors"]
p=["🗿","📃","✂"]
i=0	                 			#ABOUT TO EXECUTE A WHILE LOOP     
user_score=0
comp_score=0
while(i<=(k-1)):
	b=random.randint(0,2)       #IT SIMPLY GIVES RANDOM NUMBER IN THE SPECIFIED RANGE STARTING FROM 0 TO 2
	print("ROCK...🗿...PAPER...📃....SCISSORS..✂..")  #THIS IS HOW I BEGUN THE GAME TRADITIONALLY....:)
	time.sleep(2)
	n=str(input())
	print("THE COMPUTER CHOSE " + p[b])
	time.sleep(2)                #PRINTS THINGS ACCORDING TO THE TIME GIVEN IN PARENTHESIS..TIME IN SEC:)
	if(n==a[b]):
		print("ITS A DRAW.....")
		time.sleep(2)
	if(n=="rock" and a[b]=="paper"):
		print("COMPUTER WINS......PAPER COVERS ROCK")
		time.sleep(2)
		comp_score=comp_score+1
	if(n=="rock" and a[b]=="scissors"):
		print("YOU WIN....ROCK BLUNTS SCISSORS")
		time.sleep(2)
		user_score=user_score+1
	if(n=="paper" and a[b]=="rock"):                     #JUST CHECKING OUT ALL POSSIBILITIES....:)
		print("YOU WIN.....PAPER COVERS ROCK")
		time.sleep(2)
		user_score=user_score+1
	if(n=="paper" and a[b]=="scissors"):
		print("COMPUTER WINS....SCISSORS CUT PAPER")
		time.sleep(2)
		comp_score=comp_score+1
	if(n=="scissors" and a[b]=="rock"):
		print("COMPUTER WINS....ROCK BLUNTS SCISSORS")
		time.sleep(2)
		comp_score=comp_score+1
	if(n=="scissors" and a[b]=="paper"):
		print("YOU WIN....SCISSORS CUT PAPER")
		user_score=user_score+1
	i=i+1
print("YOUR SCORE = " + str(user_score))
print("COMP SCORE = " + str(comp_score))
if(user_score>comp_score):
	print("USER WINS")
else:
	print("COMPUTER WINS")
	
	

