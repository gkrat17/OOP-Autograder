
import os
import shutil

from configs import repository_name

# public, Variable Function
def remove_junk(javas):

    for i in reversed(range(len(javas))):
        java = javas[i]

        if any(x in java[1] for x in ['Shape', 'Point']):
            javas.pop(i)

# public
def get_student_javas(student):
    return get_javas('Downloads/%s' % student)

# public
def get_tests():
    test_files = os.listdir('Tests')
    tests = []
    for test in test_files:
        tests.append(('Tests', test))
    return tests

# public
def get_javas(dir):

    files = os.listdir(dir)
    javas = []

    for entry in files:
        path = os.path.join(dir, entry)

        if os.path.isdir(path):
            javas += get_javas(path)
        else:
            if path.endswith('.java'):
                javas.append((dir, entry))

    return javas

# public
def sort_javas(javas):
    classes, tests = [], []

    for java in javas:
        if java[1].endswith('Test.java'):
            tests.append(java)
        else: classes.append(java)

    return classes, tests

# public
def copy_files(files, new_dir):
    for dir, file in files:
        shutil.copyfile('%s/%s' % (dir, file), '%s/%s' % (new_dir, file))
