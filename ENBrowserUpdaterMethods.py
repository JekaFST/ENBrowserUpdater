# -*- coding: utf-8 -*-
import time
import logging
from datetime import datetime, timedelta
from Const import REFRESH_TIMEOUT, DOMAIN, DEMO_REFRESH_COUNT, REFRESH_TRIES

logging.basicConfig(level=logging.INFO)


def updater(team=None, driver=None):
    driver.login_to_en()
    logging.log(logging.INFO, '%s: Логин в движок команды %s выполнен' % (datetime.utcnow() + timedelta(hours=3), team))
    driver.open_game()
    logging.log(logging.INFO, '%s: Игра %s открыта в движке команды %s' % (datetime.utcnow() + timedelta(hours=3), driver.game_id, team))

    if 'demo' in DOMAIN:
        for i in xrange(DEMO_REFRESH_COUNT):
            __refresh_page(driver, i + 1, team)
    else:
        i = 1
        while True:
            __refresh_page(driver, i, team)
            i += 1

    driver.close_browser()


def __refresh_page(driver, i, team):
    for j in xrange(REFRESH_TRIES):
        try:
            driver.refresh_level_page()
            logging.log(logging.INFO, '%s: Обновление %s игры %s в движке команды %s выполнено' % (datetime.utcnow() + timedelta(hours=3), str(i), driver.game_id, team))
            time.sleep(REFRESH_TIMEOUT)
            break
        except Exception:
            if j != REFRESH_TRIES - 1:
                time.sleep(1)
                continue
            logging.log(logging.ERROR, '%s: Обновление %s игры %s в движке команды %s НЕ ВЫПОЛНЕНО' % (datetime.utcnow() + timedelta(hours=3), str(i), driver.game_id, team))
            time.sleep(REFRESH_TIMEOUT)
