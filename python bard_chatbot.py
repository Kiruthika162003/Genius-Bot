import requests
import json

def get_bard_response(prompt):
    """Gets a response from Bard."""
    url = "https://bard.googleapis.com/v1/generate"
    payload = {"prompt": prompt}
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content.decode())
        return data["text"]
    else:
        raise Exception("Error getting response from Bard: {}".format(response.status_code))

def main():
    """Main function."""
    prompt = input("What do you want to ask Bard? ")
    response = get_bard_response(prompt)
    print(response)

if __name__ == "__main__":
    main()
