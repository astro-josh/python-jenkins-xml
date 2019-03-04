from junit_xml import TestSuite, TestCase

test_cases = [TestCase('Cell Test', 'Notebook 1', 123.345, 'I am stdout!', 'I am stderr!')]
test_cases[0].add_failure_info('Invalid File')
ts = TestSuite("Notebook Tests", test_cases)
# pretty printing is on by default but can be disabled using prettyprint=False
print(TestSuite.to_xml_string(ts, prettyprint=False))

with open('test-report.xml', mode='a') as file:
    TestSuite.to_file(file, ts, prettyprint=False)
    file.close()
