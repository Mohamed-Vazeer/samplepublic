import requests
from bs4 import BeautifulSoup

# Replace these with the actual login URL, login form action URL (if different), and desired page to scrape
LOGIN_URL = 'https://example.com/login'
LOGIN_ACTION_URL = 'https://example.com/login'  # This can be different from LOGIN_URL
TARGET_URL = 'https://example.com/secret-page'

# Login credentials
payload = {
    'username': 'your_username',
    'password': 'your_password'
}

with requests.Session() as session:
    # If the website uses CSRF tokens, you need to fetch the login page first and parse out the token
    # response = session.get(LOGIN_URL)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # token = soup.find('input', {'name': 'csrf_token_name'})['value']
    # payload['csrf_token_name'] = token  # Assuming the form requires a CSRF token

    # Perform login
    post = session.post(LOGIN_ACTION_URL, data=payload)
    if post.ok:
        # After login, scrape the TARGET_URL
        response = session.get(TARGET_URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Scrape content of a specific element
        # Update this selector to match the content you want to scrape
        content = soup.find('div', {'id': 'content'})
        print(content.text)
    else:
        print("Login failed")

