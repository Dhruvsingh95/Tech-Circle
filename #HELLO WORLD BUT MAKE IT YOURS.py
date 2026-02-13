#HELLO WORLD BUT MAKE IT YOURS 

name = input("Name: ").strip()

if not name:
    print("No name entered. Using default name 'Friend'.")
    name = "Friend"


while True:
    age_input = input("Age: ").strip()

    try:
        age = int(age_input)  
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            continue
        break  
    except ValueError:
        print("Invalid input. Please enter a numeric age.")


favorite_color = input("Favorite color: ").strip()

if not favorite_color:
    favorite_color = "unknown"
    print("No favorite color entered. We'll go with 'unknown'.")


print("\n--- Personalized Greeting ---")
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your favorite color is {favorite_color} - great choice!")
print("Welcome to your programming journey!")

