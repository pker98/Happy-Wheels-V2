import datetime
class Log_repo:
    def __init__(self):
        pass

    def Update_repo(self, description):
        with open("./data/LOG.csv", "+a") as Log_file:
            today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Log_file.write("{}, Date: {}\n".format(description, today))

        
