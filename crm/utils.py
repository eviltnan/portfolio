from datetime import timedelta

import holidays


def get_working_days(start_date, end_date):
    days = [start_date + timedelta(days=1) * i for i in range(
        (end_date - start_date).days + 1
    )]

    working_days = []
    for day in days:
        if day in holidays.DE(prov='BE') or day.weekday() in [5, 6]:
            continue
        working_days.append(day)
    return working_days
