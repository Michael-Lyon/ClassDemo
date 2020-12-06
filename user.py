# if, loops, functions, list, dictionaries.

word = "Example"
for letter in word:
    # print(letter)
    pass


# names = ["Jane", "Baker", "Harry", "Peter", "Pan", "Ben", "Jordan"]
# for name in names:
#     if name.startswith("P"):
#         continue
#     else:
#         print(name)


balls = ["baseball", "basketball", "volleyball"]
colors = ["red", "orange", "white"]

for ball in balls:
    for color in colors:
        if (ball, color) == ("baseball", "orange") or (ball, color) == ("baseball", "red"):
            continue
        elif (ball, color) == ("basketball", "red"):
            continue
        else:
            print(color, "==>", ball)            
    else:
        print("Colors is done")
else:
    print("ball is done")
