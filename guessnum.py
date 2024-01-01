import random
import tkinter as tk
from tkinter import ttk, messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("Easy")  
        
        self.attempts = 0

        self.label_difficulty = tk.Label(master, text="Select Difficulty:")
        self.label_difficulty.pack()

        self.difficulty_menu = ttk.Combobox(master, textvariable=self.difficulty_var, values=["Easy", "Medium", "Hard"])
        self.difficulty_menu.pack()

        self.label = tk.Label(master, text="Enter your guess:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.master.bind('<Return>', lambda event: self.check_guess())

    def check_guess(self):
        difficulty = self.difficulty_var.get().lower()
        self.set_difficulty_range(difficulty)

        guess = self.get_user_guess()

        if guess is not None:
            self.attempts += 1

            if guess == self.secret_number:
                self.show_message(f"Congratulations! You guessed the number in {self.attempts} attempts.")
                self.reset_game()
            elif guess < self.secret_number:
                self.show_message("Too low! Try again.")
            else:
                self.show_message("Too high! Try again.")

    def set_difficulty_range(self, difficulty):
        if difficulty == 'easy':
            self.min_number, self.max_number = 1, 50
        elif difficulty == 'medium':
            self.min_number, self.max_number = 1, 100
        elif difficulty == 'hard':
            self.min_number, self.max_number = 1, 200

        if hasattr(self, 'secret_number'):
            self.secret_number = random.randint(self.min_number, self.max_number)
        else:
            self.secret_number = random.randint(1, 100)

    def get_user_guess(self):
        try:
            return int(self.entry.get())
        except ValueError:
            self.show_message("Invalid input. Please enter a valid number.")
            return None

    def show_message(self, message):
        messagebox.showinfo("Result", message)

    def reset_game(self):
        self.attempts = 0
        self.entry.delete(0, 'end')
        self.set_difficulty_range(self.difficulty_var.get().lower())

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
