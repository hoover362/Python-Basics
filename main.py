#string method

#name = "helloniggabitch"
#print(len(name)) #prints name length
#print(name.find("h")) #finds letter position start from 0
#print(name.capitalize()) #capitalizes first letter
#print(name.upper()) #capitalizes all characters
#print(name.lower()) #lowercases all characters
#print(name.isalpha())#checks if its only alphabetical
#print(name.count("i")) #int count of digit in letter
#print(name.replace("i" , "q")) #replaces first letter with second
#print(name*3)#multiplies function

#typecasting

#x = 1   #int
#y = 2.0 #float
#z = "3" #str
#print(float(x)) #changes int into float
#print(int(y)) #changing float into int
#print(z*3) #since u cannot make a str into a int or float u have to multiply to match

#input

#name = input("Whats your name?") #Inputting a question that you must answer
#age = int(input("How old are you?: ")) #inputting a number question you must answer
#height = (float(input("How tall are you?")))
#age = age+1
#print("hello "+name) #name is the variable that states an input
#print("you are "+(str(age) + " years old"))
#print("you are "+(str(height) + " good job"))

#python math

#import math

#pi = 2 #pi isnt 2 but
#x = 1
#y = 2
#z = 3
#print(round(pi)) #rounds number closest
#print(math.ceil(pi)) #rounds number up "ceil"
#print(math.floor(pi)) #rounds number down
#print(abs(pi)) #tells absolute value aka positive version of any number
#print(pow(pi,2)) #exponent of value number
#print(math.sqrt(pi)) #square root of number
#print(max(x,y,z))
#print(min(x,y,z))

#indexing and splicing

#name = "santana james"

#start:stop#step

#first_name = name[0:7] #0 = first letter, 7 = last letter its going from first letter to the 7th letter
#last_name = name[8:13] #8 first letter of last name and 13 = the last letter
#funk_name = name[0:13:2] #step is the letter ur skipping meaning a t n would be deleted
#reversed_name = name[::-1] #reverses name

#print(first_name)
#print(last_name)
#print(funk_name)
#print(reversed_name)
#website1 = "https://santana.com"
#website2 = "https://satan.com"
#slice = slice(8, -4)#starts at the 8th letter and removes the letter starting at -4
#print(website1[slice]) #slicing the website website must be indexed
#print(website2[slice])

#else,if,elif

#age = int(input("How old are you?: "))

#if age >= 18:#if the user is 18 or older it will execute more code
    #print("You're an adult")
#if age < 99: #if they are younger than 99 then prints you pay bills
    #print("You pay bills")
#elif age == 100: #if there age is equal to 100 or more prints you old as fuck
    #print("you old as fuck")
#elif age < 2: #a second hand if statement if both are false it prints fuck you
    #print("you in the womb nigga")
#else: #if they arent 18 or older it says fuck you
    #print("fuck you")

#and if,elif,else,not,or

#temperature = int(input("What's the temperature?"))
#if temperature >= 0 and temperature <=20: #requiring two true statements in one line of code using and
    #print("its pretty cold")
#elif temperature < 0:
    #print("Its fucking freezing")
#else: #if its more than >21 degrees then it will print its not cold
    #print("Its not cold")
#temperature = int(input("What's the temperature?"))
#if not temperature == 0 and temperature <= 20: #if temp ISNT 0 or isnt less than or equal to 20 prints ts cold
 #print("Its cold")
#else: #if it isn't it prints warm
    #print("Its warm")

#while loop

#while 1==1: #1 = 1 so it will print forever
    #print("help")

#name = ""

#while len(name) == 0:
    #name = input("enter yo name nigga")
#else:
    #print("Good job")

#name = None #name none is the same as ""
#while not name: #if the name has nothing in it then
    #name = input("Whats your name") #it asks to print your name

#print("hello "+name) # then it will say hello name if you did it

#for loop


#nested loops



#for i in range(10): #will count 10 numbers starting with 0
    #print(i)

#for i in range(50, 100, 2): #first number is the start second number is the end, third number is what to count by
    #print(i)

#for i in "Santana James": #removing range will allow it to use letters only, ranging the letters between
   # print(i)

#import time
# allows you to import time methods with curent time r seconds/minutes etc

#for minutes in range(10,0, -1): #minutes/seconds is just a function name, counting down by using negatives
   # print(minutes)
    #time.sleep(0.2) #sleep is a wait time, you add time.sleep(how many seconds)
#print("Fuck off") #prints a different block of code cant be connected to for

#outer/inner nest loops

#shit = (int(input("How many rows")))
#bitch = (int(input("How many Collumns")))
#ass = (input("Enter a symbol"))

#for i in range(shit): # grabs the range of input so inputting 5 would == 5
   # for j in range(bitch): #grabs the range of the input so inputting 3 = 3
       # print(ass, end="") #you enter in a symbol then clear the terminal to print what u put
  #  print()

#break, pass, contnue

#while True: #loop for true
   # name = (input("Enter your name")) #inputs name
   # if name == "": #if name = nothing then
        #break #breaks
   # else: #if you add something it will say thanks
       # print("thanks")

#phone = "493.232.2392"

#for i in phone: # index of the pone
   # if i == ".": # if the phone has a . in it
        #continue #continues by breaking the .
    #print(i, end="") #prints the index without the . on the first line cause end=""

#for i in range(10,100):

   #if i <= 50: #less than or equal to 50
       #pass # acts as placeholde
  # else: #since pass does nothing it will skip to else by printing the index 10,100 skipping 1-50
      # print(i)

#example of password system
#import time
#import os

#def Clear():
   # os.system('cls')
#Clear()

#G = input("enter the password")
#while True:
  #  if G == "amongussex":
    #    print("good job nigger")
    #    time.sleep(0.5)
     #   break
  #  else:
      #  print("ERROR: WRONG")
      #  time.sleep(5)
      #  break
#Clear()

#print("wait")
#time.sleep(3)
#while 1==1:
   # print("HAHA NIGGER")
