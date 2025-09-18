# Import the requests library to send HTTP requests
import requests

# Import datetime to add timestamps to logs
from datetime import datetime

# Function to perform brute-force directory scanning
def brute_force_directories(base_url, wordlist):
    # Print the start message with the target URL
    print(f"[*] Starting scan on {base_url}")

    # Loop through each word in the wordlist
    for word in wordlist:
        # Construct the full URL by appending the word to the base URL
        url = f"{base_url}/{word.strip()}"

        try:
            # Send a GET request to the constructed URL
            response = requests.get(url)

            # If the response status code is 200 (OK), the directory exists
            if response.status_code == 200:
                print(f"[+] Found: {url}")

        # Handle any request errors (e.g., connection issues, timeouts)
        except requests.exceptions.RequestException:
            pass  # Ignore errors and continue scanning

# Function to load the wordlist from a file
def load_wordlist(filepath):
    # Open the file and read all lines into a list
    with open(filepath, 'r') as file:
        return file.readlines()

# Main execution block
if __name__ == "__main__":   
# This ensures the code below only runs when the script is executed directly.

    # Prompt the user to enter the target URL
    target = input("Enter target URL (e.g., http://example.com): ")

    # Prompt the user to enter the path to the wordlist file
    wordlist_path = input("Enter path to wordlist file: ")

    # Load the wordlist from the specified file
    words = load_wordlist(wordlist_path)

    # Start the brute-force scan using the target and wordlist
    brute_force_directories(target, words)