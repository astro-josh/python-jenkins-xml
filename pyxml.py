from junit_xml import TestSuite, TestCase
import traceback
import re
import html

test_cases = [TestCase('Cell Test', 'Notebook_name', 123.345, 'I am stdout!', 'I am stderr!', file='./this.py')]
ts=[TestSuite("Notebook Tests", test_cases, package="Notebooks")]

# with open('output.xml', 'w') as f:
#     TestSuite.to_file(f, ts, prettyprint=False)
#     f.close()
