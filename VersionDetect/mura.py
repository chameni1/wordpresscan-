

# Mura CMS version detection
# Rev 1

import cmsdb.basic as cmseek
import re

def start(ga_content):
    regex = re.findall(r'Mura CMS (.*)', ga_content)
    if regex != []:
        version = regex[0]
        cmseek.success('Mura CMS version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
        return version
    else:
        cmseek.error('Version detection failed!')
        return '0'
