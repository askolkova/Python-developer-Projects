#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:05:15 2020

@author: askolkova
"""

class CoffeeMAchine():
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
    
    def run_machine(self):
        while True:
            act = input("Write action (buy, fill, take, remaining, exit):")

            if act == "remaining":
                print("The coffee machine has:")
                print(str(self.water) + " of water")
                print(str(self.milk) + " of milk")
                print(str(self.beans) + " of coffee beans")
                print(str(self.cups) + " of disposable cups")
                print(str(self.money) + " of money")

            elif act == "buy":
                act2 = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                if act2 == "1":
                    if self.water < 250:
                        print("Sorry, not enough water!")
                        continue
                    elif self.beans < 16:
                        print("Sorry, not enough coffee beans!")
                        continue
                    elif self.cups < 1:
                        print("Sorry, not enough cups!")
                        continue
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 250
                        self.beans -= 16
                        self.money += 4
                        self.cups -= 1
                elif act2 == "2":
                    if self.water < 350:
                        print("Sorry, not enough water!")
                        continue
                    elif self.milk < 75:
                        print("Sorry, not enough milk!")
                        continue
                    elif self.beans < 20:
                        print("Sorry, not enough coffee beans!")
                        continue
                    elif self.cups < 1:
                        print("Sorry, not enough cups!")
                        continue
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 350
                        self.milk -= 75
                        self.beans -= 20
                        self.money += 7
                        self.cups -= 1
                    
                elif act2 == "3":
                    if self.water < 200:
                        print("Sorry, not enough water!")
                        continue
                    elif self.milk < 100:
                        print("Sorry, not enough milk!")
                        continue
                    elif self.beans < 12:
                        print("Sorry, not enough coffee beans!")
                        continue
                    elif self.cups < 1:
                        print("Sorry, not enough cups!")
                        continue
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 200
                        self.milk -= 100
                        self.beans -= 12
                        self.money += 6
                        self.cups -= 1
                else:
                    continue
            
            elif act == "fill":
                water_add = input("Write how many ml of water do you want to add:")
                milk_add = input("Write how many ml of milk do you want to add:")
                beans_add = input("Write how many grams of coffee beans do you want to add:")
                cups_add = input("Write how many disposable cups of coffee do you want to add:")
                self.water += int(water_add)
                self.milk += int(milk_add)
                self.beans += int(beans_add)
                self.cups += int(cups_add)
    
            elif act == "take":
                print("I gave you $" + str(self.money))
                self.money = 0

            elif act == "exit":
                break

machine = CoffeeMAchine()
machine.run_machine()

    





