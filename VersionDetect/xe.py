

# XpressEngine version detection
# Rev 1
import cmsdb.basic as cmseek
import re

def start(ga_content):
    regex = re.findall(r'XpressEngine (.*)', ga_content)
    if regex != []:
        cmseek.success('XpressEngine version ' + cmseek.bold + cmseek.fgreen + regex[0] + cmseek.cln + ' detected')
        return regex[0]
    else:
        cmseek.error('Version detection failed!')
        return '0'
