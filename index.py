import os
import sys

from packages.modules import helpers
from packages.modules.state import g_state

from packages.modules import templates

# Check current directory
project_dir = g_state.get('projects_path')
current_dir = os.getcwd()
if current_dir != project_dir:
    print('\033[91mPlease, run generator from your project directory.')
    print('    For example:\033[0m \033[92mpython3 P-Generator/index.py\033[0m')
    sys.exit()

# Getting main data
answers = {
    'template': helpers.ask_question('Select generator template', ['rn', 'node'])
}

# Check template
if answers['template'] == 'node':
    print('Coming soon')
    sys.exit()

# Set state
answers['name'] = helpers.ask_question('Enter your project name')
g_state.update(answers)

# Output info
print('\033[92m-------------------------------------------')
print('%s template\033[0m\n' % answers['template'])

# Init templates functions
templates.clone_template()
