from Models.Salesman import Salesman
from Repository.Salesman_repo import Salesman_repo
import os

class Information_service(object):

    def __init__(self):
        self.salesman_repo = Salesman_repo()


    def get_salesman_dict(self):
        salesmen_dict = self.salesman_repo.get_salesmen()
        return salesmen_dict
        