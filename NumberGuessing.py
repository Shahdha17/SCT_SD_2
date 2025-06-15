import random
import tkinter as tk
from tkinter import messagebox
class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number Game")
        master.geometry("300x200")
        master.resizable(False, False)

        # Initialize attributes that will hold Tkinter widgets
        self.label_instructions = None
        self.entry_guess = None
        self.button_submit = None
        self.label_feedback = None
        self.button_new_game = None
        
        # Create the widgets first
        self.label_instructions = tk.Label(master, text="I'm thinking of a number between 1 and 100.")
        self.label_instructions.pack(pady=10)

        self.entry_guess = tk.Entry(master)
        self.entry_guess.pack(pady=5)
        self.entry_guess.bind("<Return>", self.check_guess_event)

        self.button_submit = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.button_submit.pack(pady=5)

        self.label_feedback = tk.Label(master, text="")
        self.label_feedback.pack(pady=5)

        self.button_new_game = tk.Button(master, text="New Game", command=self.start_new_game)
        self.button_new_game.pack(pady=5)

        # Now that all widgets are created, you can call start_new_game
        # which configures these widgets.
        self.start_new_game()

    def start_new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        if self.label_feedback: # Ensure label_feedback exists before configuring
            self.label_feedback.config(text="")
        if self.entry_guess: # Ensure entry_guess exists before configuring
            self.entry_guess.delete(0, tk.END)
            self.entry_guess.focus_set()

    def check_guess_event(self, event):
        self.check_guess()

    def check_guess(self):
        try:
            guess_str = self.entry_guess.get()
            if not guess_str:
                self.label_feedback.config(text="Please enter a number.")
                return

            guess = int(guess_str)
            self.attempts += 1
            self.entry_guess.delete(0, tk.END)

            if guess < self.secret_number:
                self.label_feedback.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.label_feedback.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.secret_number} in {self.attempts} attempts.")
                self.start_new_game()
        except ValueError:
            self.label_feedback.config(text="Invalid input. Please enter a whole number.")
        except Exception as e:
            self.label_feedback.config(text=f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGameGUI(root)
    root.mainloop()