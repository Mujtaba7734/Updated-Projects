import tkinter as tk
Array_Equation, operation = [], []
Bracket_Open, Bracket_Close = [], []

def check_e(equation):
    x = 0
    while x < len(operation):
        if operation[x] == "e":
            if equation[0] == "-":
                x -= 1
            Array_Equation[x] = Array_Equation[x] + operation[x] + operation[x + 1] + Array_Equation[x + 1]
            operation.pop(x), Array_Equation.pop(x + 1), operation.pop(x) 
            x -= 1
        x +=1
def Array(equation):
    global Array_Equation, operation, Brackets
    Array_Equation.clear(), operation.clear()
    number = ""
    new_equation = ""
    for x in range(len(equation)):
        if equation[x] != "(" and equation[x] != ")":
            new_equation = new_equation + equation[x] 
    x =0 
    while x < len(new_equation):
        while (new_equation[x] >= "0" and new_equation[x] <= "9") or new_equation[x] == ".":
            number = number + new_equation[x]
            x +=1
            if x >= (len(new_equation)):
                Array_Equation.append(number)
                check_e(new_equation)
                return 1
        operation.append(new_equation[x])
        if number != "":
            Array_Equation.append(number)
        x +=1
        number = ""
    check_e(new_equation)
    return 1

def Bracket_array(equation_1):
    global Bracket_Open, Bracket_Close
    for x in range(len(equation_1)):
        if equation_1[x] == "(":
            Bracket_Open.append(x)
        elif equation_1[x] == ")":
            Bracket_Close.append(x)          

def equation_sort(x, ans, checkneg, equation):
    new_equation = ""
    z = 0
    while z < len(operation):
        if z == x:
                new_equation = new_equation + str(ans)
        elif z > x:
            new_equation = new_equation + operation[z] + Array_Equation[z + 1]
        elif equation[0] == "-":
                if operation[z + 1] == "-":
                    new_equation = new_equation + "-" + Array_Equation[z]   
                    if ans < 0:
                        new_equation = new_equation + "-"
                    else:
                        new_equation = new_equation + "+"
                else:
                    new_equation = new_equation + "-" + Array_Equation[z]
                    if ans > 0:
                        new_equation = new_equation + "+"
        elif z == x -1 and checkneg == "-":
                if ans < 0:
                    new_equation = new_equation + Array_Equation[z]
                else:
                    new_equation = new_equation + Array_Equation[z] + "+"
        else:
                new_equation = new_equation + Array_Equation[z] + operation [z]
        z +=1
    return new_equation

def remove_bracket(index, equation_bracket, equation_unmodified):
    global Bracket_Open, Bracket_Close
    if Bracket_Close[0] != len(equation_unmodified) -1 and equation_bracket[0] == "-" and equation_unmodified[Bracket_Close[0] +1] == "^":
            if Bracket_Open[index] != 0:
                equation_unmodified = equation_unmodified[:Bracket_Open[index] +1] + equation_bracket + equation_unmodified[Bracket_Close[0]:]
            else:
                equation_unmodified = "(" + equation_bracket + equation_unmodified[Bracket_Close[0]:] 
    elif equation_bracket[0] == "-" and Bracket_Open[index] != 0:
            equation_bracket = equation_bracket[1:]
            if equation_unmodified[Bracket_Open[index] - 1] == "-":
                equation_unmodified = equation_unmodified[:Bracket_Open[index] - 1] + "+" + equation_bracket + equation_unmodified[Bracket_Close[0] + 1:]
            else:
                equation_unmodified = equation_unmodified[:Bracket_Open[index] - 1] + "-" + equation_bracket + equation_unmodified[Bracket_Close[0] + 1:]
    else:
            equation_unmodified = equation_unmodified[:Bracket_Open[index]] + equation_bracket + equation_unmodified[Bracket_Close[0] + 1:]    
    Bracket_Open.clear(), Bracket_Close.clear()
    Bracket_array(equation_unmodified)
    return equation_unmodified

def negative_number_solve(x):
    global operation, Array_Equation
    if x != 0:
        if operation[x -1] == "-":
            return "-"
    return "+"

def solve(x, opp, equation):
    global Array_Equation, operation
    ans = 0
    checkneg = negative_number_solve(x)
    if equation[0] == "-" and opp != "-":
        x -=1
    if checkneg == "-":
        Array_Equation[x] = str(-1 * float(Array_Equation[x]))
    match opp:
        case "^": 
            ans = float(Array_Equation[x]) ** float(Array_Equation[x + 1])
            if float(Array_Equation[x]) < 0 and ans > 0:
                ans = -1 * ans
        case "/": 
            ans = float(Array_Equation[x]) / float(Array_Equation[x + 1]) 
        case "*": 
            ans = float(Array_Equation[x]) * float(Array_Equation[x + 1]) 
        case "+": 
            ans = float(Array_Equation[x]) + float(Array_Equation[x + 1]) 
        case "-": 
            if x == 0 and len(operation) != 1:
                if equation[0] == "-":
                    ans = (-1 *float(Array_Equation[x])) - float(Array_Equation[x + 1])
                    operation.pop(x)
                    return x, ans, "-"
                else:
                    ans = float(Array_Equation[x]) - float(Array_Equation[x + 1])
            else:
                ans = float(Array_Equation[x]) - float(Array_Equation[x + 1])
    if equation[0] == "-":
        operation.pop(0)
    return x, ans, checkneg
    
def choose_operation(equation):
    global operation
    for x in range(len(operation)):
        if operation[x] == "^":
            return solve(x, "^", equation)
    for x in range(len(operation)):
        if operation[x] == "/":
            return solve(x, "/", equation)
    for x in range(len(operation)):
        if operation[x] == "*":
            return solve(x , "*", equation)
    for x in range(len(operation)):
        if operation[x] == "+":    
            return solve(x , "+", equation)
    for x in range(len(operation)):
        if operation[x] == "-":
            return solve(x, "-", equation)

def bracket_solve(index, equation):
    global Bracket_Open, Bracket_Close
    equation_bracket = equation[Bracket_Open[index]+ 1:Bracket_Close[0]]
    bracket_check = Array(equation_bracket)
    if Bracket_Close[0] != len(equation) -1 and len(operation) == 1:
        if equation[Bracket_Open[index] + 1] == "-" and equation[Bracket_Close[0] +1] == "^":
            bracket_check = Array(equation)
            for x in range(len(operation)):
                if operation[x] == "^":
                    if equation[0] == "-":
                        x = x - 1
                    if Array_Equation[x -1] == equation_bracket[1:]:
                        ans = float(equation_bracket) **  float(Array_Equation[x])
                        if Bracket_Open[index] != 0:
                                equation = equation[:Bracket_Open[index]] + str(ans) + equation[Bracket_Close[0] + 3:]
                        else:
                            equation = str(ans) + equation[Bracket_Close[0] + 3:]
                        break
            Bracket_Open.clear(), Bracket_Close.clear()
            bracket_check = Array(equation)
            Bracket_array(equation)
            return equation
    else:
        equation_bracket = equation[Bracket_Open[index]+ 1:Bracket_Close[0]]              
    bracket_check = Array(equation_bracket)
    while bracket_check == 1 and len(operation) != 0:
        x, ans, checkneg = choose_operation(equation_bracket)
        equation_bracket = equation_sort(x, ans, checkneg, equation_bracket)
        bracket_check = Array(equation_bracket)
        if len(operation) == 0:
            break
        elif equation_bracket[0] == "-" and len(operation) == 1:
            break
    equation = remove_bracket(index, equation_bracket, equation)
    return equation
def evaluated_answer(equation):
    check = Array(equation)
    Bracket_array(equation)
    index = 0
    while check == 1:
        while len(Bracket_Open) != 0:
            if len(Bracket_Open) == 1:
                equation = bracket_solve(index, equation)
            else:
                x = 0
                while x < len(Bracket_Open) and Bracket_Open[x] < Bracket_Close[0]:
                    x += 1
                if x == 0:
                    equation = bracket_solve(0, equation)
                else: 
                    equation = bracket_solve(x -1 , equation)
        check = Array(equation)
        if len(operation) == 0:
            return equation 
            break  
        elif equation[0] == "-" and len(operation) == 1:
            return equation 
            break
        x, ans, checkneg =  choose_operation(equation)
        equation = equation_sort(x, ans, checkneg, equation) 
        check = Array(equation)
        if len(operation) == 0:
            return equation 
            break  
        elif equation[0] == "-" and len(operation) == 1:
            return equation 
            break 
calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.set(calculation)
    
def evaluate_calculation():
    global calculation
    try:
        calculation = evaluated_answer(calculation)
        text_result.set(calculation)
    except:
        clearfield()
        text_result.set("Error")
    
def clearfield():
    global calculation
    calculation = ""
    text_result.set(calculation)

root = tk.Tk()
root.geometry("420x400")
root.title("Calculator GUI")
root.config(bg="gray")
root.resizable(False, False)

text_result = tk.StringVar()
entry = tk.Entry(root, width=28, bg="#ccddff", font=("Times New Roman", 24), textvariable=text_result)
entry.place(x=0, y=0)

btnopen = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=11, height=3, relief="flat", bg="#FF8488", font=("Times New Roman", 12))
btnopen.place(x=0, y=41)
btnclose = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=11, height=3, relief="flat", bg="#FF8488", font=("Times New Roman", 12))
btnclose.place(x=110, y=41)
btnexp = tk.Button(root, text="^", command=lambda: add_to_calculation("^"), width=11, height=3, relief="flat", bg="#FF8488", font=("Times New Roman", 12))
btnexp.place(x=220, y=41)

btn1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn1.place(x=0, y=113)
btn2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn2.place(x=110, y=113)
btn3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn3.place(x=220, y=113)

btn4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn4.place(x=0, y=185)
btn5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn5.place(x=110, y=185)
btn6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn6.place(x=220, y=185)

btn7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn7.place(x=0, y=257)
btn8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn8.place(x=110, y=257)
btn9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn9.place(x=220, y=257)

btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btn0.place(x=110, y=329)
btndot = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=11, height=3, relief="flat", bg="#FFE5B4", font=("Times New Roman", 12))
btndot.place(x=220, y=329)
btnplus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=11, height=3, relief="flat", bg="#FF8488", font=("Times New Roman", 12))
btnplus.place(x=330, y=257)

btnmin = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=11, height=3, relief="flat", bg="#FF8488", font=("Times New Roman", 12))
btnmin.place(x=330, y=185)
btnmul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=11, height=3, relief="flat", bg="#FF8488", font=("Times New Roman", 12))
btnmul.place(x=330, y= 41)
btndiv = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=11, height=3, relief="flat", bg="#FF8488", font=("Times New Roman", 12))
btndiv.place(x=330, y=113)
btnclear = tk.Button(root, text="C", command=clearfield, width=11, height=3, relief="flat", bg="#FFFF6E", font=("Times New Roman", 12))
btnclear.place(x=0, y=329)
btnequal = tk.Button(root, text="=", command=evaluate_calculation, width=11, height=3, relief="flat", bg="#ccddff", font=("Times New Roman", 12))
btnequal.place(x=330, y=329)

root.mainloop()