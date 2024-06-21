import tkinter as tk
import math

# Define the stack class
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

# This is a list of operands that are alloweed
operandsRequired = {
    "+": 2,
    "-": 2,
    "*": 2,
    "/": 2,
    "^": 2,
    "sin": 1,
    "cos": 1,
    "tan": 1,
    "log": 1,
    "ln": 1,
    "sqrt": 1,
    "cbrt": 1,
    "||": 1,
    "!": 1,
    "%": 2
}

# Defines the Order of Precedence of Operators
orderPrecedence = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
    "sin": 4,
    "cos": 4,
    "tan": 4,
    "log": 4,
    "ln": 4,
    "sqrt": 4,
    "cbrt": 4,
    "||": 5,
    "!": 5,
    "%": 6
}

calc_history = []
calc_history_top = -1
operation = None
stk = Stack()

display = None  # Define the 'display' variable
calc_history_display = None  # Define the 'calc_history_display' variable

root = tk.Tk()
root.title("Calculator")

root.resizable(False, False)

num_entry = tk.Entry(root, width=60, borderwidth=5)
num_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def clear_button():
    num_entry.delete(0, tk.END)

def button_click(number):
    current = num_entry.get()
    num_entry.delete(0, tk.END)
    if number == '.' and '.' in current:
        num_entry.insert(0, current)  # Ignore the decimal point if one already exists
    else:
        num_entry.insert(0, str(current) + str(number))

def backspace():
    current = num_entry.get()
    # Remove the last character from the current input
    num_entry.delete(0, tk.END)
    num_entry.insert(0, current[:-1])
    
def button_addition_click():
    push_operator("+")

def button_subtraction():
    push_operator("-")

def button_multiplication():
    push_operator("*")

def button_division():
    push_operator("/")
    
def button_exponent():
    push_operator("^")
    
def button_sine():
    current = num_entry.get()
    if current == '':
        num_entry.insert(0, "Error: No input")
        return

    try:
        # Convert the input to a float and then to radians
        radian = math.radians(float(current))
        result = math.sin(radian)
        statement = f"sin({current}) = {result}"
        update_calc_history(statement)
        
        num_entry.delete(0, tk.END)
        num_entry.insert(0, str(result))
        
    except ValueError as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
    except Exception as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")

def button_cosine():
    current = num_entry.get()
    if current == '':
        num_entry.insert(0, "Error: No input")
        return

    try:
        # Convert the input to a float and then to radians
        radian = math.radians(float(current))
        result = math.cos(radian)
        statement = f"cos({current}) = {result}"
        update_calc_history(statement)
        
        num_entry.delete(0, tk.END)
        num_entry.insert(0, str(result))
        
    except ValueError as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
    except Exception as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")

def button_tangent():
    current = num_entry.get()
    if current == '':
        num_entry.insert(0, "Error: No input")
        return

    try:
        # Convert the input to a float and then to radians
        radian = math.radians(float(current))
        result = math.tan(radian)
        statement = f"tan({current}) = {result}"
        update_calc_history(statement)
        
        num_entry.delete(0, tk.END)
        num_entry.insert(0, str(result))
        
    except ValueError as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
    except Exception as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
        
def button_cotangent():
    current = num_entry.get()
    if current == '':
        num_entry.insert(0, "Error: No input")
        return

    try:
        # Convert the input to a float and then to radians
        radian = math.radians(float(current))
        if math.tan(radian) == 0:
            raise ZeroDivisionError("Undefined")
        result = 1 / math.tan(radian)
        statement = f"cot({current}) = {result}"
        update_calc_history(statement)
        
        num_entry.delete(0, tk.END)
        num_entry.insert(0, str(result))
        
    except ValueError as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
    except Exception as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")

def button_secant():
    current = num_entry.get()
    if current == '':
        num_entry.insert(0, "Error: No input")
        return

    try:
        # Convert the input to a float and then to radians
        radian = math.radians(float(current))
        if math.cos(radian) == 0:
            raise ZeroDivisionError("Undefined")
        result = 1 / math.cos(radian)
        statement = f"sec({current}) = {result}"
        update_calc_history(statement)
        
        num_entry.delete(0, tk.END)
        num_entry.insert(0, str(result))
        
    except ValueError as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
    except Exception as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")

def button_cosecant():
    current = num_entry.get()
    if current == '':
        num_entry.insert(0, "Error: No input")
        return

    try:
        # Convert the input to a float and then to radians
        radian = math.radians(float(current))
        if math.sin(radian) == 0:
            raise ZeroDivisionError("Undefined")
        result = 1 / math.sin(radian)
        statement = f"csc({current}) = {result}"
        update_calc_history(statement)
        
        num_entry.delete(0, tk.END)
        num_entry.insert(0, str(result))
        
    except ValueError as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
    except Exception as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
def button_factorial():
    current = num_entry.get()
    try:
        # Check if the input is a valid number
        f_num = round(float(current))
        
        if f_num < 0:
            raise ValueError("Non-negative only")
        
        result = math.factorial(f_num)
        statement = f"{f_num}! = {result}"
        update_calc_history(statement)
        
        num_entry.delete(0, tk.END)
        num_entry.insert(0, str(result))
        
    except ValueError as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
    except Exception as e:
        num_entry.delete(0, tk.END)
        num_entry.insert(0, f"Error: {str(e)}")
# Function to update calculation history
def update_calc_history(statement):
    global calc_history, calc_history_top, calc_history_display
    
    calc_history_top += 1
    calc_history.append(statement)
    calc_history = calc_history[:calc_history_top + 1]

    if calc_history_display.get(1.0, tk.END).strip():  # Check if there's any text
        calc_history_display.delete(1.0, tk.END)
    calc_history_display.insert(tk.END, '\n'.join(calc_history))

def button_logarithmE():
    push_operator("ln")

def button_logarithm():
    push_operator("log")

def button_modulus():
    push_operator("%")

def button_clear():
    num_entry.delete(0, tk.END)
    stk.stack = []
    stk.top = -1
    display.delete(0, tk.END)

def button_equals():
    """
    Perform the calculation based on the operator and the numbers entered.

    If there is no operation to perform, an error message is displayed.
    If the number entered is invalid, an error message is displayed.
    The result of the calculation is displayed in the num_entry widget.
    The calculation history is updated with the statement of the calculation.
    """
    global f_num
    if stk.is_empty():
        num_entry.insert(0, "Error: No operation to perform")
        return

    current = num_entry.get()
    if not current:
        return  # Return if there's no number entered after the operator

    try:
        second_number = float(current)
    except ValueError:
        num_entry.insert(0, "Error: Invalid number")
        return

    operator = stk.pop()
    if operator == '+':
        result = f_num + second_number
    elif operator == '-':
        result = f_num - second_number
    elif operator == '*':
        result = f_num * second_number
    elif operator == '/':
        if second_number != 0:
            result = f_num / second_number
        else:
            num_entry.insert(0, "Error: Division by zero")
            return
    elif operator == '%':
        result = f_num % second_number
    elif operator == '^':
        result = f_num ** second_number
    elif operator == 'sin':
        result = math.sin(math.radians(second_number))
    elif operator == 'cos':
        result = math.cos(math.radians(second_number))
    elif operator == 'tan':
        result = math.tan(math.radians(second_number))
    elif operator == 'cot':
        result = 1 / math.tan(math.radians(second_number))
    elif operator == 'sec':
        result = 1 / math.cos(math.radians(second_number))
    elif operator == 'csc':
        result = 1 / math.sin(math.radians(second_number))
    elif operator == '!':
        result = math.factorial(second_number)
    elif operator == 'log':
        result = math.log10(second_number)
    elif operator == 'ln':
        result = math.log(second_number, math.e)
    else:
        num_entry.insert(0, "Error: Unknown operator")
        return

    statement = f"{f_num} {operator} {second_number} = {result}"
    update_calc_history(statement)
    
    num_entry.delete(0, tk.END)
    num_entry.insert(0, str(result))
    f_num = result

def button_absolute():
    current = num_entry.get()
    num_entry.delete(0, tk.END)
    num_entry.insert(0, float(str(current) + "||"))
    
def button_clearEverything():
    num_entry.delete(0, tk.END)

    # Clear the calculation history
    global calc_history
    calc_history = []

def button_decimal():
    current = num_entry.get()
    num_entry.delete(0, tk.END)
    num_entry.insert(0, float(str(current) + "."))

def PI_val():
    num_entry.delete(0, tk.END)
    num_entry.insert(0, math.pi)
    
def E_val():
    num_entry.delete(0, tk.END)
    num_entry.insert(0, math.e)
    
def push_operator(op):
    global f_num
    current = num_entry.get()
    if current:
        try:
            f_num = float(current)
        except ValueError:
            num_entry.delete(0, tk.END)
            num_entry.insert(0, "Error: Invalid number")
            return
        stk.push(op)
        num_entry.delete(0, tk.END)

# Define buttons
button_1 = tk.Button(root, text="1", padx=40.5, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40.5, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40.5, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40.5, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40.5, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40.5, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40.5, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40.5, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40.5, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40.5, pady=20, command=lambda: button_click(0))

button_addition = tk.Button(root, text="+", padx=39.5, pady=20, command=button_addition_click)
button_subtraction = tk.Button(root, text="-", padx=41.5, pady=20, command=button_subtraction)
button_multiplication = tk.Button(root, text="*", padx=40.5, pady=20, command=button_multiplication)
button_division = tk.Button(root, text="/", padx=41.5, pady=20, command=button_division)
button_clear = tk.Button(root, text="C", padx=41.5, pady=20, command=clear_button)
button_equals = tk.Button(root, text="=", padx=40.5, pady=20, command=button_equals)
button_sine = tk.Button(root, text="sin", padx=33, pady=20, command=button_sine)
button_cosine = tk.Button(root, text="cos", padx=32, pady=20, command=button_cosine)
button_tangent = tk.Button(root, text="tan", padx=32.5, pady=20, command=button_tangent)
button_cotangent = tk.Button(root, text="cot", padx=32.5, pady=20, command=button_cotangent)
button_secant = tk.Button(root, text="sec", padx=32, pady=20, command=button_secant)
button_cosecant = tk.Button(root, text="csc", padx=32, pady=20, command=button_cosecant)
button_logarithm = tk.Button(root, text="log", padx=33, pady=20, command=button_logarithm)
button_logarithmE = tk.Button(root, text="ln", padx=37, pady=20, command=button_logarithmE)
button_exponent = tk.Button(root, text="^", padx=44, pady=20, command=button_exponent)
button_absolute = tk.Button(root, text="|x|", padx=40, pady=20, command=button_absolute)
button_modulus = tk.Button(root, text="%", padx=40.5, pady=20, command=button_modulus)
button_factorial = tk.Button(root, text="n!", padx=41.5, pady=20, command=button_factorial)
button_clearEverything = tk.Button(root, text="CE", padx=37, pady=20, command=button_clearEverything)
button_decimal = tk.Button(root, text=".", padx=42.5, pady=20, command=button_decimal)
backspace_button = tk.Button(root, text="Backspace",padx=109.5,pady=20, command=backspace)
pi_button=tk.Button(root, text="π",padx=39.5,pady=20, command=PI_val)
e_button=tk.Button(root, text="ℯ",padx=40.5,pady=20, command=E_val)

# Add buttons to the GUI grid
calc_history_display = tk.Text(root, height=10, width=50, borderwidth=1)
calc_history_display.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
calc_history_display.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
scrollbar = tk.Scrollbar(root, command=calc_history_display.yview)
calc_history_display.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=1, column=5, sticky='nsew')

button_logarithm.grid(row=2, column=3)
button_tangent.grid(row=2, column=2)
button_cosine.grid(row=2, column=1)
button_sine.grid(row=2, column=0)
button_clear.grid(row=2, column=4)

button_logarithmE.grid(row=3, column=3)
button_cosecant.grid(row=3, column=2)
button_secant.grid(row=3, column=1)
button_cotangent.grid(row=3, column=0)
button_clearEverything.grid(row=3, column=4)

button_exponent.grid(row=4, column=4)
button_addition.grid(row=4, column=3)
button_9.grid(row=4, column=2)
button_8.grid(row=4, column=1)
button_7.grid(row=4, column=0)

button_factorial.grid(row=5, column=4)
button_subtraction.grid(row=5, column=3)
button_6.grid(row=5, column=2)
button_5.grid(row=5, column=1)
button_4.grid(row=5, column=0)

button_modulus.grid(row=6, column=4)
button_multiplication.grid(row=6, column=3)
button_3.grid(row=6, column=2)
button_2.grid(row=6, column=1)
button_1.grid(row=6, column=0)

button_absolute.grid(row=7, column=4)
button_division.grid(row=7, column=3)
button_equals.grid(row=7, column=2)
button_0.grid(row=7, column=1)
button_decimal.grid(row=7, column=0)

backspace_button.grid(row=8, column=2, columnspan=3)
e_button.grid(row=8, column=1)
pi_button.grid(row=8, column=0)

# Set the background color of the root window
root.configure(bg='black')

# Set the colors of the buttons
button_cosine.configure(bg='#A9AEED', font=('Helvetica', '12', 'bold'))
button_tangent.configure(bg='#A9AEED', font=('Helvetica', '12', 'bold'))
button_sine.configure(bg='#A9AEED', font=('Helvetica', '12', 'bold'))
button_cosecant.configure(bg='#A9AEED', font=('Helvetica', '12', 'bold'))
button_secant.configure(bg='#A9AEED', font=('Helvetica', '12', 'bold'))
button_cotangent.configure(bg='#A9AEED', font=('Helvetica', '12', 'bold'))

button_logarithm.configure(bg='#52ED92', font=('Helvetica', '12', 'bold'))
button_logarithmE.configure(bg='#52ED92', font=('Helvetica', '12', 'bold'))

button_exponent.configure(bg='#57D862', font=('Helvetica', '12', 'bold'))
button_absolute.configure(bg='#57D862', font=('Helvetica', '12', 'bold'))
button_modulus.configure(bg='#57D862', font=('Helvetica', '12', 'bold'))
button_factorial.configure(bg='#57D862', font=('Helvetica', '12', 'bold'))

e_button.configure(bg='#F0A0AB', font=('Helvetica', '12', 'bold'))
pi_button.configure(bg='#F0A0AB', font=('Helvetica', '12', 'bold'))

backspace_button.configure(bg='light grey', font=('Helvetica', '12', 'bold'))
button_equals.configure(bg='#E69081', font=('Helvetica', '12', 'bold'))
button_decimal.configure(bg="#D1A3B3", font=('Helvetica', '12', 'bold'))

button_clearEverything.configure(bg='#CAD621', font=('Helvetica', '12', 'bold'))
button_clear.configure(bg='#CAD621', font=('Helvetica', '12', 'bold'))

button_addition.configure(bg="#91D7F0", font=('Helvetica', '12', 'bold'))
button_subtraction.configure(bg="#91D7F0", font=('Helvetica', '12', 'bold'))
button_multiplication.configure(bg="#91D7F0", font=('Helvetica', '12', 'bold'))
button_division.configure(bg="#91D7F0", font=('Helvetica', '12', 'bold'))

button_0.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))
button_1.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))
button_2.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))
button_3.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))
button_4.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))
button_5.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))
button_6.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))
button_7.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))
button_8.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))
button_9.configure(bg="#EDA9ED", font=('Helvetica', '12', 'bold'))

# Set the colors of the text widget
calc_history_display.configure(bg='black', fg='white', border=10)
num_entry.configure(bg="black", fg="white", border=10)

# Set the colors of the scrollbar
scrollbar.configure(bg='black')

root.mainloop()