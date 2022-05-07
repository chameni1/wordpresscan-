

# Sitefinity version detection
# Rev 1

import cmsdb.basic as cmseek
import re

def start(ga_content):
    ga_content = ga_content.lower()
    regex = re.findall(r'sitefinity (.*)', ga_content)
    if regex != []:
        version = regex[0]
        cmseek.success('Sitefinity version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected')
        return version
    else:
        cmseek.error('Version detection failed!')
        return '0'
