import pathlib
import webbrowser

me = pathlib.Path(__file__)

webbrowser.open_new_tab(str(me.parent / 'web' / 'index.html'))
