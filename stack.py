def greet(name, step=1):
    if step == 1:
        print("Hello " + name + "!")
        greet(name, step + 1)  # Recursive call to proceed to the next step
    elif step == 2:
        print("How are you " + name + "?")
        greet(name, step + 1)  # Recursive call to proceed to the next step
    elif step == 3:
        print("Bye!")  # Base case to end recursion

greet("Alice")