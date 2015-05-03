#!/usr/bin/env python

from datetime import datetime
from time import sleep
from time import time

import lcddriver


lcd = lcddriver.lcd(bus=2, address=0x27)

lcd.display_string("Hello world!", 1)
lcd.display_string("I have four lines!", 2)

while True:
  dateString = datetime.now().strftime('Date: %y-%m-%d')
  timeString = datetime.now().strftime('Time: %H:%M:%S')
  lcd.display_string(dateString, 3)
  lcd.display_string(timeString, 4)
  sleep(1)
