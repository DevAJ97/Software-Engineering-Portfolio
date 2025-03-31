# TextBasedGame.py
# Author: [Aliyah Johnson]
# Preferred [Lee Johnson]

def show_instructions():
    """
    Display game instructions and valid commands.
    """
    print("Welcome to 'A Transman's Journey in a Cisman's World'!")
    print(
        "Your goal is to collect all the symbolic items of strength and identity while navigating through different environments.")
    print("Finally, confront societal barriers represented by the CEO and win the game.")
    print("\nMove commands: go North, go South, go East, go West")
    print("To collect an item: get 'item name'")
    print("Type quit to exit the game.\n")


def show_status(current_room, inventory, rooms):
    """
    Display the current status of the player.
    """
    print("\nYou are currently at:", current_room)
    print("Your Inventory:", inventory)
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']} here.")
    print("-------------------------------------")


def main():
    """
    Main function to control the gameplay
    """
    # Define the game layout
    rooms = {
        'Home': {'North': 'Workplace', 'East': 'Mall'},
        'Workplace': {'South': 'Home', 'East': 'Gym', 'item': 'Paycheck'},
        'Gym': {'West': 'Workplace', 'North': 'Boardroom', 'item': 'Workout Gear'},
        'Mall': {'West': 'Home', 'East': 'Pharmacy', 'item': 'Chest Binder'},
        'Pharmacy': {'West': 'Mall', 'North': 'Dr. Office', 'item': 'Testosterone medication'},
        'Dr. Office': {'South': 'Pharmacy', 'North': 'Girlfriends House', 'item': 'HRT Results'},
        'Girlfriends House': {'South': 'Dr. Office', 'item': 'Laptop'},
        'Boardroom': {'South': 'Gym', 'item': 'CEO'}  # Villain
    }

    # Start position and inventory
    current_room = 'Home'
    inventory = []
    total_items = 6  # Total items needed to win the game

    # Show game instructions
    show_instructions()

    while True:
        # Display player status
        show_status(current_room, inventory, rooms)

        # Get player input
        command = input("Enter your move: ").strip().lower()

        # Quit the game
        if command == "quit":
            print("\nThank you for playing. Goodbye!")
            break

        # Handle movement commands
        elif command.startswith('go '):
            direction = command.split(' ')[1].capitalize()
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way! Try a different direction.")

        # Handle item collection
        elif command.startswith('get '):
            item_name = command[4:]
            # Check if item is available in the current room
            if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == item_name.lower():
                inventory.append(item_name)
                print(f"{item_name} collected!")
                del rooms[current_room]['item']  # Remove the item from the room
            else:
                print("That item is not here.")

        # Invalid command
        else:
            print("Invalid command! Please try again.")

        # Check win/loss conditions
        if current_room == 'Boardroom' and 'CEO' in rooms[current_room]:
            if len(inventory) < total_items:
                print(
                    "\nThe CEO overwhelmed you! You must gather more strength and items to overcome societal barriers.")
                print("GAME OVER! Better luck next time.")
                break
            else:
                print("\nCongratulations, Keyshawn! You gathered all the symbolic items of strength and identity.")
                print("With your preparation and courage, you faced and overcame the societal barriers.")
                print("YOU WIN! Thank you for playing.")
                break


if __name__ == "__main__":
    main()