import re

GET_GAMES = 'GET GAMES'
NUM_GAMES = 'NUM GAMES'
DONE_GAMES = 'DONE GAMES'
RUN_GAME = re.compile(r'RUN GAME (?P<id>[0-9]+)')
