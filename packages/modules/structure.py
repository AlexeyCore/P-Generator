import os, shutil
from packages.modules.state import g_state
from distutils.dir_util import copy_tree


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


def copy_template(path=''):
    dst = '%s/%s' % (g_state.get('projects_path'), g_state.get('name'))
    copy_tree(path, dst)


def restructuring():
    print('Copying template structure')
    projects_path = g_state.get('projects_path')
    generator_dir = g_state.get('generator_dir')
    packages_dir = g_state.get('packages_dir')
    templates_dir = g_state.get('templates_dir')
    template_name = g_state.get('template')
    template_tree_dir = g_state.get('template_tree_dir')
    template_tree_path = '%s/%s/%s/%s/%s/%s' % (
        projects_path,
        generator_dir,
        packages_dir,
        templates_dir,
        template_name,
        template_tree_dir
    )

    # Copy template tree
    copy_template(template_tree_path)
