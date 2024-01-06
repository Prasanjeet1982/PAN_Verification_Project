from user_input import get_user_input
from verification_logic import verify_pan_details

def main():
    print("Welcome to PAN Card Verification System")
    print("Please enter your PAN card details:")

    # Get PAN card details from the user
    pan_details = get_user_input()

    # Verify PAN card details
    verification_result = verify_pan_details(pan_details)

    # Display verification result
    if verification_result:
        print("PAN card details are valid and verified.")
    else:
        print("Invalid PAN card details. Please check and try again.")

if __name__ == "__main__":
    main()
