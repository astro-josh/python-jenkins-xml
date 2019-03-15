from pycodestyle import Checker, StyleGuide
import re

source = [
    "firstImage = hdu1[1].data['FLUX'][0]\n",
    "fig = plt.figure(figsize=(8,8))\n",
    "plt.imshow(firstImage, origin = 'lower', cmap = plt.cm.viridis, \\\n",
    "           vmax = np.percentile(firstImage,92), vmin = np.percentile(firstImage,5))\n",
    "plt.xlabel('CCD Column', fontsize = 14)\n",
    "plt.ylabel('CCD Row', fontsize = 14)\n",
    "plt.grid(axis = 'both', color = 'white', ls = 'solid')"
   ]


c = Checker(lines=source, quiet=1, ignore=('W292', 'E122'))
c.check_all()
report = c.report
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
print('\n\n')
print('\n\n'.join(l))
