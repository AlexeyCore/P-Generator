from modules import constants, git
from modules.state import g_state


def clone_template():
    selected_tm = g_state.get('template')
    tm = constants.templates[selected_tm]
    if not tm:
        print('Sorry, template "%s" not found :(' % selected_tm)
    else:
        print('Cloning template repository...')
        coned = git.clone(tm['git_url'], selected_tm)
        print(coned)
