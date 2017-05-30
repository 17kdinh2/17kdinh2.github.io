import time
import random
#welcoming the user
name = raw_input("What is your name? ")

print "Hello, " + name, "lets play hangman!"

#the space part
print " "

#wait for 1 second
time.sleep(1)
print "Start guessing..."
time.sleep(0.5)

#setting the word
WORDS= ["xylophone", "bookmark", "python", "jumble", "easy", "difficult", "answer",  "xylophone", "happiness", "html"]
word= random.choice(WORDS)
#makes the space for the name
guesses = ''

turns = 10
#check if the turns are more than zero
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
        # print out the character
            print char,    
        else:
        # if not found, print a dash
            print "_",     
        # add to failures
            failed += 1    
    if failed == 0:        
        print "You won"  
    # finish the script
        break              
    print
    
    guess = raw_input("guess a character:") 
    # set the players guess to guesses
    guesses += guess                    

    if guess not in word:  
        turns -= 1        
    # print wrong
        print "Wrong"    
    # how many turns are left
        print "You have", + turns, 'more guesses' 
    # if the turns are equal to zero
        if turns == 0:           
            print "You Lose"  