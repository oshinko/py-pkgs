import pathlib

print('imported', __file__)

greet_file = pathlib.Path(__file__).parent / 'data/greet.txt'

print(greet_file.read_text(encoding='utf8').strip())
