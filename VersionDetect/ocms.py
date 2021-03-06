

# OpenCms Version detection
# Rev 1
import cmsdb.basic as cmseek
import re

def start(url, ua):
    kurama = cmseek.getsource(url, ua)
    header = kurama[2].split('\n')
    regex = []
    for tail in header:
        if 'Server' in tail and 'OpenCms' in tail:
            regex = re.findall(r'Server: OpenCms/(.*)', tail)
    if regex != []:
        cmseek.success('OpenCms version ' + cmseek.bold + cmseek.fgreen + regex[0] + cmseek.cln + ' detected')
        return regex[0]
    else:
        cmseek.error('Version detection failed!')
        return '0'
