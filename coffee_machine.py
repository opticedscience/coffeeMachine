# Write your code here
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")

# n=int(input("Write how many cups of coffee you will need:"))
# print("For {} cups of coffee you will need:".format(n))
# water_amount=200*n
# milk_amount=50*n
# coffee_amount=15*n
#
# print("{} ml of water".format(water_amount))
# print("{} ml of milk".format(milk_amount))
# print("{} g of coffee beans".format(coffee_amount))

# water=int(input())//200
# milk=int(input())//50
# coffee=int(input())//15
# num=int(input())

# total=min(water,milk,coffee)
#
# if total>num:
#     print('Yes, I can make that amount of coffee (and even {} more than that'.format(total-num))
# elif total==num:
#     print('Yes, I can make that amount of coffee')
# else:
#     print('No, I can make only {} cups of coffee'.format(total))
class coffeeMachine:
    def __init__(self,water=400,milk=540,coffee=120,cups=9,money=550):
        self.water=water
        self.milk=milk
        self.coffee=coffee
        self.cups=cups
        self.money=money
        self.run()

    def run(self):
        while True:
            action = input('Write action (buy, fill, take,remaining,exit):\n')

            if action == 'buy':
                print('What do you want to buy? 1 - espresso, 2 - latte,'
                      ' 3 - cappuccino, back - to main menu:')
                choice = input()
                if choice == '1':
                    if self.water - 250<0:
                        print('Sorry, not enough water!')
                        continue
                    elif self.coffee - 16<0:
                        print('Sorry, not enough coffee!')
                        continue
                    else:
                        self.water-=250
                        self.coffee-=16
                        self.money += 4
                        print('I have enough resources, making you a coffee!')

                elif choice == '2':
                    if self.water - 350<0:
                        print('Sorry, not enough water!')
                        continue
                    elif self.coffee - 20<0:
                        print('Sorry, not enough coffee!')
                        continue
                    elif self.milk-75<0:
                        print('Sorry, not enough milk!')
                        continue
                    else:
                        self.water-=350
                        self.coffee-=20
                        self.milk-=75
                        self.money += 7
                        print('I have enough resources, making you a coffee!')
                elif choice == '3':
                    if self.water - 200<0:
                        print('Sorry, not enough water!')
                        continue
                    elif self.coffee - 12<0:
                        print('Sorry, not enough coffee!')
                        continue
                    elif self.milk-100<0:
                        print('Sorry, not enough milk!')
                        continue
                    else:
                        self.water-=200
                        self.coffee-=12
                        self.milk-=100
                        self.money += 6
                        print('I have enough resources, making you a coffee!')
                elif choice=='back':
                    continue
                self.cups -= 1
            elif action == 'fill':
                print('Write how many ml of water do you want to add:')
                self.water += int(input())
                print('Write how many ml of milk do you want to add:')
                self.milk += int(input())
                print('Write how many grams of coffee beans do you want to add:')
                self.coffee += int(input())
                print('Write how many disposable cups of coffee do you want to add:')
                self.cups += int(input())
            elif action == 'take':
                print('\nI gave you ${}\n'.format(self.money))
                self.money = 0
                continue

            elif action=='remaining':
                print('''The coffee machine has:
                    {} of water
                    {} of milk
                    {} of coffee beans
                    {} of disposable cups
                    {} of money'''.format(self.water,self.milk, self.coffee, self.cups, self.money))

            elif action=='exit':
                break
            else:
                print('wrong input!')

coffeeMachine()
