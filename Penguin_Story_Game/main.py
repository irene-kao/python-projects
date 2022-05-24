print("Welcome to Penguin Island.")
print("Your mission is to find the Sumo penguin.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

step1 = input('\nYou\'ve been designated captain of a boat to Antarctica. While steering, you arrive at a fork in the sea. Do you want to steer east or west? \n\nType "east" or "west": \n').lower()

if step1 == "west":
    step2 = input('Great! You arrived at Antarctica. However, the landing area passage is currently inaccessible. Do you want to swim to shore or wait for the water to recede? \n\nType "swim" or "wait": \n').lower()
    if step2 == "swim":
        step3 = input('Congrats! You made it onto the ice. You turn around and see that an iceberg has hit your boat and waiting would not have been good. You see 3 colored igloos up ahead. One of them will bring you to the penguin. Which one do you want to pick? \n\nType "red", "blue", or "yellow": \n').lower()
        if step3 == "yellow":
          print("Yay! You found the sumo penguin.")
          print('''
               _
             ('v')
            //-=-\\
            (\_=_/)
             ^^ ^^
            ''')
        elif step3 == "blue":
            print("Oh no, it's a seal. Run!!")
        else:
            print("Oh no!")
            print('''
                     ===
          (`\,;+++;,/`)
         (- (((^.^))) -)
        (-   ))\-/((   -)
        (-   (() ())   -)
         \   `/`@`\`   /
          \  /     \  /
           \/       \/
           /         \
          /_/_/_|_\_\_\  
          ''')
    else:
        print("Oh no. A giant iceberg hit your boat when you were waiting and sank your boat.")
else:
    print("Game over. You ran into a storm, and your boat sank.")