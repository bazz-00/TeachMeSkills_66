import os
import string
import json
def alpha():
    os.makedirs('alpha')
    os.chdir('alpha')
    for i in string.ascii_uppercase:
        f = open(str(i), 'w')
        f.write(str(i))


def to_json(file):
    dlina = {}
    with open(file) as f:
        for i in f:
            f1 = i.split()
            s = len(f1)
            dlina[s] = f1
    new_dlina = json.dumps(dlina, indent=2)
    return new_dlina




