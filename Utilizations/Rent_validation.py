import datetime

class Rent_validation():

    def Check_location(self, location):
        if location in ("1", "2", "3"):
            return True
        else:
            return False

    def Check_date(self, dates): # mm//dd//yyyy
        pick_up = dates[0]
        drop_off = dates[1]
        # Time after exactly 1 year
        date_after_1year = datetime.date.today() + datetime.timedelta(365)  
        # Checks if dates are valid
        try:
            pickup_date = datetime.date(int(pick_up[4:8]), int(pick_up[:2]), int(pick_up[2:4]))
            dropoff_date = datetime.date(int(drop_off[4:8]), int(drop_off[:2]), int(drop_off[2:4]))
        except(ValueError):
            return False
        # Checks if pick_up- and drop_off dates are bigger than the date today and smaller than the date after 1 year
        # Also checks if pick_up date is smaller than drop_off date
        if datetime.date.today() < pickup_date < date_after_1year \
            and datetime.date.today() < dropoff_date < date_after_1year \
            and pickup_date < dropoff_date:         
            return True 
        else: 
            return False

    def Check_vehicle_size(self, vehicle_size):
        if vehicle_size in ("a", "b", "c"):
            return True
        else:
            return False
        
