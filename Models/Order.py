from Customer import Customer

class Order(Customer):
    def __init__(self, name, phone, cust_email, creditcard, order_num, datetime, plate_number):  
        # Gæti verið cust_ID frekar
        Customer.__init__(self, name, phone, cust_email, creditcard) 
        ### Hægt að gera þetta á skilvirkari hátt?? ###
        self.order_num = order_num  
        self.datetime = datetime
        self.plate_number = plate_number    # Sækir þetta hjá "Car" klasanum með get skipun

    def __str__(self):
        pass
                                            ######################################################
    def __repr__(self):                     # Adda pöntun fyrir ofan með smiðnum ( __init__ )
        pass                                # Hvernig eyðir maður eintaki af pöntun, customer etc?

    def get_order_num(self):
        return self.order_num
    
    def get_cust_email(self):
        return self.cust_email

    def get_datetime(self):
        return self.datetime

    def get_plate_number(self):
        return self.plate_number