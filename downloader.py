
from configs import repository_name
from cleaner import create_or_replace_dir

import os
import subprocess

def download():

    students_file = open('Files/students.txt', 'r')
    students = students_file.read().splitlines()
    students_file.close()

    errors = []

    for student in students:
        create_or_replace_dir('Downloads/' + student)

        # Download repository
        command = 'git clone https://github.com/%s/%s Downloads/%s' % (student, repository_name, student)
        process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
        process.wait()

        # Save error if exists
        error = process.returncode
        if error != 0:
            errors.append('%s' % student)

    if len(errors) == 0:
        print('Success\n')
    else:
        print('Errors occurred: %s\n' % ', '.join(errors))

if __name__ == '__main__':
    download()
