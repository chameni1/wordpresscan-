

# Al Mubda version detection
# Rev 1

import cmsdb.basic as cmseek
import re

def start(source):
    cmseek.statement("Detecting Al Mubda version using source code [Method 1 of 1]")
    regex = re.findall(r'Powered by Al Mubda version (\d.*?)</a>', source)
    if regex != []:
        if regex[0] != '' and regex[0] != ' ':
            version = regex[0]
            cmseek.success('Al Mubda version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
            return version

    cmseek.error('Version detection failed!')
    return '0'
