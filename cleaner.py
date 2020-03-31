
import shutil
import stat
import os

def clean(clean_classes = True):
    create_or_replace_dir('StudentHomework/ClassFiles')

    if clean_classes:
        create_or_replace_dir('StudentHomework/SourceFiles/Classes')
    create_or_replace_dir('StudentHomework/SourceFiles/Tests')

    jacoco = 'jacoco.exec'
    if os.path.exists(jacoco):
        os.remove(jacoco)

def create_or_replace_dir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)
