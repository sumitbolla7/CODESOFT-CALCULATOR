import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == 'Addition':
            result = num1 + num2
        elif operation == 'Subtraction':
            result = num1 - num2
        elif operation == 'Multiplication':
            result = num1 * num2
        elif operation == 'Division':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets for input
entry_num1 = tk.Entry(root, width=10)
entry_num2 = tk.Entry(root, width=10)

# Dropdown for operation choice
operation_var = tk.StringVar()
operation_var.set("Addition")  # Default operation
operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']
operation_menu = tk.OptionMenu(root, operation_var, *operations)

# Button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Label to display the result
result_label = tk.Label(root, text="Result: ")

# Grid layout
entry_num1.grid(row=0, column=0, padx=10, pady=10)
operation_menu.grid(row=0, column=1, padx=10, pady=10)
entry_num2.grid(row=0, column=2, padx=10, pady=10)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)
result_label.grid(row=2, column=0, columnspan=3)

# Start the main loop
root.mainloop()
