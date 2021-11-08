import pathlib

me = pathlib.Path(__file__)

print(me, 'Hello!')

greet_file = me.parent / 'data/greet.txt'

print(me, 'greet', greet_file.read_text(encoding='utf8').strip())
