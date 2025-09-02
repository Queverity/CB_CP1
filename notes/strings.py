# CB 1st Strings Notes

# String Examples
sentence = 'The quick brown fox jumps over the lazy dog!'

first_name = 'Clayton'
last_name = 'Baird'
month = 'March'
book = 'Red Sky At Morning'
food = 'yogurt'
fruits = ['Apple','Pear','Orange','Peach','Dragonfruit']

print(book)

# Checking String Length

sentence_len = (len(sentence))

book_title_len = (len(book))

list_len = (len(fruits))

fruit_len = (len(fruits[4]))


print(f"The sentence is {sentence_len} characters long.")

print(f"The book title is {book_title_len} characters long.")

print(list_len)

print(fruit_len)

# Escape Character

print('"soup" will not break the code')
print("'soup' will not break the code")
print("\"soup\" will not break the code.")
print("Inkheart is \nnot the best book ever!")
print("\t Inkheart is not the best book ever!")

# Concatenation

full_name = first_name + " " + last_name

print(full_name)

# Index

# Index numbers always start at 0.

print(full_name[2])
# When you are printing a range of characters, the second number is the end point. It will not print that index.
# If you want to slice at the start of a string, you can just leave that spot blank. If you want to go until the end of the string, you can just leave that spot blank.
print(full_name[0:7])
print(sentence[10:15])
