import traceback
import subprocess
import re
import html


list_changed_files_cmd = "git show --pretty=format: --name-only master"

changed_file_names = subprocess.check_output(list_changed_files_cmd, shell=True).decode()
changed_file_names = [x for x in changed_file_names.strip().split('\n') if '.py' in x]
print(','.join(changed_file_names))
