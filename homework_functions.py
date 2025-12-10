# -----------------------------
# Part 1 — Basic Function Arguments
# -----------------------------

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} and its name is {pet_name}.")

# Calling function three times
describe_pet("dog", "Buddy")
describe_pet("cat", "Milo")
describe_pet("hamster", "Nugget")

print("\n--- Part 2 ---\n")

# -----------------------------
# Part 2 — Positional vs Keyword Arguments
# -----------------------------

# Positional call
describe_pet("dog", "Buddy")

# Keyword call (reversed)
describe_pet(pet_name="Milo", animal_type="cat")

print("\n--- Part 3 ---\n")

# -----------------------------
# Part 3 — Default Arguments
# -----------------------------

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} and its name is {pet_name}.")

# Using default animal
describe_pet("Brownie")

# Overriding default
describe_pet("Nugget", "chicken")

print("\n--- Part 4 ---\n")

# -----------------------------
# Part 4 — Create Your Own Function
# -----------------------------

def order_drink(drink, size="medium", iced=False):
    iced_text = "iced" if iced else "hot"
    return f"Your order: {size} {iced_text} {drink}"

# Tasks
print(order_drink("coffee"))
print(order_drink("hot chocolate", size="large", iced=False))
print(order_drink("milk tea", size="small", iced=True))

print("\n--- Part 5 ---\n")

# -----------------------------
# Part 5 — Mini Challenge (Calculator)
# -----------------------------

def compute(operation, num1, num2=1):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"

# Tasks
print(compute("add", 5, 10))
print(compute("multiply", num1=3, num2=4))
print(compute("subtract", 20))
print(compute("divide", 10, 2))
