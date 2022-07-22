from Class.Colors import *
from Class.Bftp import *
from Functions.menuCreation import *


def askConnexion():
    textList = ["Enter credentials for ftp:"]
    header(bcolors.pink, bcolors.Blue, textList)
    host = input(f"{bcolors.Green}{'Enter the host: ': >41}")
    port = int(input(f"{bcolors.Green}{'Enter the port: ': >41}"))
    username = input(f"{bcolors.Green}{'Enter the username: ': >41}")
    password = input(f"{bcolors.Green}{'Enter the password: ': >41}")
    return Bftp(host, port, username, password)


def askUpload(connexion):
    filePath = input(f"{bcolors.Green}{'Enter the path to upload: ': >41}")
    connexion.upload(filePath)


def askDownload(connexion):
    filePath = input(f"{bcolors.Green}{'Enter the path to download: ': >41}")
    connexion.download(filePath)


def askList(connexion):
    connexion.list()


def askCreateDirectory(connexion):
    directoryName = input(f"{bcolors.Green}{'Enter the name of the directory: ': >41}")
    connexion.createDirectory(directoryName)


def askChangeDirectory(connexion):
    path = input(f"{bcolors.Green}{'Enter the path to change the working directory: ': >41}")
    connexion.changeDirectory(path)


def askRename(connexion):
    filePath = input(f"{bcolors.Green}{'Enter the path of the file ': >41}")
    newFileName = input(f"{bcolors.Green}{'Enter the NEW name of the file: ': >41}")
    connexion.rename(filePath, newFileName)


def askDeleteFile(connexion):
    filePath = input(f"{bcolors.Green}{'Enter the path of the file to delete: ': >41}")
    connexion.delete(filePath)


def askDeleteDirectory(connexion):
    directoryName = input(f"{bcolors.Green}{'Enter the path of the directory to delete: ': >41}")
    connexion.deleteDirectory(directoryName)