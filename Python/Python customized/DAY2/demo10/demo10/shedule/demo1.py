import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
    print ('EVENT:', (time.time()*1000), name)

print ('START:', (time.time()*1000))
scheduler.enter(3, 1, print_event, ('first',))
scheduler.enter(2, 1, print_event, ('second',))

scheduler.run()


