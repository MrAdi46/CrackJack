# CrackJack

CrackJack is a Python tool designed to perform brute-force attacks on web application login pages. It iterates through a list of usernames and passwords, attempting to find valid credentials. The tool includes rate-limiting to prevent overwhelming the server with requests.

## Features

- **Brute-Force Attack**: Tests multiple username and password combinations to find valid credentials.
- **Rate Limiting**: Limits the number of requests sent per second to avoid detection and server overload.
- **Exception Handling**: Handles common errors gracefully, including network issues and invalid responses.
- **Input Validation**: Ensures that provided inputs, such as URL and credential lists, are valid.
- **URL Validation**: Checks if the provided URL is in a valid format before attempting login.

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/MrAdi46/CrackJack.git
```

2. Navigate to the directory
```bash
   cd CrackJack
```
## Usage
### To run CrackJack, use the following command:
```bash 
   python crackjack.py -u <url> -u_file <usernames_file> -p_file <passwords_file> -r <requests_per_second>
```
### Parameters

- `-u <url>`: The URL of the login page to attack.
- `-u_file <usernames_file>`: File containing a list of usernames (one per line).
- `-p_file <passwords_file>`: File containing a list of passwords (one per line).
- `-r <requests_per_second>`: Number of requests to send per second (rate limit).

## Example
### This will attempt to brute-force the login page at `https://example.com/login` using usernames 
```bash
   python crackjack.py -u https://example.com/login -u_file users.txt -p_file pass.txt -r 5
```
## Contributing
 
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.