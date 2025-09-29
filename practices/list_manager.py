# CB 1st Shopping List Manager

groceries = []

while True:
   action = input("Would you like to add an item, remove an item, mark an item as complete, or print out your list? Add/Remove/Print/Mark/Exit").strip().capitalize()
   if action == "Add":
      new_item = input("What do you want to add to your list?").strip().capitalize()
      if new_item in groceries:
         print("Item is already on shopping list.")
         continue
      else:
        groceries.append(new_item)
        print("Item added")
   elif action == "Remove":
        for x in groceries:
           print(x)
        delete_item = input("What do you want to remove from your list?").strip().capitalize()
        if delete_item not in groceries:
            print("Item is not on shopping list.")
            continue
        else:
            groceries.append(new_item)
            print("Item removed")
   elif action == "Mark":
      for x in groceries:
         print(x)
      mark_item = input("What item do you want to mark as complete?")
      if mark_item not in groceries:
         print("Item is not on shopping list.")
         continue
      else:
         groceries[mark_item] = mark_item + " \u2713"
         print("Item marked")
   elif action == "Print":
      for x in groceries:
         print(x)
   else:
      print("Goodbye!")
      break
        

    

    