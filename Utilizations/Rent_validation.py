import datetime

class Rent_validation():
    def __init__(self):
        pass

    def Check_location(self, location):
        if location in ("1", "2", "3"):
            return True
        else:
            return False

    def Check_date(self, dates): # mm//dd//yyyy
        pick_up = dates[0]
        drop_off = dates[1]
        # Checks if dates are valid
    # try:
        mm = int(pick_up[:2])
        dd = int(pick_up[2:4])
        yyyy = int(pick_up[4:8])
        pickup_datetime = datetime.datetime(mm, dd, yyyy, 12)
        dropoff_datetime = datetime.datetime(int(drop_off[:2]), int(drop_off[2:4]), int(drop_off[4:8], 12))
        print(pickup_datetime)
        print(dropoff_datetime)
        input("lol")
        # Time after exactly 1 year
        datetime_after_1year = datetime.datetime.now() + datetime.timedelta(365)  

        if datetime.datetime.now() < (pickup_datetime and dropoff_datetime) < datetime_after_1year \
        and pickup_datetime < dropoff_datetime:
            return True 
    # except(ValueError):
        # return False
