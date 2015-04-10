import socket
import os

from mcp import api

DEFAULT_SOCKET = '/tmp/mcp'
BUF_SIZE = 255


def main():
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.bind(DEFAULT_SOCKET)
	sock.listen(0)

	while True:
		client, addr = sock.accept()

		line = b'MESSAGE'
		while line != b'':
			line = client.recv(BUF_SIZE).strip()

			if line == api.GET_GAMES:
				client.send(b"'Space Invaders' 'spc.pde' '/home/nate/git/arcade-machine-mcp-gui/src/main/java/data/space_invaders.png'\n")
				print('sent games')
			elif line == api.NUM_GAMES:
				client.send(b'1\n')
				print('sent num games')
			else:
				print(line)
