from time_module import get_hours,get_date
from output_module import output
from database import update_last_seen,get_last_seen
from datetime import date


def greats():

    today = get_date()
    update_last_seen(today)
    previous_date = get_last_seen()
    today_date = date.today()
    if previous_date == today:
        output("welcome ser")
    else:
        hour = int(get_hours())

        if hour >= 4 and hour<12:
            output("good morning")
        elif hour >= 12 and hour<16:
            output("good after noon")
        else:
            output("good evening")



