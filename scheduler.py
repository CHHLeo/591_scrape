import subprocess
import os
import sys
import signal
import time
from threading import Thread
import cPickle as pickle

from apscheduler.schedulers.blocking import BlockingScheduler
from rent_scrape import rent_neihulu
from rent_scrape import rent_xingshan
import logging
import socket
import sys

lock_socket = None  # we want to keep the socket open until the very end of


# our script so we use a global variable to avoid going
# out of scope and being garbage-collected

def is_lock_free():
    global lock_socket
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        lock_id = "ch2leo./home/ch2leo/mysite/591_scrape/scheduler.py"  # this should be unique. using your username as a prefix
        # is a convention
        lock_socket.bind('\0' + lock_id)
        logging.debug("Acquired lock %r" % (lock_id,))
        return True
    except socket.error:
        # socket already locked, task must already be running
        logging.info("Failed to acquire lock %r" % (lock_id,))
        return False


if not is_lock_free():
    sys.exit()

scheduler = BlockingScheduler()
scheduler.add_job(rent_xingshan, 'interval', minutes=30)
scheduler.add_job(rent_neihulu, 'interval', minutes=30)
scheduler.start()

# def signal_term_handler(signal, frame):
#     print 'got SIGTERM'
#     sys.exit(0)
#
#
# signal.signal(signal.SIGTERM, signal_term_handler)
# try:
#     scheduler = BlockingScheduler()
#     scheduler.add_job(rent_neihulu, 'interval', seconds=5)
#     scheduler.add_job(rent_xingshan, 'interval', seconds=5)
#     scheduler.start()
# except:
#     subprocess.Popen([sys.executable, ''.join(sys.argv)])
# python = sys.executable
# os.execl(python, python, *sys.argv)
