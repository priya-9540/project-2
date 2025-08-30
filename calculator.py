import tkinter as tk

# Initialize main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x400")

# Equation display
equation = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Function to update expression
def press(num):
    current = equation.get()
    equation.set(current + str(num))

# Function to clear
def clear():
    equation.set("")

# Function to evaluate
def equalpress():
    try:
        result = str(eval(equation.get()))
        equation.set(result)
    except:
        equation.set("Error")

# Buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val, col_val = 1, 0
for button in buttons:
    action = lambda x=button: press(x)
    if button == "C":
        action = clear
    elif button == "=":
        action = equalpress

    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), command=action)\
        .grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
