from datetime import datetime


class Blogger:
    # Constructeur
    def __init__(self):
        # Create file name depending on date
        self.fileName = 'history_' + str(datetime.now().strftime("%Y-%m-%d")) + '.log'
        print("Logger initialized")

    # Function that update the file name
    def updateFileName(self):
        self.fileName = 'history_' + str(datetime.now().strftime("%Y-%m-%d")) + '.log'

    # Function that log a success message
    def logSuccess(self, message):
        self.updateFileName()
        toWrite = str(datetime.now().strftime("%H:%M:%S")) + " -- INFO -- " + message + "\n"
        # Open file
        with open(self.fileName, 'a') as f:
            f.write(toWrite)
            print(toWrite)
            # Close file
            f.close()

    # Function that log a warning message
    def logWarning(self, message):
        self.updateFileName()
        toWrite = str(datetime.now().strftime("%H:%M:%S")) + " -- WARNING -- " + message + "\n"
        # Open file
        with open(self.fileName, 'a') as f:
            f.write(toWrite)
            print(toWrite)
            # Close file
            f.close()

    # Function that log an error message
    def logError(self, message):
        self.updateFileName()
        toWrite = str(datetime.now().strftime("%H:%M:%S")) + " -- ERROR -- " + message + "\n"
        # Open file
        with open(self.fileName, 'a') as f:
            f.write(toWrite)
            print(toWrite)
            # Close file
            f.close()
