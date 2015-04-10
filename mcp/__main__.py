import os

from mcp import main, DEFAULT_SOCKET

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		os.unlink(DEFAULT_SOCKET)
