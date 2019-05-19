# -*- coding: utf-8 -*-
import time
import logging
import threading
from ENDriver import ENChromeDriver
from datetime import datetime, timedelta
from Const import SESSIONS_DATA, REFRESH_TIMEOUT, DOMAIN, DEMO_REFRESH_COUNT


def updater(team=None, driver=None):
    driver.login_to_en()
    logging.log(logging.INFO, '%s: Логин в движок команды %s выполнен' % (datetime.utcnow() + timedelta(hours=3), team))
    driver.open_game()
    logging.log(logging.INFO, '%s: Игра %s открыта в движке команды %s' % (datetime.utcnow() + timedelta(hours=3), driver.game_id, team))

    if 'demo' in DOMAIN:
        for i in xrange(DEMO_REFRESH_COUNT):
            driver.refresh_level_page()
            # datetime.utcnow()
            logging.log(logging.INFO, '%s: Обновление %s игры %s в движке команды %s выполнено' % (datetime.utcnow() + timedelta(hours=3), str(i+1), driver.game_id, team))
            time.sleep(REFRESH_TIMEOUT)
    else:
        i = 1
        while True:
            driver.refresh_level_page()
            logging.log(logging.INFO, '%s: Обновление %s игры %s в движке команды %s выполнено' % (datetime.utcnow() + timedelta(hours=3), str(i), driver.game_id, team))
            i += 1
            time.sleep(REFRESH_TIMEOUT)
    driver.close_browser()

logging.basicConfig(level=logging.INFO)
en_drivers = [{'team': team, 'driver': ENChromeDriver(*session_data)} for team, session_data in SESSIONS_DATA.items()]
for en_driver in en_drivers:
    threading.Thread(name=en_driver['team'], target=updater, args=(en_driver['team'], en_driver['driver'])).start()
