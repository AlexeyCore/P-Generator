import sys
from modules import helpers, structure


def questions():
    return {
        'navigator': helpers.ask_question(
            'Select react native navigator',
            ['react-navigation', 'react-native-navigation']
        ),
        'reduxsauce': helpers.ask_question(
            'Add reduxsauce',
            ['Y', 'N']
        )
    }


def complete(name=''):
    print('Complete')


def format_template(answers={}):
    print('Project restructuring...')
    structure.format(rn_structure)


def init(name=''):
    answers = questions()
    print('Initializing "%s" project...' % name)
    result = helpers.run_command(['react-native init %s' % name])
    if not result:
        print('Error initializing react-native project :(')
        sys.exit()
    format_template(answers, name)
