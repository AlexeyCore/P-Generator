import os, sys
from modules import helpers, templates
from modules.state import g_state


# Check current directory
current_path = g_state.get('projects_dir')
current_dir = os.path.basename(current_path)
if current_dir != 'P-Generator':
    print('\033[91mPlease, run generator from "P-Generator" directory\033[0m')
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
