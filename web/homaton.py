#!/usr/bin/python

import time
import web
import RPi.GPIO as GPIO
import thread

# GPIO pin config
#gpios = [21, 22, 23, 24, 10, 9, 25, 11, 8, 7]

       #   all   1   2   3   4 
gpios = [[   7, 21, 22, 23, 24 ], #  on 
         [   8, 10,  9, 25, 11 ]] # off

hightime = 1

# setup GPIOs
GPIO.setmode(GPIO.BCM)
for ps in gpios:
  for p in ps:
    GPIO.setup(p, GPIO.OUT)

# test GPIOs
#for p in gpios:
#  GPIO.output(p, GPIO.HIGH)
#  time.sleep(0.2)
#  GPIO.output(p, GPIO.LOW)

render = web.template.render("templates/")

urls = (
#  '/api/form', 'api_form',
  "/api/([0-9a-z]+)", "api",
  "/", "index",
  "/favicon.ico", "favicon"
)

#class api_form:
#  def POST(self):
#    print web.data()
#    raise web.seeother("/")
class api:
  def POST(self, switch):
    print "api:"
    print switch
    state = web.data()
    print state
    switchToStateBackground(switch, state)
    web.header("Cache-Control", "no-cache")
    return "ok"

class index:
  def GET(self):
    return render.index()
  def POST(self):
    input = web.input()
    command = input.command
    print command
    switch, state = command.split(":")
    switchToStateBackground(switch, state)
    web.header("Cache-Control", "no-cache")
    return render.index()

class favicon:
  def GET(self):
    raise web.seeother("/static/favicon.png")

def switchToStateBackground(switch, state):
    thread.start_new_thread(switchToState, (switch, state))

def switchToState(switch, state):
    #print "switch: " + switch
    #print "state: " + state
    #i = ((int("5" if (switch == "all") else switch)-1) * 2) + (1 if (state == "on") else 0)
    #p = gpios[i]
    ist = 0 if state == "on" else 1
    #isw = 0 if switch == "all" else int(switch)
    #isws = [1, 2, 3, 4] if switch == "all" else [int(switch)]
    isws = [0] if switch == "all" else [int(switch)]
    for isw in isws:
      print "switch: {0}, {1}".format(switch, isw)
      print "state:  {0}, {1}".format(state, ist)
      p = gpios[ist][isw]
      print "pin:    {0}".format(p)
      GPIO.output(p, GPIO.HIGH)
      time.sleep(hightime)
      GPIO.output(p, GPIO.LOW)
    return

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()

#for i in range(0,10):
#  GPIO.output(18, GPIO.HIGH)
#  time.sleep(0.1)
#  GPIO.output(18, GPIO.LOW)
#  GPIO.output(24, GPIO.HIGH)
#  time.sleep(0.1)
#  GPIO.output(24, GPIO.LOW)

