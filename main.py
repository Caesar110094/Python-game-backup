import random
pincode = ["1221", "9997", "8829", "6765", "9114", "5673", "0103", "4370", "8301", "1022"]
number = (random.choice (pincode))
print(number)

quesses = 0
while quesses < 10:
  userinput = input("Guess the random 4 digit number: ")

  quesses += 1    
  print ("This is your guess: %s" %(userinput))
  print ("You have used " + str(quesses) + " out of 10 guesses")
  if userinput == number:
    quesses2 = str(quesses)
    print ("You guessed it in:", quesses2 + " guesses")  

  number = str(number)
  userinput = str(userinput)
  
  if userinput.isdigit() == False:
    print ("Error: You can only use numbers")
    quesses = quesses - 1
    continue
  
  if len(userinput) != len(number):
    print("Your input is too long or too short.")
    quesses = quesses - 1
    continue



  check = ["F"] * 4
  if userinput == number and quesses >= 1:
    print("The game was beaten in " + str(quesses) +" quesses. Congratulations!")
    break
  else:
    for idx, digit in enumerate(userinput):     
      #als het nummer op de goede plek staat, print G
      if number[idx] == digit:       
        check[idx] = "G"
      
      #als het nummer vookomt, print C
      elif digit in number:
        check[idx] = "C"
      
      #anders, print F
      else:        
        check[idx] = "F"
      

  e1 = "1980"
  e2 = "1955"

  if userinput != number and userinput == e1:

     if userinput == e1:
        print ("Yeah! You found an easteregg: The birthyear of LGG!")
     quesses = quesses - 1
    
  elif userinput != number and userinput == e2:

     if userinput == e2:
        print ("Yeah! You found an easteregg: The birthyear of BNT!")
     quesses = quesses - 1

  else:
     print(*check, sep=" ")
     print ("Wrong code")
