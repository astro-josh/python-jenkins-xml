from junit_xml import TestSuite, TestCase

test_cases = [TestCase('Cell Test', 'Notebook 1', 123.345, 'I am stdout!', 'I am stderr!')]
ts = [TestSuite("Notebook Tests", test_cases)]

with open('output.xml', 'wb') as f:
    TestSuite.to_file(f, ts, prettyprint=False)
    f.close()
