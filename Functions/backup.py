from Bbackup import *
from Functions.ftp import *


def askBackup():
    ftp = askConnexion()
    #local = input(f"{bcolors.Green}{'Enter the local path where to download: ': >41}")
    return Bbackup(ftp)
