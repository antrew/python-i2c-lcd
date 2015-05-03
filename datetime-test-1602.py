#!/usr/bin/env python

from datetime import datetime
from time import sleep
from time import time

import lcddriver


lcd = lcddriver.lcd(bus=2, address=0x27)

while True:
  dateString = datetime.now().strftime('%y-%m-%d')
  timeString = datetime.now().strftime('%H:%M:%S')
  lcd.display_string(dateString, 1)
  lcd.display_string(timeString, 2)
  sleep(1)
