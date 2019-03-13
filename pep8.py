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

source = [
"job = HSC_service.launch_job(\"\"\"\n",
"SELECT TOP 10 MatchID, MatchRA, MatchDec, TargetName, StartTime, StopTime, TargetName \n",
"FROM dbo.SumMagAper2CatView\n",
"WHERE \n",
"CONTAINS(POINT('ICRS', MatchRA, MatchDec),CIRCLE('ICRS',129.23,7.95,0.1))=1\n",
"AND StartTime > '2015-01-01' AND StopTime < '2015-04-01'\n",
"\"\"\")\n",
"HSC_results = job.get_results()\n",
"HSC_results"
]


c = Checker(lines=source, quiet=0, ignore='W292')
c.check_all()
report = c.report
l = []
print(type(source))
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

print("\n\nstart of list")
print('\n\n'.join(l))
