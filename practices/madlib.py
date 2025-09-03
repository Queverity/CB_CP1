# CB 1st Madlib

print("This is a madlib game. You will be giving words in a reponse to a prompt to fill in a story that you do not know.")

adjective_one = input("Enter an adjective: \n")

animal = input("Enter an animal: \n")

animal_name = input("Enter an animal name: \n").capitalize

item = input("Enter an item: \n")

place = input("Enter a place: \n")

human_name = input("Enter a human name: \n").capitalize

adjective_two = input("Enter another adjective: \n")

adjective_three = input("Enter one last adjective: \n")

monster_one = input("Enter a creature: \n")

monster_two = input("Enter another creature: \n")

story = "One day, a brave " + adjective_one + " " + animal + " named " + animal_name + " went on an adventure to find the legendary " + item + ". It was said that the " + item + " could grant anyone who touched it the power to become the strongest " + animal + " in the world. But there was a catch: the " + item + " was hidden in the deepest part of the " + place + ". " + human_name + " began the journey with their trusty " + adjective_one + " " + animal + " sidekick, " + human_name + "'s best friend. They traveled through " + place + ", where they encountered fierce creatures like the " + adjective_two + " " + monster_one + " and the terrifying " + adjective_three + " " + monster_two + ". But with courage and determination, they continued on, hoping to find the " + item + " and claim its power for themselves. They died, never reaching their goal. Sounds like a skill issue to me."

print(story)