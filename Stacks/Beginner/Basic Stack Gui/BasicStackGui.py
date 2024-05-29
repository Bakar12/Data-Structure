import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def display(self):
        return self.stack

    def is_empty(self):
        return len(self.stack) == 0

class StackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Operations")

        self.stack = Stack()

        self.input_value = tk.StringVar()

        # Create the input field
        self.input_entry = tk.Entry(root, textvariable=self.input_value)
        self.input_entry.pack()

        # Create the buttons
        self.push_button = tk.Button(root, text="Push", command=self.push_value)
        self.push_button.pack()

        self.pop_button = tk.Button(root, text="Pop", command=self.pop_value)
        self.pop_button.pack()

        self.display_button = tk.Button(root, text="Display", command=self.display_stack)
        self.display_button.pack()

        # Create the display area
        self.display_area = tk.Text(root, height=10, width=30)
        self.display_area.pack()

    def push_value(self):
        value = self.input_value.get()
        if value:
            self.stack.push(value)
            self.input_value.set("")  # Clear the input field
        else:
            messagebox.showwarning("Input Error", "Please enter a value to push.")

    def pop_value(self):
        popped_value = self.stack.pop()
        if popped_value is None:
            messagebox.showwarning("Stack Underflow", "The stack is empty. Cannot pop.")
        else:
            messagebox.showinfo("Popped Value", f"Popped value: {popped_value}")

    def display_stack(self):
        self.display_area.delete(1.0, tk.END)  # Clear the display area
        stack_content = self.stack.display()
        self.display_area.insert(tk.END, "\n".join(stack_content))

if __name__ == "__main__":
    root = tk.Tk()
    app = StackApp(root)
    root.mainloop()
