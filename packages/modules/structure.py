import os, shutil, re
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


# TODO: get files sheme from template path
def restructure_file_content(files=[], t_vars={}):
    reg_ex = r'%{(.*?)}%'
    files_path = '%s/%s' % (g_state.get('projects_path'), g_state.get('name'))
    for file_path in files:
        file = open('%s/%s' % (files_path, file_path), 'r+')
        f_content = file.read()
        template_values = re.findall(reg_ex, f_content)
        if template_values:
            for template_value in template_values:
                if template_value in t_vars:
                    f_content = re.sub(r'%{%s}%' % template_value, t_vars[template_value], f_content)
                else:
                    f_content = re.sub(r'%{%s}%' % template_value, '', f_content)
                file.seek(0)
                file.truncate()
                file.write(f_content)


def restructuring():
    print('Copying template structure...')
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
