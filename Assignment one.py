#Problem one
#Input requests users name
name = input("What's your name? ")
#Print function with greeting to user's input variable
print("Nice to meet you " + name + "!")

#Problem 2
#User imputs the name in the "Z" Variable
z= input("whats your name: ")
#Prints the following phrase and counts the number of letters in the "Z" input variable
print("your name has", len(z), "letters in it.",z,"is a cool name dude!")

#Problem 3
#Program asks the usrer for the following, noun, verb, adverb, adjective, and puts them into a phrase
noun= input("give me a noun ")
verb =input("give me a verb ")
adverb = input("give me an adverb ")
adjective= input("give me an adjective ")
#prints out the phrase below, and congrats the user on being funny.
print("did you", verb,"your", adjective, noun, adverb,"?.", "Congrats your as funny as a one legged pirate")

#problem 4
#Asks the user for two random numbers and perfroms the four basic math operations
x= input("give me a number ")
y= input("give me another number ")
X=int(x)
Y=int(y)
#pritns the four basic operations from the above random numbers inputed by the user.
print (X, " + ", Y, " = ", X+Y)
print (X, " - ", Y, " = ", X-Y)
print (X, " * ", Y, " = ", X*Y)
print (X, " / ", Y, " = ", X/Y)

#problem 5
x= input("What is your current age?  ")
y= input("What age would you like to retire? ")
X=int(x)
Y=int(y)
print ("You have", Y-X, "years left until you can retire.")
import datetime
now = datetime.datetime.now()
print("It's", now.year, "so you can retire in", now.year+(Y-X))
#Problem 6
#asks user for length of a room and width to calculate area and area in sq meters
x= input("What is the length of the room in feet? ")
y= input("What is the width of the room in feet? ")
X=int(x)
Y=int(y)
#performs the calculations for Sqaure feet and for Square meters
SF= Y*X
SM=SF*0.092903
#pritns the users input and gives the calculations back to the user in a print format
print("You entered", X ,"feet by", Y ,"feet for length and width")
print(SF, "square feet")
print(SM, "square meters")

#problem 7
#program figures out how many slices you've got for you and your cheap friends.
x = input("how many people you got? ")
y = input("how many pizza's you get hommie? ")
z = input("how many slices each pizza got? ")
#convents strings into integers for calculations
X=int(x)
Y=int(y)
Z=int(z)
#performs the math for figuring out number of slices per person and leftover slices
yz= (Y*Z)
ZAA= (Y%X)
Zep = (yz-ZAA)
#prints out answers to inputs asked by program
print( X, "people with", Y, "pizza's")
print("each mofo get's ", Zep, "slices")
print("you got", ZAA, "slices left over")
#problem 8  
#Problem 9
#Ask user for three item prices, and quantitys and calculates cost, with tax
#User inputs informaiton for price and Quantity
Item= input("enter price of item 1 $:")
Quantity= input("enter the quantity of item 1:")
Item2= input("enter the price of item 2 $:")
Quantity2= input("enter the quantity of item 2:")
Item3= input("enter the price of item 3 $:")
Quantity3= input("enter the quantity of item 3:")
#Converts user inputs into floats for $value
i1=float(Item)
q1=float(Quantity)
i2=float(Item2)
q2=float(Quantity2)
i3=float(Item3)
q3=float(Quantity3)
#Calculate the subtotal, tax, and total for the floaats
Subtotal = ((i1*q1)+(i2*q2)+(i3*q3))
tax= Subtotal*.055
total= Subtotal + tax
#Prints output for user Subtotal, tax and total
print("Subtotal", "$",Subtotal)
print("tax", "$",tax)
print("total", "$",total)

#problem 10
P= input("how much money do you want to invest? ")
T= input("how many years do you want to put it away for? ")
I= input("what is the rate of return %? ")
p= int(P)
t= int(T)
i= float(I)
In= i/100
Value = p*(1+t*In)
print("after", t, "years at", i,"%","you will have", "$",Value)
