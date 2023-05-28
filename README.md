# lightweight-c2
Light weight C2

This project is a light weight C2 that can be used to control infected machines. It has both Linux and Windows clients.
Getting Started

To get started, you will need to install Python and the requests module.
### Linux

sudo apt-get install python3-pip
pip3 install requests

### Windows

pip install requests

Once you have installed the required dependencies, you can start the C2 server by running the following command:

python main.py

The C2 server will listen on port 8080 you can edit port in code.

To create a client, run the following command:

python c2.py

The client will connect to the C2 server and wait for commands.

To send a command, type the command in the terminal and press Enter. The command will be sent to the C2 server and the results will be displayed in the terminal.

Features
    Light weight
    Supports Linux and Windows clients
    Easy to use

Limitations

    The C2 server is not secure. It is not meant to be used in production.

Future Work

    Add security features
    Add support for other platforms
    Add more commands
