

# SeamlessCMS version detection
# Rev 1

import cmsdb.basic as cmseek
import re

def start(source):
    regex = re.findall(r'Published by Seamless.CMS.WebUI, (.*?) -->', source)
    if regex != []:
        version = regex[0]
        cmseek.success('SeamlessCMS version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
        return version
    else:
        cmseek.error('Version detection failed!')
        return '0'
