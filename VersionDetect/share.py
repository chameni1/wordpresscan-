

# Microsoft SharePoint Version detection
# Rev 1
import cmsdb.basic as cmseek
import re

def start(url, ua):
    kurama = cmseek.getsource(url, ua)
    header = kurama[2].split('\n')
    regex = []
    for tail in header:
        if 'MicrosoftSharePointTeamServices' in tail:
            regex = re.findall(r'MicrosoftSharePointTeamServices: (.*)', tail)
    if regex != []:
        cmseek.success('SharePoint version ' + cmseek.bold + cmseek.fgreen + regex[0] + cmseek.cln + ' detected')
        return regex[0]
    else:
        cmseek.error('Version detection failed!')
        return '0'
