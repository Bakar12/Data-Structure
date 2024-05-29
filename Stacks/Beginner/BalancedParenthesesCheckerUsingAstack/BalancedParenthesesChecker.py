import tkinter as tk
from tkinter import messagebox


class ParenthesesChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Balanced Parentheses Checker")

        self.input_string = tk.StringVar()

        # Create the input field
        self.input_entry = tk.Entry(root, textvariable=self.input_string, width=50)
        self.input_entry.pack(pady=10)

        # Create the check button
        self.check_button = tk.Button(root, text="Check Balance", command=self.check_balance)
        self.check_button.pack(pady=5)

        # Create the display area
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def check_balance(self):
        input_str = self.input_string.get()
        if self.is_balanced(input_str):
            self.result_label.config(text="The parentheses are balanced.", fg="green")
        else:
            self.result_label.config(text="The parentheses are not balanced.", fg="red")

    def is_balanced(self, input_str):
        stack = []
        opening = set('([{')
        closing = set(')]}')
        matches = {')': '(', ']': '[', '}': '{'}

        for char in input_str:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack or stack[-1] != matches[char]:
                    return False
                stack.pop()

        return not stack


if __name__ == "__main__":
    root = tk.Tk()
    app = ParenthesesChecker(root)
    root.mainloop()
