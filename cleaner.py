
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

    def on_rm_error(func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)

    if os.path.exists(dir):
        shutil.rmtree(dir, onerror = on_rm_error)

    os.makedirs(dir)
