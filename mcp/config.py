import json
from collections import namedtuple
from subprocess import Popen

from mcp.game import Game

Config = namedtuple('Config', 'games gui')


def _load_config(filename='config.json'):
	with open(filename, 'r') as json_file:
		raw_config = json.load(json_file)

	config = Config(raw_config['games'], raw_config['gui'])
	return config


def load_games(filename='config.json'):
	config = _load_config(filename)
	games = [Game(i['name'], i['command'], i['image']) for i in config.games]

	return games


def start_gui():
	config = _load_config()
	gui_jar = config.gui

	Popen(['java', '-jar', gui_jar])
