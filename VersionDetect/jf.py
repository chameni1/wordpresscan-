
# JForum version detection
# Rev 1

import cmsdb.basic as cmseek
import re

def start(source):
    regex = re.search(r'Powered by(.*?)JForum (\d.*?)</a>', source)
    if regex != None:
        try:
            version = regex.group(2)
            cmseek.success('JForum version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
            return version
        except Exception as e:
            cmseek.error('Version detection failed!')
            return '0'

    cmseek.error('Version detection failed!')
    return '0'
