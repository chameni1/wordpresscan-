

# XMB version detection
# Rev 1

import cmsdb.basic as cmseek
import re

def start(source):
    regex = re.findall(r'<!-- Powered by XMB (\d.*?) ', source)
    if regex != []:
        if regex[0] != '' and regex[0] != ' ':
            version = regex[0]
            cmseek.success('XMB version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
            return version
    else:
        regex = re.findall(r'Powered by XMB (\d.*?) ', source)
        if regex != []:
            if regex[0] != '' and regex[0] != ' ':
                version = regex[0]
                cmseek.success('XMB version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
                return version

    cmseek.error('Version detection failed!')
    return '0'
