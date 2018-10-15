                 				#FIRST PYTHON PROJECT......
					#	ROCK..:)...PAPER...:)....SCISSORS......:)

 # CREATED A LIST AND SEE WHAT IVE DONE....:)))
import random
import time
a=["rock","paper","scissors"]
i=0	                 			#ABOUT TO EXECUTE A WHILE LOOP     
while(i>=0):
	b=random.randint(0,2)       #IT SIMPLY GIVES RANDOM NUMBER IN THE SPECIFIED RANGE STARTING FROM 0 TO 2
	print("ROCK......PAPER.......SCISSORS.....")  #THIS IS HOW I BEGUN THE GAME TRADITIONALLY....:)
	n=str(input())
	print("THE COMPUTER CHOSE " + a[b])
	time.sleep(2)                #PRINTS THINGS ACCORDING TO THE TIME GIVEN IN PARENTHESIS..TIME IN SEC:)
	if(n==a[b]):
		print("ITS A DRAW.....")
		time.sleep(2)
	if(n=="rock" and a[b]=="paper"):
		print("COMPUTER WINS......PAPER COVERS ROCK")
		time.sleep(2)
	if(n=="rock" and a[b]=="scissors"):
		print("YOU WIN....ROCK BLUNTS SCISSORS")
		time.sleep(2)
	if(n=="paper" and a[b]=="rock"):                     #JUST CHECKING OUT ALL POSSIBILITIES....:)
		print("YOU WIN.....PAPER COVERS ROCK")
		time.sleep(2)
	if(n=="paper" and a[b]=="scissors"):
		print("COMPUTER WINS....SCISSORS CUT PAPER")
		time.sleep(2)
	if(n=="scissors" and a[b]=="rock"):
		print("COMPUTER WINS....ROCK BLUNTS SCISSORS")
		time.sleep(2)
	if(n=="scissors" and a[b]=="paper"):
		print("YOU WIN....SCISSORS CUT PAPER")
	
	
	

