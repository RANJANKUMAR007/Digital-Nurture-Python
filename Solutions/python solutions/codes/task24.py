from math import *
def show_math_values(num):
    if num < 0:
        print("Invalid input")
        return
    print("Square Root:", sqrt(num))
    print("Power:", pow(num, 2))
    print("Pi Value:", pi)
num=int(input())
show_math_values(num)