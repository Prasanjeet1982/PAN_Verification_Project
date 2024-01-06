# user_input.py

def get_user_input():
    pan_number = input("Enter PAN number: ").strip().upper()  # Get PAN number from the user and format it
    name = input("Enter name: ").strip().title()  # Get name and capitalize first letters
    dob = input("Enter date of birth (YYYY-MM-DD): ").strip()  # Get date of birth

    # You might add additional validation or formatting for the date of birth

    # Create a dictionary with user input
    pan_details = {
        "pan_number": pan_number,
        "name": name,
        "dob": dob
    }

    return pan_details
