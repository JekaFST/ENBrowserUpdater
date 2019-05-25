# -*- coding: utf-8 -*-
import threading
from Const import SESSIONS_DATA
from ENDriver import ENChromeDriver
from ENBrowserUpdaterMethods import updater

en_drivers = [{'team': team, 'driver': ENChromeDriver(*session_data)} for team, session_data in SESSIONS_DATA.items()]
for en_driver in en_drivers:
    threading.Thread(name=en_driver['team'], target=updater, args=(en_driver['team'], en_driver['driver'])).start()
