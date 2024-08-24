import tkinter as tk
import random
computer =random.choice([-1,0,1])
def main():
    root=tk.Tk()
    root.title("Greeting Window")
    root.geometry("300x200")
    greeting_label=tk.Label(root,text="Let`s play the game",font=("Arial",18),fg="blue")
    greeting_label.pack(expand=True) 
    root.mainloop()
    return True 
main()                       
print("Let`s start playing the snake , water , gun game ")
print("Enter `s` for snake. ")
print("Enter `w` for water. ")
print("Enter `g` for gun. ")
youstr=input("Enter your choice ")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]
reverseDict={1:"snake",-1:"water",0:"gun"}
print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")
if(computer==you):
    print("It`s a draw")
else:
    if((computer-you == -1) or (computer-you==2)):
        print("You lose")
    else:
        print("You win")
    