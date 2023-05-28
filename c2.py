import requests
import json

def get_command(command):
    """Gets the command from the client."""
    command = requests.get("http://localhost:8080/command").content.decode("utf-8")
    return command

def send_command(command):
    """Sends the command to the client."""
    url = "http://localhost:8080/command"
    data = {"command": command}
    requests.post(url, data=data)

def get_results(command):
    """Gets the results of the command from the client."""
    url = "http://localhost:8080/results"
    data = {"command": command}
    response = requests.post(url, data=data)
    return json.loads(response.content)

while True:
    command = get_command()
    send_command(command)
    results = get_results(command)
    print(results)
