import time

# pisa.py
name = input("What is your name?\n")
print("Hi, ", name,"\n")
num = input("How many pisa do you want?\n")
print("Here you are!")
drink = input('Would you like some drinks?\n')
print("你点的是",drink,"请稍后... ...")
time.sleep(3)
print("你点的",drink,"好了！请享用!")