
import os
import subprocess

from utils import run_process

def compile_classes_and_tests(student):

    output_dir = 'StudentHomework/ClassFiles'
    additional_cps = 'Libraries/junit-platform-console-standalone-1.3.1.jar'
    to_compile = []

    # Classes
    to_compile += get_full_path_files('StudentHomework/SourceFiles/Classes')
    # Tests
    to_compile += get_full_path_files('StudentHomework/SourceFiles/Tests')

    command = 'javac -d %s -cp %s %s' % (output_dir, additional_cps, ' '.join(to_compile))
    return run_process(command, student, 'Compilation Error')

def get_full_path_files(dir):
    files = []
    for file in os.listdir(dir):
        files.append('%s/%s' % (dir, file))
    return files
