import requests

def fetch_data():
    response = requests.get("https://google.com")
    print(response.status_code)

if __name__ == "__main__":
    fetch_data()