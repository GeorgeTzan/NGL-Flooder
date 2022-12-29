import requests
import threading
import time
import logging

logging.basicConfig(level=logging.ERROR)

def send_request(session, text):
    """Sends a POST request with the given text as the question parameter."""
    url = "https://ngl.link/[PUT USERNAME]"
    params = {'question': text}
    try:
        session.post(url, data=params)
    except Exception as e:
        logging.error(e)

def main():
    # Create a session object to be used for all requests
    session = requests.Session()

    text = input("give text: ")
    while text:
        # Send the request in a new thread
        thread = threading.Thread(target=send_request, args=(session, text))
        thread.start()

        # Get the next input from the user
        text = input("give text: ")

        # Add a delay between requests to avoid overloading the server
        time.sleep(0.6)

if __name__ == "__main__":
    main()
