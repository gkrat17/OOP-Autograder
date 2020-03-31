
from configs import repository_name

import os
import subprocess

def download():

    students_file = open('Files/students.txt', 'r')
    students = students_file.read().splitlines()
    students_file.close()

    errors = []

    for student in students:
        dir_path = 'Downloads/' + student
        # Make directory
        os.mkdir(dir_path)
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
