import ftplib
from Class.Blogger import *


class Bftp:
    # Constructor that initialize the ftp connection
    def __init__(self, host, port, user, password):
        self.logger = Blogger()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.initialized = False
        try:
            self.ftp = ftplib.FTP(self.host, self.user, self.password)
            print(self.ftp.getwelcome() + "- Bienvenue sur l'outil Bftp")
            self.logger.logSuccess("FTP initialized")
            self.initialized = True
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us open the ftp connection
    def open(self):
        try:
            self.ftp.connect(self.host, self.port)
            self.logger.logSuccess("Opened connection")
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us rename a file on the ftp server
    def rename(self, file, newName):
        try:
            self.ftp.rename(file, newName)
            self.logger.logSuccess("Renamed " + file + " to " + newName)
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us delete a file from the ftp server
    def delete(self, file):
        try:
            self.ftp.delete(file)
            self.logger.logSuccess("Deleted " + file)
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us upload a file to the ftp server
    def upload(self, file):
        try:
            self.ftp.storbinary('STOR ' + file, open(file, 'rb'))
            self.logger.logSuccess("Uploaded " + file)
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us download a file from the ftp server
    def download(self, file):

        try:
            self.ftp.retrbinary('RETR ' + file, open(file, 'wb').write)
            self.logger.logSuccess("Downloaded " + file)
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us create a directory on the ftp server
    def createDirectory(self, directory):
        try:
            self.ftp.mkd(directory)
            self.logger.logSuccess("Created directory " + directory)
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us delete a directory on the ftp server
    def deleteDirectory(self, directory):
        try:
            self.ftp.rmd(directory)
            self.logger.logSuccess("Deleted directory " + directory)
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us change the current directory on the ftp server
    def changeDirectory(self, directory):
        try:
            self.ftp.cwd(directory)
            self.logger.logSuccess("Changed directory to " + directory)
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us rename a file on the ftp server
    def rename(self, file, newName):
        try:
            self.ftp.rename(file, newName)
            self.logger.logSuccess("Renamed " + file + " to " + newName)
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us delete a file from the ftp server
    def delete(self, file):
        try:
            self.ftp.delete(file)
            self.logger.logSuccess("Deleted " + file)
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us close the ftp connection
    def close(self):
        try:
            self.ftp.quit()
            self.logger.logSuccess("Closed connection")
        except ftplib.all_errors as e:
            self.logger.logError(str(e))

    # Function that let us get the current directory on the ftp server
    def list(self):
        dirlisting = []
        files = []
        self.ftp.retrlines('LIST', callback=dirlisting.append)
        current_dir = self.ftp.pwd()
        for l in dirlisting:
            lastspace = l.rindex(' ')
            file_name = l[lastspace + 1:]

            if l[0] == '-':
                if current_dir == '/':
                    files.append(current_dir + file_name)
                else:
                    files.append(current_dir + "/" + file_name)
        for l in dirlisting:
            lastspace = l.rindex(' ')
            file_name = l[lastspace + 1:]
            if l[0] == 'd' and file_name != '.' and file_name != '..':
                self.ftp.cwd(file_name)
                self.list()
        print("Dossier: ---- " + self.ftp.pwd() + " ----")
        for f in files:
            print("         File: ---- " + f)
        if current_dir != '/':
            self.ftp.cwd('..')

    def get_files_directories(self):
        dirlisting = []
        self.ftp.retrlines('LIST', callback=dirlisting.append)
        files = []
        directories = []
        for l in dirlisting:
            lastspace = l.rindex(' ')
            file_name = l[lastspace + 1:]
            if l[0] == 'd' and file_name != '.' and file_name != '..':
                directories.append(file_name)
            elif l[0] == '-':
                files.append(file_name)
        return files, directories
