#!/usr/bin/python

from __future__ import print_function
import sys
import time
import RPi.GPIO as GPIO
import emw100
import web
import thread

# setup GPIOs
gpio = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio, GPIO.OUT)

urls = (
  "/api/([0-9a-z]+)", "api"
)

class api:
  def POST(self, switch):
    state = web.data()
    print("api: {} {}".format(switch, state))
    switchToStateBackground(switch, state)
    web.header("Cache-Control", "no-cache")
    return "ok"

def switchToStateBackground(switch, state):
    thread.start_new_thread(switchToState, (switch, state))

def switchToState(switch, state):
    button = int(switch) - 1
    command = 1 if state == "on" else 0
    print("switch: {} {}".format(button, command))
    emw100.sendEmw(gpio, 0, button, command)
    return

if __name__ == "__main__":
    try:
      app = web.application(urls, globals())
      app.run()

    except KeyboardInterrupt as e:
        print("shutting down...", file=sys.stderr)
        GPIO.output(gpio, GPIO.LOW)

    finally:
        print("gpio cleanup...", file=sys.stderr)
        GPIO.cleanup()
