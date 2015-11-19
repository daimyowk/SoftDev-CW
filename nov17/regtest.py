import re

def find_pone(s):
    result = re.findall("[0-9]{3}",s)
    return result

##looking for character 0-9 three times
