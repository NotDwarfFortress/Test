#Ryan Kaplan
#Samuel Kemp
import Town as t

game_over = False
#town_name = input("Enter a town name: ")
print()

town = t.Town("Johannesburg")

while game_over == False:

    town.display()
    print()
    user_input = input ("Input the number of days that you would like to pass: ")

    if user_input.isnumeric():
        for i in range(0, int(user_input)):
            town.pass_day()

    print()




