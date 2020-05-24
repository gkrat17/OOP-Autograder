
import subprocess

# public
def run_process(command, student, error_type):

    process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    # Wait for the process to terminate
    out, err = process.communicate()

    if process.returncode != 0:
        errors_file = open('Files/errors.txt', 'a+')
        errors_file.write('%s %s:\nstderr:\n%s\nstdout:\n%s\n\n' % (student, error_type, str(err), str(out)))
        errors_file.close()
        return False # failed

    return True # success
