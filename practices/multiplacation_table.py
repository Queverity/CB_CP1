# CB 1st Multiplacation Table

row1 = ""
row2 = ""
row3 = ""
row4 = ""
row5 = ""
row6 = ""
row7 = ""
row8 = ""
row9 = ""
row10 = ""
row11 = ""
row12 = ""

column = 1
row = 1

for i in range(1,13):
    product = str(column * row)
    match column:
        case 1:
            row1 + (product + " ")
            row += 1

print(row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9 + row10 + row11 + row12)
