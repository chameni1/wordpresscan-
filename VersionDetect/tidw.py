
## TiddlyWiki version detection
## Rev 1

import re
import cmsdb.basic as cmseek

def start(source):
    version = '0'
    if 'major:' in source and 'minor:' in source and 'revision:' in source:
        major = re.findall(r'major: (.*?),',source)
        minor = re.findall(r'minor: (.*?),',source)
        rev = re.findall(r'revision: (.*?),',source)
        if major != [] and minor != [] and rev != []:
            version = major[0] + '.' + minor[0] + '.' + rev[0]
            cmseek.success('TiddlyWiki version ' + cmseek.bold + cmseek.fgreen + version + cmseek.cln + ' detected!')
        else:
            cmseek.warning('Version detection failed!')
    else:
        cmseek.warning('Version detection failed!')
    return version
