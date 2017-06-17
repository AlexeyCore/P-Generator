from modules import rn


def clone_template(answers={}):
    tm = answers['template']
    if tm == 'rn':
        rn.init(answers['name'])
    elif tm == 'node':
        pass

    # if answers[]
    # repository_url = constants.templates[answers['template']]
    # cloned_repo = Repo.clone_from(repository_url, '%s/%s' % (os.getcwd(), answers['name']))
    # print (cloned_repo)