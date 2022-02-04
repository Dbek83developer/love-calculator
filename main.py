# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#lowerCase letters
lower_name1 = name1.lower()
lower_name2 = name2.lower()
#counting T R U E
true_number = lower_name1.count("t") + lower_name1.count("r") + lower_name1.count("u") + lower_name1.count("e") + lower_name2.count("t") + lower_name2.count("r") + lower_name2.count("u") + lower_name2.count("e")

#counting L O V E
love_number = lower_name1.count("l") + lower_name2.count("l") + lower_name1.count("o") + lower_name2.count("o") + lower_name1.count("v") + lower_name2.count("v") + lower_name1.count("e") + lower_name2.count("e")

#love score
love_score =str(true_number) + str(love_number)

#usloviya
if int(love_score) < 10 or int(love_score) > 90: 
  print("Your score is " + love_score +", you go together like coke and mentos.")
elif   int(love_score) >= 40 or int(love_score) <= 50:
  print("Your score is " + love_score + ", you are alright together.")
else:
  print("Your score is " + love_score + ".")  
