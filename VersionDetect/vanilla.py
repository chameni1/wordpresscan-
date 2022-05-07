

# Vanilla version detection
# Rev 1

import cmsdb.basic as cmseek
import re

def start(url, ua):
    kurama = cmseek.getsource(url, ua)
    header = kurama[2].split('\n')
    regex = []
    for tail in header:
        if 'X-Garden-Version: Vanilla' in tail:
            regex = re.findall(r'X-Garden-Version: Vanilla (\d.*)', tail)
    if regex != []:
        cmseek.success('Vanilla version ' + cmseek.bold + cmseek.fgreen + regex[0] + cmseek.cln + ' detected')
        return regex[0]
    else:
        cmseek.error('Version detection failed!')
        return '0'
