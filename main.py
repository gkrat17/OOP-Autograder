
import os

from sorter import get_student_javas, sort_javas, remove_junk, copy_files, get_tests
from pregrader import compile_classes_and_tests
from grader import run_tests, get_coverage, write_student_results, get_methods_passed
from cleaner import clean, create_or_replace_dir

def main():

    # Clear errors.txt
    open('Files/errors.txt', 'w').close()

    # Read students.txt
    students_file = open('Files/students.txt', 'r')
    students = students_file.read().splitlines()
    students_file.close()

    clean() # Who knows...

    for student in students:
        create_or_replace_dir('Results/%s' % student)

        # Get student Classes and Tests paths
        student_javas = get_student_javas(student)
        student_classes, student_tests = sort_javas(student_javas)

        # Remove junk from 'student_classes' and 'student_tests'
        remove_junk(student_classes)
        remove_junk(student_tests)

        # Copy 'student_classes' and 'student_tests' in appropriate directories
        copy_files(student_classes, 'StudentHomework/SourceFiles/Classes')
        copy_files(student_tests, 'StudentHomework/SourceFiles/Tests')

        # Compile java files set above - 'student_classes' and 'student_tests'
        compiled_succesfully = compile_classes_and_tests(student)

        if not compiled_succesfully:
            print('%s: Student Classes and Student Tests did not compiled successfully' % student)
            clean()
            continue # CompileTime error is stored in errors.txt

        report_name = 'student_tests_result'
        testing_result = run_tests(student, report_name)

        if testing_result < 0:
            print('%s: Some RunTime error occurred while executing Student Tests: %d' % (student, testing_result))
            # clean()
            # continue # testing running or report running RunTime error is stored in errors.txt
        # else report is generated

        # Parse and save student tests result for future
        # st_covered_ins - student tests covered instructions
        # st_covered_brs - student tests covered branches
        st_covered_ins, st_covered_brs = (0.0, 0.0) if testing_result < -1 else get_coverage(student, report_name)

        # Clean everythin except Classes
        clean(clean_classes = False)

        # Get tests
        tests = get_tests()

        # Copy test files in appropriate directory for testing
        copy_files(tests, 'StudentHomework/SourceFiles/Tests')

        # Compile 'student_classes' and 'tests'
        compiled_succesfully = compile_classes_and_tests(student)

        if not compiled_succesfully:
            print('%s: Student Classes and Tests did not compiled successfully' % student)
            write_student_results(student, st_covered_ins, st_covered_brs, 0.0)
            clean()
            continue # CompileTime error is stored in errors.txt

        report_name = 'tests_result'
        testing_result = run_tests(student, report_name)

        if testing_result < -1:
            print('%s: Some RunTime error occurred in Jacoco while executing Tests: %d' % (student, testing_result))
            # write_student_results(student, st_covered_ins, st_covered_brs, 0.0)
            # clean()
            # continue # testing running or report running RunTime error is stored in errors.txt
        # else report is generated

        # t_covered_ins - tests covered instructions
        # t_covered_brs - tests covered branches
        methods_passed = 0.0 if testing_result < -1 else get_methods_passed(student, report_name)

        # Save results
        write_student_results(student, st_covered_ins, st_covered_brs, methods_passed)

        # Cleanup for next student
        clean()

if __name__ == '__main__':
    main()
