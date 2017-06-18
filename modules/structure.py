import os, shutil
from modules import helpers, constants


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


# def move(paths=[''], name=''):
#     for path in paths:
#         shutil.move(path, '%s/%s' % (constants.paths.projects, name))


# def format(project_structure, name):
#     print(project_structure)