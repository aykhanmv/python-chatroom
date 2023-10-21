# Simple python-chatroom

This is simple e2e chatroom in python. Users can create multiple chatrooms to chat.

## Installation

```
git clone https://github.com/aykhanmv/python-chatroom/
cd python-chatroom
virtualenv .venv
source .venv/bin/activate
pip insall -r requirements.txt
```

## Usage

To enable server:
```
python server_inc.py
```

To enable client:
```
python client_inc.py
```

1. Enter you name
2. Chose 1 if you want to create a new room, 2 to join an existing room and enter the room name
3. Start chatting

## Info

The server_inc.py file generates public and private keys based RSA encryiption and sends publickey to the client user. The public key is then used to encrypt messages before sending by the clinet_inc.py. On the server side, private keys and room data are stored in server_db.py file. 
