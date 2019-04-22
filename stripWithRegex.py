import re

regex_whitespaces = re.compile(r'^(\s*)(.*?)(\s*)$')


def strip(string, letter=None):
    if not isinstance(string, str):
        print('Not a string')
        return False
    elif letter is None:
        mo = regex_whitespaces.search(string)
        print(mo.groups())
        stripped = mo.group(2)
        print(stripped)
        return True
    else:
        letter = re.escape(letter)
        stripLetter = re.compile(r'^[{0}]+|[{0}]+$'.format(letter))
        return re.sub(stripLetter, '', string)
    return False


x = 10
print(strip('as ss saaaaaaaaas    s  s   sa', 's'))
