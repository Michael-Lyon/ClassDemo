beans = 300
rice = 500
beef = 750
egg = 200
chioma_money = 1_500

food = input("What do you want: ")
if food.lower() == "beans":
    print(f"It costs {beans}NGN")
    ask = input("Buying? ")
    if ask.lower() == "yes":
        chioma_money = chioma_money - beans
        print(f"ping ping!! you have {chioma_money} left in your account.")



