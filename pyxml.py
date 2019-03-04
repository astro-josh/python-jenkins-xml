from junit_xml import TestSuite, TestCase

test_cases = [TestCase('Cell Test', 'Notebook 1', 123.345, 'I am stdout!', 'I am stderr!')]
test_cases[0].add_failure_info('Invalid File')
test_cases[0].elapsed_sec = 69
ts = [TestSuite("Notebook Tests", test_cases)]

with open('test-report.xml', mode='w') as file:
    TestSuite.to_file(file, ts, prettyprint=False)
    file.close()
