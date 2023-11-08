# https://www.tutorialspoint.com/how-to-convert-timestamp-string-to-datetime-object-in-python

from datetime import datetime, timezone
import pytz

def est_to_utc():
    # Get the current UTC time
    utc_time = datetime.utcnow()

    # Make it aware of the UTC timezone
    utc_time = utc_time.replace(tzinfo=pytz.utc)

    # Convert it to EST timezone
    est_time = utc_time.astimezone(pytz.timezone("US/Eastern"))

    # Print the results
    print("UTC time:", utc_time)
    print("EST time:", est_time)

def get_today_datetime():
    now = datetime.now()
    print(now)
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    print("date and time =", dt_string)
    timestamp = now.replace(tzinfo=timezone.utc).timestamp()
    print(timestamp)


def utc_now():
    est_to_utc()
    print("_*_"*20)
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    print("date and time =", dt_string)
    dt_utc = now.replace(tzinfo=timezone.utc)
    print("date and time (UTC) : ", dt_utc)
    dt_utc_string = dt_utc.strftime("%m/%d/%Y %H:%M:%S")
    print(dt_utc_string)



if __name__ == '__main__':
    get_today_datetime()
    utc_now()