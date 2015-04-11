import socket

from mcp import api
from mcp.config import load_games, start_gui

DEFAULT_SOCKET = '/tmp/mcp'
BUF_SIZE = 255


def main():
	start_gui()
	games = load_games()

	print(games)
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.bind(DEFAULT_SOCKET)
	sock.listen(0)

	while True:
		client, addr = sock.accept()

		line = b'MESSAGE'
		while line != b'':
			if line == api.GET_GAMES:
				for game in games:
					client.send('{}\n'.format(str(game)).encode('ascii'))
			elif line == api.NUM_GAMES:
				client.send('{}\n'.format(len(games)).encode('ascii'))

			line = client.recv(BUF_SIZE).strip()
