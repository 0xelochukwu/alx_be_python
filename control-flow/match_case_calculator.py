#match_case_calculator.py

#collecting numbers from user
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))


#asking for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

#matching them
match operation:
    case "+" :
        result = first_number + second_number
        print(f"The result is {result}.")
    case "-":
        result = first_number - second_number
        print(f"The result is {result}.")
    case "*":
        result = first_number * second_number
        print(f"The result is {result}.")
    case "/":
        if second_number == 0:
            print("Error: Cannot divide by zero")
        else:
            result = first_number / second_number
            print(f"The result is {result}.")
    case _:
        print("Invalid Operation")
