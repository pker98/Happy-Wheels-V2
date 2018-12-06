from Controller.Main_controller import Main_controller
from Respository.Cars_repo import Cars_repo
from Controller.Rent_controller import Rent_controller

def main():
    test = Cars_repo()
    print(test.get_cars())

    test2 = Rent_controller()
    print(test2.Rent_page())
    """
    while True:
        test = Cars_repo()
        test.get_cars()
        #start_program = Main_controller()
        #start_program.Main_page()
"""
main()