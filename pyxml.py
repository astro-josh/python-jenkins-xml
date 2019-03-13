from junit_xml import TestSuite, TestCase
import traceback
import subprocess
import re
import html

test_cases = [TestCase('Cell Test', 'Notebook_name', 123.345, 'I am stdout!', 'I am stderr!', file='./this.py')]
ts=[TestSuite("Notebook Tests", test_cases, package="Notebooks")]

# with open('output.xml', 'w') as f:
#     TestSuite.to_file(f, ts, prettyprint=False)
#     f.close()

list_changed_files_cmd = "git show --pretty=format: --name-only master"

changed_file_names = subprocess.check_output(list_changed_files_cmd, shell=True).decode()
changed_file_names = [x for x in changed_file_names.strip().split('\n') if '.py' in x]
print(','.join(changed_file_names))
