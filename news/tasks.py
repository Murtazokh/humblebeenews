from crawler import get_economy, get_latest, get_siyosat, get_sport
import schedule
import time
import pytz
from datetime import datetime


# Set the time zone to South Korea
tz = pytz.timezone('Asia/Seoul')

# Define the time you want your function to run each day
# In this example, the function will run at 10 PM (22:00) every day in South Korea time
run_time = datetime.strptime('05:00', '%H:%M').time()

# Define the function to run your crawler
def run_crawler():
    # Call your crawler function here
    get_siyosat()
    get_sport()
    get_economy()
    get_latest()

# Define the scheduled job
schedule.every().day.at(run_time.strftime('%H:%M')).do(run_crawler).\
    timezone(tz)

# Run the scheduled job continuously
while True:
    schedule.run_pending()
    time.sleep(1)

