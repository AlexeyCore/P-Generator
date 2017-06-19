import os, shutil
from packages.modules.state import g_state


def remove_files(files_and_dirs=['']):
    errors = []
    for file_or_dir in files_and_dirs:
        try:
            if os.path.isdir(file_or_dir):
                shutil.rmtree(file_or_dir, ignore_errors=True)
            else:
                os.remove(file_or_dir)
        except OSError:
            errors.append('OSError')
            pass
    return len(errors)


def mk_dirs(directory_paths=['']):
    errors = []
    for directory_path in directory_paths:
        try:
            os.makedirs(directory_path)
        except OSError:
            errors.append('OSError')
            pass
    return len(errors)


def create_project_dir():
    os.mkdir('%s/%s' % (g_state.get('projects_path'), g_state.get('name')))


def move(paths=['']):
    for path in paths:
        shutil.move(path, '%s/%s' % (g_state.get('projects_path'), g_state.get('name')))


def make_project_structure(structure={}):
    print('Initializing the template structure')
