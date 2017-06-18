import os, inspect


class State:
    state = {
        'name': '',
        'projects_dir': ''
    }

    def __init__(self):
        modules_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.state['projects_dir'] = os.path.abspath(os.path.join(modules_dir, os.pardir))

    def get(self, getting_value=''):
        return self.state[getting_value]

    def update(self, values={}):
        self.state = {**self.state, **values}


g_state = State()
