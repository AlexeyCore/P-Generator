import os

from packages.modules import constants, git, helpers

from packages.modules.state import g_state


def clone_template():
    projects_path = g_state.get('projects_path')
    packages_dir = g_state.get('packages_dir')
    generator_dir = g_state.get('generator_dir')
    templates_dir = g_state.get('templates_dir')
    selected_tm = g_state.get('template')
    template_path = '%s/%s/%s/%s/%s/index.py' % (projects_path, generator_dir, packages_dir, templates_dir, selected_tm)
    tm = constants.templates[selected_tm]
    clone_available = True
    if not tm:
        print('Sorry, template "%s" not found :(' % selected_tm)
        clone_available = False
    elif os.path.isfile(template_path):
        print('Template is already exist in generator template folder')
        answer = helpers.ask_question('Do you want update it?', ['Y', 'N'])
        if answer == 'N':
            clone_available = False
            helpers.init_template_scripts(selected_tm)
        else:
            helpers.remove_template(selected_tm)

    if clone_available:
        print('Cloning template repository...')
        cloned = git.clone(
            tm['git_url'],
            '%s/%s/%s/%s' % (generator_dir, packages_dir, templates_dir, selected_tm)
        )
        if cloned is None:
            print('Failed :(')
        else:
            print('Initialisation template scripts...')
            helpers.init_template_scripts(selected_tm)
