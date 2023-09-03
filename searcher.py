import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
from urllib.parse import urlparse, urljoin
import threading

# Initialize colorama for colored text
init(autoreset=True)

# Set of visited URLs to avoid duplicates
visited_urls = set()

# Function to crawl the website, search for specific words, and follow links within the domain
def crawl_and_search(url, search_words, domain):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all text on the page
            page_text = soup.get_text()

            # Check if any of the search words exist in the page text
            for search_word in search_words:
                if search_word.lower() in page_text.lower():
                    print(Fore.GREEN + f"Found '{search_word}' on {url}" + Fore.RESET)

            # Add the URL to the set of visited URLs
            visited_urls.add(url)

            # Find all links on the page
            links = soup.find_all('a', href=True)

            for link in links:
                href = link['href']

                # Make sure the link is within the same domain
                if domain in href:
                    # Create an absolute URL by joining with the base URL
                    absolute_url = urljoin(url, href)

                    # Ensure the URL is not visited to avoid infinite loops
                    if absolute_url not in visited_urls:
                        # Recursively crawl the linked page
                        crawl_and_search(absolute_url, search_words, domain)

        else:
            print(f"Failed to retrieve {url}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Accept user input for the website URL and the words to search for (comma-separated)
website_url = input("Enter the website URL: ")
search_words = input("Enter the words to search for (comma-separated): ").split(',')

# Parse the domain from the website URL
parsed_url = urlparse(website_url)
domain = parsed_url.netloc

# Create a thread for crawling and searching
thread = threading.Thread(target=crawl_and_search, args=(website_url, search_words, domain))

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()
