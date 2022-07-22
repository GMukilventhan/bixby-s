from datetime import *
import os
from ftplib import *
import string

from Bftp import *


class Bbackup:
    def __init__(self, ftp):
        self.ftp = ftp
        self.local_dir = os.getcwd()
        self.remote_dir = "/"

    def get_local_dir(self):
        print(self.local_dir)

    def backup_directory(self):
        os.chdir(self.local_dir)
        datestring = str(date.today())
        datestring += "_" + str(datetime.now())
        print(datestring)
        str_date_backup = str(datestring).replace('-', '_')
        str_date_backup = str(str_date_backup).replace(':', '_')
        os.mkdir(str_date_backup)
        self.local_dir = self.local_dir + "/" + str_date_backup
        os.chdir(str_date_backup)
        try:
            self.ftp.cwd(self.remote_dir)

            files, directories = self.ftp.get_files_directories()

            for f in files:
                # Log the file name
                self.ftp.logger.logInfo("Backing up file: " + f)
                try:
                    self.ftp.retrbinary('RETR ' + f, open(f, 'wb').write)
                except error_perm:
                    self.ftp.logger.logError('Skipping ' + f + ' due to permissions')

            for d in directories:
                newremote = self.remote_dir + d + '/'
                newlocal = self.local_dir + '/' + d
                os.mkdir(newlocal)
                self.backup_directory(newlocal, newremote)
        except:
            self.ftp.logger.logError('Skipping ' + self.remote_dir + ' due to permissions!!!!!')


