import os, inspect


class State:
    state = {
        'name': '',
        'projects_dir': ''
    }

    def __init__(self):
        generator_dir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
        self.state['projects_dir'] = os.path.dirname(generator_dir)
        print(self.state['projects_dir'])

    def get(self, getting_value=''):
        return self.state[getting_value]

    def update(self, values={}):
        self.state = {**self.state, **values}


g_state = State()
