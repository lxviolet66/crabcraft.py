"""CLI Interface for use via with python3 -m crabcraft.py

  * Copyright  (C) 2026  lxviolet@proton.me
  * Licensed under GPL-3 (see LICENSE-GPL-3)
"""

__version__ = '1.0'
__author__ = 'lxviolet'

import sys
import json
from typing import Any
from ast import literal_eval

from requests import Response
from rich import print_json

import api
from docopt import docopt


class BudgetGoto(Exception):
    """Used to escape from try blocks"""


HELP_MESSAGE = """crabcraft.py
Usage:
  crabcraft.py [-j] ping
  crabcraft.py [-j] players
  crabcraft.py [-j] query <user>
  crabcraft.py [-j] stats <user> <category> <stat> 
  crabcraft.py (-h | --help)
  crabcraft.py --version

Options:
  -h --help  
  --version  
  -j --json
"""

args = docopt(HELP_MESSAGE, version=__version__)
print(args, '\n')

response: Response | None = None
content: str = ''
match = False

# HACK: We modify content as if it were json by converting from str to
# dict with literal_eval, using dict methods, then converting back to
# to str. This works but there's definitely a better way, perhaps
# content.json() (DUMBASS)
# FIXME: this is ugly! really ugly! i hate this! fix this! this sucks!
try:
    if args['ping'] == True:
        if match:
            raise BudgetGoto
        match = True
        response = api.ping()
        content = response.content.decode()

    if args['players'] == True:
        if match:
            raise BudgetGoto
        match = True
        response = api.players()
        content = response.content.decode()

    if args['query'] == True:
        if match:
            raise BudgetGoto
        match = True
        response = api.query(args['<user>'])
        content = response.content.decode()
        x = ''.join([i.capitalize() for i in content.replace('{', '').replace('}', '').replace('"', '').replace(':', ': ').replace(',', '\n').split(' ')]).replace(':', ': ').split('\n')
        x.pop(1)
        content = '\n'.join(x)
    
    if args['stats'] == True:
        if match:
            raise BudgetGoto
        match = True
        response = api.stats(args['<user>'], args['<category>'], args['<stat>'])
        content = response.content.decode()

except BudgetGoto:
    ...

if not isinstance(response, Response):
    print(HELP_MESSAGE, end='')
    sys.exit()

if args['--json']:
    print_json(content)
else:
    print(''.join([i.capitalize() for i in content.replace('{', '').replace('}', '').replace('"', '').replace(':', ': ').replace(',', '\n').split(' ')]).replace(':', ': '))
