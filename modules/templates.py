import os
from git import Repo
from modules import helpers
from modules import constants


def init_rn(name=''):
    helpers.run_command(['react-native init %s' % name])
    return



def clone_template(answers={}):
    tm = answers['template']
    if tm == 'rn':
        init_rn(answers['name'])
    elif tm == 'node':
        print('Coming soon')

    # if answers[]
    # repository_url = constants.templates[answers['template']]
    # cloned_repo = Repo.clone_from(repository_url, '%s/%s' % (os.getcwd(), answers['name']))
    # print (cloned_repo)