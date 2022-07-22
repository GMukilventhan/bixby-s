from Class.Colors import *


def ask_ip():
    ip = input(f"{bcolors.Black}{'Enter the ip: ': >41}")
    return ip


def ask_port():
    port = int(input(f"{bcolors.Black}{'Enter the port: ': >41}"))
    return port


def askRange():
    rangeStart = int(input(f"{bcolors.Black}{'Enter the starting range: ': >41}"))
    rangeEnd = int(input(f"{bcolors.Black}{'Enter the ending range: ': >41}"))
    return rangeStart, rangeEnd
