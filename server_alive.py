import requests

def fetch_response():
    try:
        url = "https://roadmapper-backend-1.onrender.com/"
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Response from server:")
            print(response.text)
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
            print("Response details:", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:")
        print(e)

# Example usage
if __name__ == "__main__":   
    fetch_response()
    