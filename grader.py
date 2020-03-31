
import os
import subprocess

from utils import run_process

# public
def run_tests(student, report_name):

    # For JUnit4:
    # for test in [x[:-6] for x in os.listdir('StudentHomework/ClassFiles/Tests')]:
        # system('java -javaagent:Libraries/jacocoagent.jar -cp Libraries/junit-4.13.jar;Libraries/hamcrest-core-1.3.jar;StudentHomework/ClassFiles/Classes;StudentHomework/ClassFiles/Tests org.junit.runner.JUnitCore ' + test)

    error_code = 0

    command = 'java -javaagent:Libraries/jacocoagent.jar -jar Libraries/junit-platform-console-standalone-1.3.1.jar --cp StudentHomework/ClassFiles --scan-class-path --reports-dir Results/%s/%s' % (student, report_name)
    tests_succeed = run_process(command, student, 'Runtime Error')
    if not tests_succeed:
        error_code = -1

    command = 'java -jar Libraries/jacococli.jar report jacoco.exec --classfiles StudentHomework/ClassFiles --sourcefiles StudentHomework/SourceFiles/Classes --csv Results/%s/%s/%s' % (student, report_name, report_name)
    report_succeed = run_process(command, student, 'Runtime Error')
    if not report_succeed:
        error_code += -2

    #  0 - success
    # -1 - tests failed
    # -2 - jacoco failed
    # -3 - both failed
    return error_code

# public
def get_coverage(student, report_name):
    parsed_report = parse_report(student, report_name)
    return covered(parsed_report, 3, 4), covered(parsed_report, 5, 6)

# public
def get_methods_passed(student, report_name):

    jupiter = 'Results/%s/%s/TEST-junit-jupiter.xml' % (student, report_name)
    vintage = 'Results/%s/%s/TEST-junit-vintage.xml' % (student, report_name)

    j_passed, j_failed = parse_junit_report(jupiter)
    v_passed, v_failed = parse_junit_report(vintage)

    return (j_passed + v_passed) * 1.0 / (j_passed + j_failed + v_passed + v_failed)

# public
def write_student_results(student, st_covered_ins, st_covered_brs, methods_passed):
    results = open('Results/results.txt', 'a+')
    results.write('%s %.2f %.2f %.2f\n' % (student, st_covered_ins, st_covered_brs, methods_passed))
    results.close()

def parse_junit_report(path):

    report = open(path, 'r')

    _ = report.readline()
    report_line = report.readline().split('"')

    report.close()

    total = int(report_line[3])
    failed = int(report_line[7])
    passed = total - failed

    return passed, failed

def parse_report(student, report_name):
    parsed_report = []

    result_file = open('Results/%s/%s/%s' % (student, report_name, report_name), 'r')
    result = result_file.read().splitlines()
    result_file.close()

    for i in range(1, len(result)):
        line = result[i]
        data = line.split(',')
        parsed_report.append(data)

    return parsed_report

def covered(parsed_report, missed_i, covered_j):

    def summer(i):
        return sum([int(x[i]) for x in parsed_report])

    missed = summer(missed_i)
    covered = summer(covered_j)
    total = missed + covered

    return (covered * 1.0 / total)
