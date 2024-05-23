import tkinter as tk
from tkinter import simpledialog, messagebox


# Define the BasicTextEditorGUI class
class BasicTextEditorGUI:
    # Initialize the class with a root parameter
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Text Editor")

        self.lines = []  # Initialize an empty list to store the lines of text

        # Create a text area widget
        self.text_area = tk.Text(root, wrap='word', height=20, width=50)
        self.text_area.pack(padx=10, pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Create the append button and bind it to the append_line method
        self.append_button = tk.Button(self.button_frame, text="Append Line", command=self.append_line)
        self.append_button.grid(row=0, column=0, padx=5)

        # Create the insert button and bind it to the insert_line method
        self.insert_button = tk.Button(self.button_frame, text="Insert Line", command=self.insert_line)
        self.insert_button.grid(row=0, column=1, padx=5)

        # Create the delete button and bind it to the delete_line method
        self.delete_button = tk.Button(self.button_frame, text="Delete Line", command=self.delete_line)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Create the display button and bind it to the display_text method
        self.display_button = tk.Button(self.button_frame, text="Display Text", command=self.display_text)
        self.display_button.grid(row=0, column=3, padx=5)

    # Define the append_line method
    def append_line(self):
        text = self.get_text_input("Append Line", "Enter the text to append:")
        if text is not None:
            self.lines.append(text)  # Append the text to the lines list

    # Define the insert_line method
    def insert_line(self):
        line_number = self.get_line_number_input("Insert Line", "Enter the line number to insert at:")
        if line_number is not None:
            text = self.get_text_input("Insert Line", "Enter the text to insert:")
            if text is not None:
                # Check if the line number is valid, then insert the text at the specified line number
                if 0 < line_number <= len(self.lines) + 1:
                    self.lines.insert(line_number - 1, text)
                else:
                    messagebox.showerror("Error", f"Invalid line number {line_number}")

    # Define the delete_line method
    def delete_line(self):
        line_number = self.get_line_number_input("Delete Line", "Enter the line number to delete:")
        if line_number is not None:
            # Check if the line number is valid, then delete the line at the specified line number
            if 0 < line_number <= len(self.lines):
                self.lines.pop(line_number - 1)
            else:
                messagebox.showerror("Error", f"Invalid line number {line_number}")

    # Define the display_text method
    def display_text(self):
        self.text_area.delete(1.0, tk.END)  # Clear the text area
        # Loop through the lines list and insert each line into the text area
        for idx, line in enumerate(self.lines):
            self.text_area.insert(tk.END, f"{idx + 1}: {line}\n")

    # Define the get_text_input method
    def get_text_input(self, title, prompt):
        return simpledialog.askstring(title, prompt)  # Display a dialog to get text input from the user

    # Define the get_line_number_input method
    def get_line_number_input(self, title, prompt):
        try:
            return simpledialog.askinteger(title, prompt)  # Display a dialog to get a line number from the user
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid line number.")
            return None


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BasicTextEditorGUI(root)
    root.mainloop()
