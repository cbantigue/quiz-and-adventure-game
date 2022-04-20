
from PIL import Image

print("Welcome to Clo's computer quiz!")
playing = input("Attempt quiz?: ")
if playing.lower() != 'yes':
    quit()
print("Attempting quiz..")
score = 0

answer = input("Who is the best and most legendary underground rap group: ")
if answer.lower() == "drain gang":
     print("Correct.")
     score = score + 1
else:
    print("Incorrect.")
    score = score 


answer = input("define DG: ")
if answer.lower() == "drain gang":
    print("Correct.")
    score = score + 1
else: 
    print('Incorrect.')
    score = score

answer = int(input("How many people died in hamlet?: "))
image4 = Image.open('hamlet.png')
image4.show('hamlet.png)')
if answer == 9:
    print("Correct.")
    score = score + 1
else: 
    print('Incorrect')

answer = (input("Who is Bladee's bestfriend?: "))
image3 = Image.open('ecco2k.jpeg')
image3.show('ecco2k.jpeg')
if answer.lower() == 'ecco2k':
    print("Correct.")
    score = score + 1
else: 
    print('Incorrect')

answer = float(input("What is 3!/5!?: "))
if answer == 0.05 :
    print("Correct.")
    score = score + 1
else: 
    print('Incorrect')

answer = int(input("How many apostles did Jesus have?: "))
if answer == 12:
    print("Correct.")
    score = score + 1
else: 
    print('Incorrect')

answer = (input("Who is Barry Dylan?: "))
if answer.lower() == 'yung lean':
    print("Correct.")
    score = score + 1
else: 
    print('Incorrect')

answer = (input("The best grade 12 class is?: "))
if answer.lower() == 'programming 12':
    print("Correct.")
    score = score + 1
else: 
    print('Incorrect')

answer = (input("The best color is?: "))
if answer.lower() == 'periwinkle':
    print("Correct.")
    score = score + 1
else: 
    print('Incorrect')

answer = (input("The best fast food is?: "))
if answer.lower() == 'tacobell':
    print("Correct.")
    score = score + 1
else: 
    print('Incorrect')

print ("You scored " + str(score) + " out of 10 questions correctly.")
percentage = str((score/10)*100)
print("your percentage is " + str(percentage) + '%') 