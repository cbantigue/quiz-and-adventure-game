from PIL import Image 

name = input('What is your name?: ')
print ('Hello, ' + name + ' welcome to your new adventure!')

answer = input("You are on a voyage alone. Your ship is sinking. You can either wait for rescue, or seek shelter at a tiny island.\
     Type 'rescue' or 'island': ").lower()
image6 = Image.open('island.jpeg')
image6.show('island.jpeg')
if answer == 'rescue': 
    answer = input("You await for resue. Just as your ship submerges in water, a huge ship makes its way towards you.\
         Yell for help? or make comotion. Type 'yell' or 'commotion': ").lower()
       
    if answer == 'yell':
            print('You yell at the top of your lungs. The ship doesnt hear you. You lose your voice. your boat sinks and you drown.')
            print('GAME OVER')
        
    elif answer == 'commotion':
            answer = input('You wave your hands and rock your boat. The ship honks its horns and makes its way toward you. They are PIRATES\
                They take you to thier ship and agree to complete your voyage with you but only on one condition you either perform a song\
                     or walk the plank for thier amusement. Type "sing" or "plank": ')
            image1 = Image.open('pirate.jpeg')
            image1.show('pirate.jpeg')

            if answer == 'sing': 
                print("The pirates admire your eagerness to entertain them. THey decide to recruit you as a crew member for the rest of your voyage.\
                     GOOD ENDING. GAME OVER.")
            if answer == 'plank':
                print('You hesitantly walk the plank. A pirate pushes u into the water. They all laugh and leave you stranded.\
                    BAD ENDING. GAME OVER')

    else: print('Invaid option. Game over.')

elif answer == 'island': 
    answer = input("You decide to find shelter at a nearby island. Swim to the island or try to salvage your boat. \
        Type 'swim' OR 'salvage': ")
    if answer == 'swim': 
        image5 = Image.open('realshark.jpeg')
        image5.show('realshark.jpeg')
        print('You try to swim to the shore. But while you are swimming a shark plummets to the surface and devours you alive!\
            WORST ENDING > GAME OVER.')
       
    if answer == 'salvage':
        image2 = Image.open('mermaid.jpeg')
        image2.show('mermaid.jpeg')
        answer2 = input("You sail your sinking ship to the shore. A strange figure emerges from the horizon. IT IS A MERMAID!\
            She tells you she will fix your ship and magically return you home. In one condition you have to give her your soul.\
                Type 'give soul', 'don't' OR 'seduce': ")
    

        if answer2 == 'give soul': 
            print('You give her your soul. Magically your ship repairs itself. You start to feel sleepy.. Everything seems blurry unitl.. You wake up safe and secure in your bed.\
                GOOD ENDING >> GAME OVER.')

        if answer2 == "don't": 
            print('The mermaid is upset with you. She eats you alive. \
                BAD ENDING >> GAME OVER.')

        if answer2 == "seduce": 
            print("You tell her shes the prettiest thing she has ever seen. She takes you to her mermaid town.\
                You decide that life with her is better than the life you had before. she converts you into a mermaid and makes you mermaid king!\
            This is the best ending >> YOU WIN!")

    else: print('Not a valid option >> GAME OVER.')

else:
    print('Not a valid option. You lose.')
