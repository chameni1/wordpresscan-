

# NodeBB version detection
# Rev 1

import cmsdb.basic as cmseek
import re

def start(source):
    regex = re.search(r'var config(.*?)"version":"(\d.*?)"', source)
    if regex != None:
        try:
            version = regex.group(2)
            if version != "":
                cmseek.success('NodeBB version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
                return version
        except Exception as e:
            cmseek.error('lol detection failed!')
            return '0'
    cmseek.error('Version detection failed!')
    return '0'
