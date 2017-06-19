import os, inspect


class State:
    state = {
        'name': '',
        'template': '',
        'generator_dir': 'P-Generator',
        'packages_dir': 'packages',
        'templates_dir': 'templates',
        'template_tree_dir': 'g_tree',
        'projects_path': ''
    }

    def __init__(self):
        generator_dir = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(inspect.getfile(inspect.currentframe()))
                )
            )
        )
        self.state['projects_path'] = os.path.dirname(generator_dir)

    def get_state(self):
        return self.state

    def get(self, getting_value):
        if type(getting_value) is str:
            return self.state[getting_value]
        elif type(getting_value) is list:
            values = {}
            for value in getting_value:
                values[value] = self.state[value]
            return values

    def update(self, values={}):
        self.state = {**self.state, **values}


g_state = State()
