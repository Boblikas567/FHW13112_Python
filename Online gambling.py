import random
import tkinter as tk

Gambles = 0
Jackpots = 0
Numbers = 0
root = tk.Tk()
root.title("Online casino")
root.geometry("800x600")
root.resizable(False, False)

def gamble():
    global Gambles
    global Numbers
    Gambles += 1
    slot_numbers = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
    Numbers = slot_numbers[0] *100 + slot_numbers[1] * 10 + slot_numbers[2]
    number_label.config(text=f"Numbers: {' | '.join(map(str, slot_numbers))}")
    if slot_numbers == [7, 7, 7]:
        jackpot()
    else:
        result_label.config(text="Try again! No jackpot!")
    gambled_times.config(text=f"Gambles: {Gambles}")

def jackpot():
    global Jackpots
    Jackpots += 1
    jackpots.config(text=f"Jackpots: {Jackpots}")
    result_label.config(text="JACKPOT!")

img_1 = tk.PhotoImage(file = "Slotmachine.png")
slotmachine_button = tk.Button(image = img_1, command = gamble)
slotmachine_button.pack()

welcome_label = tk.Label(text = "Press on the slotmachine to gamble! Go big, or go broke. 777 = Jackpot!", bg = "Black", fg = "White", font=("Comic Sans MS", 12))
welcome_label.pack()

gambled_times = tk.Label(text = f"Gambles: {Gambles}", bg = "Black", fg = "White", font=("Comic Sans MS", 12))
gambled_times.pack()

jackpots = tk.Label(text = f"Jackpots: {Jackpots}", bg = "Black", fg = "White", font=("Comic Sans MS", 12))
jackpots.pack()

number_label = tk.Label(text = "Numbers: - | - | -", bg = "Black", fg = "White", font=("Comic Sans MS", 12))
number_label.pack()

result_label = tk.Label(text = "Goodluck!", bg = "Black", fg = "White", font=("Comic Sans MS", 12))
result_label.pack()























root.mainloop()