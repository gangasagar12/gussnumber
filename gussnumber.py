import random
import os
def load_high_scores():
    if os.path.exists("high_scores.txt"):
        with open("high_scores.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    return []
def main():
    n=random.randint(1,100)
    a=-1
    gusses_count=0
    #  set up the maximum guss limit here
    max_gusses = 10
    gusses_history=[]   
    #  list to store the gusses history
    print("welcome the game of gusses number ")
    while a!=n and gusses_count < max_gusses:
        gusses_count+=1
        #  increament the gusses count
        
        try:
            a=int(input(" enter the gusses number: "))
        except ValueError:
            print("please enter a valid integer:")
            continue
        #  keep to the next iteration if input is invilid
        gusses_history.append(a)
        #  add the gusses to the history
        if a>n:
            print("please gusses the lower number: ")
        elif a<n: