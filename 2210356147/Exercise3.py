#!/usr/bin/env python
# coding: utf-8

# 3. Guessing game! Pick a number randomly. While user does not guess the number correctly give an instruction about the number and take another guess from user.

# In[ ]:


import random
number=random.randint(1,100)
guess=int(input("Please enter a number: "))
if guess == number:
    print("You picked the correct number.")
while guess != number:
    if guess<number:
        print("Increase your number.")
    if number<guess:
        print("Decrease your number.")
    print("Guessed number is not correct.")
    guess=int(input("Please enter a number: "))

