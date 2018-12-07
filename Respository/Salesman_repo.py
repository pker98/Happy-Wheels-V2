from Models.Salesman import Salesman
import csv

class Salesman_repo(object):
    def __init__(self):
        pass
    
    def get_salesmen(self):
        with open("./data/Salesman.csv", "r") as Salesman_file:
            csv_reader = csv.reader(Salesman_file)
            next(csv_reader)
            self.salesman_dict = {}
            for line in csv_reader:
                name, email, ID, pw = line
                new_salesman = Salesman(name, email, ID, pw)
                key = new_salesman.get_ID() 
            
                self.salesman_dict[key] = new_salesman

        return self.salesman_dict


