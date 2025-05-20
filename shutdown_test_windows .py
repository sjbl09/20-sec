import os
import time

def safe_shutdown_test():
    print("This is a test shutdown script for Windows. It will initiate a shutdown in 20 seconds.")
    print("You can cancel it by running 'shutdown /a' in Command Prompt within 20 seconds.")
    print("For testing purposes only. Ensure you are in a safe, controlled environment (e.g., VM).")
    
    try:
        # Initiate shutdown with 20-second delay (Windows)
        os.system("shutdown /s /t 20")
        print("Shutdown initiated. To cancel, run 'shutdown /a' in Command Prompt within 20 seconds.")
        
        # Simulate a testing process (e.g., waiting for user to observe)
        time.sleep(5)
        print("Reminder: You have 15 seconds left to cancel the shutdown with 'shutdown /a'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Shutdown not initiated. Please check permissions (run as administrator if needed).")

if __name__ == "__main__":
    # Prompt user to confirm they are in a test environment
    confirmation = input("Are you running this in a controlled test environment (e.g., VM)? (yes/no): ").strip().lower()
    if confirmation == "yes":
        safe_shutdown_test()
    else:
        print("Aborted. Please run this script only in a controlled test environment.")
