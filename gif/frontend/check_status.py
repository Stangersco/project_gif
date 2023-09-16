import requests

def check_server_status():
    try:
        response = requests.get('http://127.0.0.1:8000/status')
        if response.status_code == 200:
            return 'online', "Server is up and running"
        else:
            return 'offline', f"Server returned status code: {response.status_code}"

    except:
        return 'offline', "Could not connect to the server"


if __name__ == "__main__":
    print(check_server_status())