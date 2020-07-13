import sys
import os
import errno
from datetime import datetime

name = "{query}"
sys.stdout.write(name)

title = name.title()
file_name = "{}-{}.md".format(
    datetime.today().strftime('%Y-%m-%d'),
    name.replace(' ', '-').lower()
)
folder = os.environ.get('noteable_folder')
home = os.getenv("HOME")
if folder:
    if folder.startswith('~'):
        folder = home + folder[1:]
else:
    folder = "{}/.notable".format(home)
if folder.endswith('notes') or folder.endswith('notes/'):
    pass
else:
    if folder.endswith('/'):
        folder = '{}notes'.format(folder)
    else:
        folder = '{}/notes'.format(folder)
if folder.endswith('/'):
    folder = folder[:-1]

try:
    os.makedirs(folder)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

template_path = '{}{}template.txt'.format(folder, os.sep)
if os.path.isfile(template_path):
    template = open(template_path, 'r').read()
else:
    template = """# {title}

## Agenda

1. 
2.

## Tasks

* [x] Task One
+ [ ] Task Two 

## Remarks

| Task | Your Remark |
| ------ | ----- |
| Task One | I got it done without any issue |
| Task Two | Had some problem with foo bar |

---

[Cheatsheet](https://cheatsheet.md/notable.pdf) :smile:
"""

if os.environ.get('no_template'):
    data = ""
else:
    data = template.format(title=title)

with open("{}{}{}".format(folder, os.sep, file_name), 'w') as f:
    f.write(data)
    f.close()
