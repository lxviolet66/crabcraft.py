"""Handles requests to the CrabCraft API

  * Copyright  (C) 2026  lxviolet@proton.me
  * Licensed under GPL-3 (see LICENSE-GPL-3)
"""

import requests
from requests import Response

URI = 'https://api.crabcraft.net'


def ping() -> Response:
    return requests.get(f'{URI}/ping')


def players() -> Response:
    # TODO: make this better by organising it via server or something idk its 4am im really confused
    # its 40 minutes later and i have no idea wtf this comment was talking about????? organise what via server?? this returns a single element there's nothing to organise I
    return requests.get(f'{URI}/players')


def query(user: str) -> Response:
    # TODO this should also get player position info
    return requests.get(f'{URI}/players/{user}')


def stats(user, category, stat) -> Response:
    ...


# TODO make the nickname_raw thing compatible with the /nick command
