from Class.Colors import *


def askPwdToCheck():
    return input(f"{bcolors.White}{'Enter the password to check: ': >41}")


def askFilePath():
    return input(f"{bcolors.White}{'Enter the file path: ': >41}")
