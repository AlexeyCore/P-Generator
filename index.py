import sys
from modules import helpers, templates


# Getting main data
answers = {
    'template': helpers.ask_question('Select generator template', ['rn', 'node'])
}

# Check template
if answers['template'] == 'node':
    print('Coming soon')
    sys.exit()

answers['name'] = helpers.ask_question('Enter your project name')
print('\033[92m-------------------------------------------')
print('%s template\033[0m\n' % answers['template'])


templates.clone_template(answers)
