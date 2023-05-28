import requests
import json



def get_command(command):
    """Gets the command from the user."""
    command = input("Enter command: ")
    return command

def send_command(command):
    """Sends the command to the C2 server."""
    url = "https://localhost/command"
    data = {"command": command}
    response = requests.post(url, data=data)
    return response

def get_results(response):
    """Gets the results of the command from the C2 server."""
    if response.status_code == 200:
        results = json.loads(response.content)
        return results
    else:
        raise Exception("Error getting results: {}".format(response.status_code))


while True:
    command = get_command()
    response = send_command(command)
    results = get_results(response)
    print(results)
