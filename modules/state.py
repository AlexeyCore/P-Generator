import os, inspect
from modules import helpers


class State:
    state = {
        'name': '',
        'generator_dir': 'P-Generator',
        'templates_dir': 'templates',
        'projects_path': ''
    }

    def __init__(self):
        generator_dir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
        self.state['projects_path'] = os.path.dirname(generator_dir)

    def get(self, getting_value=''):
        return self.state[getting_value]

    def update(self, values={}):
        self.state = {**self.state, **values}


g_state = State()
