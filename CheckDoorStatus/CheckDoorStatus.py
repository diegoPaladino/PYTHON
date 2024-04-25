class DoorStatusChecker:
    """
    A class to check if a door is closed based on user input.
    """

    def __init__(self):
        self.status = None

    def get_status_from_user(self):
        """
        Gets the door status from user input.
        """
        self.status = input("Is the door closed? (yes/no): ").strip().lower()
        self.validate_input()

    def validate_input(self):
        """
        Validates the user's input. If invalid, prompts again.
        """
        while self.status not in ['yes', 'no']:
            print("Invalid input. Please answer 'yes' or 'no'.")
            self.status = input("Is the door closed? (yes/no): ").strip().lower()

    def check_door_status(self):
        """
        Checks and displays the door status based on user input.
        """
        if self.status == 'yes':
            print("The door is closed.")
        elif self.status == 'no':
            print("The door is open.")

def main():
    checker = DoorStatusChecker()
    checker.get_status_from_user()
    checker.check_door_status()

if __name__ == "__main__":
    main()
