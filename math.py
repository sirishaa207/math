try;
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition:{a + b}")
    print(f"Subtraction:{a - b}")
except ValueError:
  print("please enter valid number.")
