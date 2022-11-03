#!/usr/bin/env python
# coding: utf-8

# 2. Write a Boolean function that checks if a string contains ‘@’ sign and at least one ‘.’ dot (disregard the order for the sake of simplicity). Use that function to check if a user input is a valid e-mail or not.

# In[48]:


email = input("Enter Your E-Mail Address: ")
if "@" in email:
    if "." in email:
        print("Entered E-Mail is valid.")
if "." in email:
    if "@" not in email:
        print("Entered E-Mail is not valid.")
else:
    print("Entered E-Mail is not valid.")

