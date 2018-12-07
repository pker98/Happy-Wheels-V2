
class Salesman(object):
    def __init__(self, name, email, ID, password):
        self.ID = ID
        self.password = password
        self.name = name
        self.email = email

    # def __str__(self):
    #     return "{},{},{}".format(self.name, self.email, self.ID)
    
    def __repr__(self):
        return repr([self.name,self.email,self.password])

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_ID(self):
        return self.ID
    
    def get_password(self):
        return self.password