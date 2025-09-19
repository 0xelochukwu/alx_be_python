#match_case_calculator.py

#collecting numbers from user
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))


#asking for the type of operation
type_of_operation = input("Choose the operation (+, -, *, /): ")

#matching them
match type_of_operation:
    case "+" :
        result = first_number + second_number
        print("The result is " + str(result)+ ".")
    case "-":
        result = first_number - second_number
        print("The result is " + str(result)+ ".")
    case "*":
        result = first_number * second_number
        print("The result is " + str(result)+ ".")
    case "/":
        if second_number == 0:
            print("Error: Cannot divide by zero")
        else:
            result = first_number / second_number
            print("The result is " + str(result)+ ".")
    case _:
        print("Invalid Operation")
