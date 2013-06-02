#!/bin/bash
cd /home/pi/homaton/web
#echo >> std.out
#echo >> std.err
#echo $(date --iso-8601=seconds) started >> std.out
#echo $(date --iso-8601=seconds) started >> std.err
echo >> stdio.log
echo $(date --iso-8601=seconds) started >> stdio.log
#exec nohup sudo python homaton.py >> std.out 2>> std.err < /dev/null &
#python homaton.py >> stdio.log 2>&1 < /dev/null 
python homaton.py
#exec /home/pi/homaton/start.sh >> /home/pi/homaton/std.out 2>> /home/pi/homaton/std.err &
