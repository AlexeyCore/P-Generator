import os


class State:
    state = {
        'name': '',
        'projects_dir': ''
    }

    def __init__(self):
        self.state['projects_dir'] = os.getcwd()

    def get(self, getting_value=''):
        return self.state[getting_value]

    def update(self, values={}):
        self.state = {**self.state, **values}


g_state = State()
