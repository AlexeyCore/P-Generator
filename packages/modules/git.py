from packages.modules import helpers


def clone(repo_url='', folder_path=''):
    return helpers.run_command(['git clone %s %s' % (repo_url, folder_path)])
