import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "etc/hosts"
redirect = "127.0.0.1"
website_list = ["https://github.com/pushshift/api", "https://www.github.com/pushshift/api", "http://redditsearch.io/", "http://www.redditsearch.io/"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours....")
    else:
        print("You're off")
    time.sleep(5)    
    
        