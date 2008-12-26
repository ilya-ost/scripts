#!/usr/bin/env python2.5

import dbus
import sys

bus = dbus.SessionBus()
qstardict = bus.get_object('org.qstardict.dbus', '/qstardict')
qstardict.showPopup(sys.argv[1])

