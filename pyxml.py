import traceback
import subprocess
import re
import html
import os


list_changed_files_cmd = "git show --pretty=format: --name-only -r master"

changed_file_names = subprocess.check_output(list_changed_files_cmd, shell=True).decode()
changed_file_names = [os.path.split(x)[1].replace('.py', '') for x in changed_file_names.strip().split('\n')]
print(','.join(changed_file_names))
