# CB 1st Shopping List Manager
groceries = []

print("Shopping List")
while True:
   print("Chose one of the following options (type in as follows, no numbers)")
   action = input("1. Add\n2. Remove\n3. Mark\n4. Print\n5. Clear\n6. Exit\n").strip().capitalize()
   
   if action == "Add":
      item = input("What do you want to add to your list?").strip().capitalize()
      if item in groceries:
         print(f"{item} is already on shopping list.")
         continue
      else:
        groceries.append(item)
        print(f"{item} added")
        
   elif action == "Remove":
        if groceries == []:
           print("List is empty.")
           continue
        print("Current list:")
        for x in groceries:
           print(x)
        item = input("What do you want to remove from your list?").strip().capitalize()
        if item not in groceries:
            print(f"{item} is not on shopping list.")
            continue
        else:
            groceries.remove(item)
            print(f"{item} removed")

   elif action == "Mark":
      if groceries == []:
         print("List is empty.")
         continue
      else:
         print("Current list:")
         for x in groceries:
            print(x)
         item = input("What item do you want to mark as complete?").strip().capitalize()
         if item  not in groceries:
            print(f"{item} is not on shopping list.")
            continue
         else:
            item_index = groceries.index(item)
            groceries[item_index] = item + " \u2713"
            print(f"{item} marked")

   elif action == "Print":
      if groceries == []:
         print("List is empty.")
         continue
      else:
         print("Current list:")
         for x in groceries:
            print(x)
   
   elif action == "Clear":
      if groceries == []:
         print("List is already empty.")
      else:
         confirm = input("Confirm? If confirmed, the list will be emptied. Y/N").strip().capitalize()
         if confirm == "N":
            print("Task canceled, list has not been cleared.")
            continue
         elif confirm == "Y":
            groceries = []
            print("List cleared.")
         else:
            print("Invalid answer, list not cleared")
            continue

   elif action == "Exit":
      print("Goodbye!")
      break

   else:
      print("Invalid answer")
      continue