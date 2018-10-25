                            # CLI SHOPPING CART......😁

import time                           #TO PRINT THINGS SLOWWLY...
from PIL import Image 				#THIS COMMAND HELPED ME OPEN AN IMAGE FROM A GIVEN PATH...😊
from contextlib import contextmanager #THIS AWESOME COMMAND HELPED ME IN BREAKING OUT OF NESTED LOOPS.🙏
@contextmanager
def nested_break():				#THE COMMAND WORKS BY DEFINING A FUNCTION....
    class NestedBreakException(Exception):
        pass
    try:						#THE TRY BLOCK IS USED FOR HANDLING EXCEPTIONS....
        yield NestedBreakException
    except NestedBreakException:
        pass
print("🙏......WELCOME TO YOUR SHOPPING CART.......🙏")
time.sleep(2)                    #HERE THE TIME COMMAND COMES INTO PLAY....😄
i=1
with nested_break() as mylabel:  #mylabel IS ARBITARARILY CHOSEN TO COMPLETELY BREAK OUT OF ALL LOOPS
	while(i>0):
		print("CHOOSE YOUR AREA OF INTEREST")
		time.sleep(1.5)								
		print("PRESS 1 FOR TODAYS BURNING DEALS...💥")
		time.sleep(1.5)
		print("PRESS 2 FOR DEALS ON LATEST MOBILES....🤳")
		time.sleep(1.5)
		print("PRESS 3 FOR LAPTOPS....💻")
		time.sleep(1.5)
		print("PRESS 4 FOR MEN'S SECTION.....👦")
		time.sleep(1.5)
		print("PRESS 5 FOR WOMEN'S SECTION......👧")
		time.sleep(1.5)
		a=int(input())
		
		if(a==1):
			print("TODAY'S BURNING DEALS....")
			time.sleep(1)
			print("SKULL CANDY HEADPHONES.....FROM 399\- ONLY......PRESS s TO SELECT")
			time.sleep(1)
			print("MEMORY CARDS AND PENDRIVES......FROM 350\- ONLY.....PRESS m TO SELECT")
			time.sleep(1)
			print("WOMEN'S FOOTWEAR......UPTO 60% OFF......PRESS f TO SELECT")
			time.sleep(1)
			b=str(input())
			if(b=="s"):
				print("YOU HAVE SELECTED SKULL CANDY HEADPHONES WORTH 399\-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=399*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()    #IT WORKS THROUGH THE MODULE WE CALLED IN THE BEGINNING
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								elif(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				
			if(b=="m"):	
				print("YOU HAVE SELECTED USB PENDRIVES WORTH 350\-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=350*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
						
			if(b=="f"):
				print("YOU HAVE SELECTED STANDARD WOMEN'S FOOTWARE  WORTH 399\- WITH A DISCOUNT OF 60%")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=(399-(399*0.6))*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
		if(a==2):
			print("DEALS ON LATEST MOBILE PHONES....")
			time.sleep(1)
			print("MOTO ONE POWER.....WORTH 16000/-......PRESS m TO SELECT")
			time.sleep(1)
			print("SAMSUNG GALAXY A7...WORTH 24000/-..PRESS s TO SELECT")
			time.sleep(1)
			print("OPPO F9 PRO...WORTH 21000/- ...PRESS o TO SELECT")
			time.sleep(1)
			b=str(input())
			if(b=="m"):
				print("YOU HAVE SELECTED MOTO ONE POWER WORTH 16000\-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=16000*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				
			if(b=="s"):	
				print("YOU HAVE SELECTED SAMSUNG GALAXY A7 WORTH 24000\-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=24000*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
						
			if(b=="o"):
				print("YOU HAVE SELECTED OPPO F9 PRO WORTH 21000/-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=(21000)*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
		if(a==3):
			print("DEALS ON LAPTOPS....")
			time.sleep(1)
			print("ACER PREDATOR....WORTH 1.1 LAKHS....PRESS p TO SELECT")
			time.sleep(1)
			print("ACER NITRO 5....WORTH 70000/-.....PRESS n TO SELECT")
			time.sleep(1)
			print("HP OMEN 15.....WORTH 60000/-......PRESS h TO SELECT")
			time.sleep(1)
			b=str(input())
			if(b=="p"):
				print("YOU HAVE SELECTED ACER PREDATOR WORTH 1.1 LAKHS")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=110000*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				
			if(b=="n"):	
				print("YOU HAVE SELECTED ACER NITRO 5 WORTH 70000\-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=70000*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
						
			if(b=="h"):
				print("YOU HAVE SELECTED HP OMEN 15 WORTH 60000/-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=(60000)*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				
		if(a==4):
			print("MEN'S SECTION....")
			time.sleep(1)
			print("MEN'S T SHIRT.....WORTH 500/-......PRESS s TO SELECT")
			time.sleep(1)
			print("MEN'S JEANS....WORTH 900/-.....PRESS j TO SELECT")
			time.sleep(1)
			print("MEN'S PERFUME.....WORTH 300/-......PRESS p TO SELECT")
			time.sleep(1)
			b=str(input())
			if(b=="s"):
				print("YOU HAVE SELECTED MEN'S T SHIRT WORTH 500/-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=500*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				
			if(b=="j"):	
				print("YOU HAVE SELECTED MEN'S JEANS WORTH 900\-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=900*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
						
			if(b=="p"):
				print("YOU HAVE SELECTED MEN'S PERFUME WORTH 300/-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=(300)*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
								
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				
		if(a==5):
			print("WOMEN'S SECTION....")
			time.sleep(1)
			print("WOMEN'S SAREE....WORTH 2000/-......PRESS s TO SELECT")
			time.sleep(1)
			print("WOMEN'S KURTA.....WORTH 300/-.....PRESS k TO SELECT")
			time.sleep(1)
			print("WOMEN'S FOOTWEAR......UPTO 60% OFF......PRESS f TO SELECT")
			time.sleep(1)
			b=str(input())
			if(b=="s"):
				print("YOU HAVE SELECTED WOMEN'S SAREE WORTH 2000\-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=2000*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				
			if(b=="k"):	
				print("YOU HAVE SELECTED WOMEN'S KURTA WORTH 300\-")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=300*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
						
			if(b=="f"):
				print("YOU HAVE SELECTED STANDARD WOMEN'S FOOTWARE  WORTH 399\- WITH A DISCOUNT OF 60%")
				time.sleep(1)
				print("ENTER THE NO OF PIECES U WISH TO HAVE ?")
				time.sleep(1)
				c=int(input())
				print("YOU HAVE SELECTED TO PURCHASE " + str(c) + " PIECES")
				time.sleep(1)
				d=(399-(399*0.6))*c
				print("YOUR TOTAL IS " + str(d) )
				time.sleep(1)
				print("DO YOU WISH TO PROCEED TO CHECKOUT")
				e=str(input())
				if(e=="yes"):
					print("HOW DO YOU WISH TO PAY FOR YOUR ITEMS ?...")
					time.sleep(1)
					print("SELECT 1 FOR CASH ON DELIVERY")
					time.sleep(1)
					print("SELECT 2 FOR ONLINE PAYMENT")
					time.sleep(1)
					n=int(input())
					if(n==1):
						print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
						j=0
						captcha=["not a robot","PQJRYD"]
						for j in range(0,2):
							if(j==0):
								img = Image.open("/home/ritvik/IMAGES/first.jpeg")
								img.show()
								img.close()
								w=input()
								
								if(w==captcha[0]):									
									print("PLEASE ENTER UR PERSONAL DETAILS...")
									print("ADDRESS..")
									input()
									print("PHONE NO")
									input()
									print("CITY")
									input()
									print("STATE")
									input()
									print("PIN CODE")
									input()
									print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
									print("DO U WISH TO BUY ANYTHING ELSE")
									v=input()
									if(v=="yes"):
										break
									
	
									elif(v=="no"):
										print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
									raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
				if(e=="no"):
					i=2		
				elif(n==2):
					print("ENTER UR CARD NO AND PIN")
					input()
					print("TO IDENTIFY WHETHER U ARE A HUMAN OR NOT.....PLEASE ENTER THE WORDS OF THE CAPTCHA GIVEN BELOW")
					j=0
					captcha=["not a robot","PQJRYD"]
					for j in range(0,2):
						if(j==0):
							img = Image.open("/home/ritvik/IMAGES/first.jpeg")
							img.show()
							img.close()
							w=input()
							
							if(w==captcha[0]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
								

								elif(v=="no"):
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")
								raise mylabel
										
							if(w!=captcha[0]):
								print("INVALID CAPTCHA")
								print("TRY ANOTHER ONE")
						if(j==1):
							img=Image.open("/home/ritvik/IMAGES/second.png")	
							img.show()
							img.close()	
							w=input()
							
							if(w==captcha[1]):									
								print("PLEASE ENTER UR PERSONAL DETAILS...")
								print("ADDRESS..")
								input()
								print("PHONE NO")
								input()
								print("CITY")
								input()
								print("STATE")
								input()
								print("PIN CODE")
								input()
								print("YOUR ORDER HAS BEEN SUCCESSFULLY PLACED")
								print("DO U WISH TO BUY ANYTHING ELSE")
								v=input()
								if(v=="yes"):
									break
									
								if(v=="no"):										
									print("THANK U FOR SHOPPING WITH US....HOPE TO SEE U AGAIN SOON..")				
								raise mylabel
							if(w!=captcha[1]):
								print("INVALID CAPTCHA")
								print("U CANNOT CONTINUE")
								i=0
print("YOUR ORDER NO IS " + str(random.randint(100000,1000000)))
