from pycodestyle import Checker
import re

code = [
"# Retrieve the IR/F160W calibrated FLT and SPT data products  \n",
"\n",
"\n",
"science_list =Observations.query_criteria(proposal_id='13926', filters='F160W')\n",
"\n",
"Observations.download_products(science_list['obsid'], mrp_only=False, download_dir='./science',\n",
"                               productSubGroupDescription=['FLT', 'SPT'])\n",
"\n",
"science_files =glob.glob(os.path.join(os.curdir,'science', 'mastDownload', 'HST', '*', '*fits'))\n",
"for im in science_files:\n",
"    root=im.split('/')[-1]\n",
"    os.rename(im,'./' + root)\n",
"shutil.rmtree('science/')"
]


c = Checker(lines=code, quiet=0, ignore='W292')
c.check_all()
report = c.report
print(len(report._deferred_print))
l = []
for line_number, offset, code, text, doc in report._deferred_print:
    if line_number > len(report.lines):
        line = ''
    else:
        line = report.lines[line_number - 1]
    l.append('%(path)s:%(row)d:%(col)d: %(code)s %(text)s \n%(source)s' % {
        'path': report.filename,
        'row': report.line_offset + line_number, 'col': offset + 1,
        'code': code, 'text': text, 'source': line.rstrip() + "\n" + re.sub(r'\S', ' ', line[:offset]) + '^',
    })
    #print(line.rstrip())
    #print(re.sub(r'\S', ' ', line[:offset]) + '^')
print("\n\n\n")
print('\n\n'.join(l))
