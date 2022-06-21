import random

move_list = ["F" ,"F'", "U","U'","R","R'", "L" ,"L'","D","D'"]

def scramble():
	lmove = " "
	inp = 20
	x=0
	out=""
	while x < inp :
	  move = random.choice(move_list)
	  if move == lmove: 
	    continue
	  if move == 'R'  and lmove == 'R\'' :
	    continue
	  if move == 'R\''  and lmove == 'R' :
	    continue
	  if move == 'L\''  and lmove == 'L':
	    continue
	  if move == 'L'  and lmove == 'L\'':
	    continue
	  if move == 'L\''  and lmove == 'L':
	    continue
	  if move == 'F'  and lmove == 'F\'':
	    continue
	  if move == 'F\''  and lmove == 'F' :
	    continue 
	  if move == 'U'  and lmove == 'U\'' :
	    continue   
	  if move == 'U\''  and lmove == 'U' :
	    continue
	  if move == 'D\''  and lmove == 'D' :
	    continue
	  if move=="D" and lmove=="D\'"	:
			 continue
	  if inp == 0 :
	    print("not able to print zero moves")
	    break
	  out+= move + " "
	  x = x + 1
	  lmove = move
	return out	
in_ = input("wca or list? ")
if in_=="list":
	num = int(input("How Many Scrambles? "))
	for i in range(0,num):
		print(f"{i+1}: {scramble()}")
		print()
if in_ == "wca":
	num = int(input("How Many Groups? "))
	for i in range(0,num):
			print(f"group {i+1}: ")
			for i in range(0,5):
				print(f"{i+1}: {scramble()}")
				print()
			print(f"E1: {scramble()}\n")
		
			print(f"E2: {scramble()}")	
