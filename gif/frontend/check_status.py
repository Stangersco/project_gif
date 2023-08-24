import requests

def check_server_status():
    try:
        response = requests.get('http://127.0.0.1:8000/status')
        if response.status_code == 200:
            return 'True', "Server is up and running"
        else:
            return 'False', f"Server returned status code: {response.status_code}"

    except:
        return 'False', "Could not connect to the server"


if __name__ == "__main__":
    print(check_server_status())