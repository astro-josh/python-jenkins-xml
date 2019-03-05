from pycodestyle import *
import os

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


c = Checker(lines=code, quiet=0, ignore='W292', show_source=True)
c.check_all()

print(c.report._deferred_print)
