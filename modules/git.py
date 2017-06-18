from modules import helpers


def clone(repo_url='', folder_name=''):
    return helpers.run_command(['git clone %s %s' % (repo_url, folder_name)])
