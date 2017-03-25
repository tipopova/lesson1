name = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

i = 0
l_name = name.index("Валера")
while True:
    if i == l_name:
        break
    else:
        print (name[i])
        i = i+1
print("Валера нашелся!")