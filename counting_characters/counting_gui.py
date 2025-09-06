


import tkinter as tk
from tkinter import messagebox


def check_string_length():
    root = tk.Tk()
    root.title("String Length Checker")

    # Create a label and entry field for user input
    label = tk.Label(root, text="Enter a string:")
    label.pack()
    entry_field = tk.Entry(root)
    entry_field.pack()

    # Define a function to check the length of the input string
    def check_length():
        input_string = entry_field.get()
        if len(input_string) > 0:
            messagebox.showinfo("Result", f"Length: {len(input_string)}")
        else:
            messagebox.showerror("Error", "Please enter a valid string")

    # Create a button to trigger the length check
    button = tk.Button(root, text="Check Length", command=check_length)
    button.pack()

    # Start the GUI event loop
    root.mainloop()

check_string_length()