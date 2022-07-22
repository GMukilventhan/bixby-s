from Class.Colors import *
from Functions.menuCreation import *
from Class.Bftp import *
import sys

from Functions.ftp import *

sys.path.append("../../BixbyPY")


while True:
    textList = [
        "Choose your role",
        "1) User",
        "2) Admin"
                ]
    header(bcolors.Cyan, bcolors.Purple, textList)
    while True:
        loginChoice = int(input(f"{'Enter the number: ': >41}"))
        if loginChoice == 1:
            break
        elif loginChoice == 2:
            break
        elif loginChoice == 0:
            break
        else:
            continue
    footer(bcolors.Cyan)

    if loginChoice == 0:
        msg_center("", bcolors.Black, bcolors.White)
        msg_center("Goodbye", bcolors.Black, bcolors.White)
        msg_center("", bcolors.Black, bcolors.White)
        break
    else:
        while True:

            textList = [
                "Choose an option:",
                "1) FTP",
                "2) Backup"
                        ]
            if loginChoice == 2:
                textList.append("3) Boîte à outils")

            header(bcolors.pink, bcolors.Blue, textList)

            while True:
                toolChoice = int(input(f"{bcolors.BYellow}{'Enter a number: ': >41}"))
                if toolChoice == 1:
                    break
                elif toolChoice == 2:
                    break
                elif loginChoice == 2 and toolChoice == 3:
                    break
                elif toolChoice == 0:
                    break
                else:
                    continue
            footer(bcolors.pink)

            # Exit
            if toolChoice == 0:
                break
            # FTP
            elif toolChoice == 1:

                ftpConnexion = askConnexion()

                if not ftpConnexion.initialized:
                    continue
                else:
                    textList = [
                        "FTP - Choose a option:",
                        "1) Upload",
                        "2) Download",
                        "3) Afficher les fichiers",
                        "4) Créer un répertoire",
                        "5) Change working directory"
                                ]
                    if loginChoice == 2:
                        textList.append("6) Renommer un fichier")
                        textList.append("7) Supprimer un fichier")
                        textList.append("8) Supprimer un répertoire")

                    while True:

                        header(bcolors.Blue, bcolors.Yellow, textList)
                        toolChoice = int(input(f"{bcolors.Green}{'Enter a number: ': >41}"))

                        if toolChoice == 1:
                            askUpload(ftpConnexion)
                            continue
                        elif toolChoice == 2:
                            askDownload(ftpConnexion)
                            continue
                        elif toolChoice == 3:
                            askList(ftpConnexion)
                            continue
                        elif toolChoice == 4:
                            askCreateDirectory(ftpConnexion)
                            continue
                        elif toolChoice == 5:
                            askChangeDirectory(ftpConnexion)
                            continue
                        elif loginChoice == 2 and toolChoice == 6:
                            askRename(ftpConnexion)
                            continue
                        elif loginChoice == 2 and toolChoice == 7:
                            askDeleteFile(ftpConnexion)
                            continue
                        elif loginChoice == 2 and toolChoice == 8:
                            askDeleteDirectory(ftpConnexion)
                            continue
                        elif toolChoice == 0:
                            ftpConnexion.close()
                            break
                        else:
                            continue
                    footer(bcolors.Blue)
            # Backup
            elif toolChoice == 2:
                textList = [
                    "Backup - Choose a option",
                    "1) Consulter",
                    "2) Backup",
                            ]
                header(bcolors.Black, bcolors.Yellow, textList)

                while True:
                    toolChoice = int(input(f"{bcolors.Green}{'Enter a number: ': >41}"))
                    if toolChoice == 1:
                        break
                    elif toolChoice == 2:
                        break
                    elif toolChoice == 0:
                        ftpConnexion.close()
                        break
                    else:
                        continue

                footer(bcolors.Black)

            elif loginChoice == 2 and toolChoice == 3:

                textList = ["Boite de outils - Choose a option", "1) Scan Port", "2) Brute Force", "3) Fichiers logs"]

                header(bcolors.White, bcolors.Green, textList)

                while True:
                    toolChoice = int(input(f"{bcolors.Black}{'Enter a number: ': >41}"))
                    if toolChoice == 1:
                        break
                    elif toolChoice == 2:
                        break
                    elif toolChoice == 3:
                        break
                    elif toolChoice == 0:
                        break
                    else:
                        continue
                footer(bcolors.White)

                if toolChoice == 0:
                    break

                elif toolChoice == 1:
                    textList = ["Scan Port - Choose a option", "1) Scan 1 Port", "2) Scan tous les ports", "3) Scan par scope"]
                    header(bcolors.White, bcolors.Green, textList)
                    while True:
                        toolChoice = int(input(f"{bcolors.Black}{'Enter a number: ': >41}"))
                        if toolChoice == 1:
                            break
                        elif toolChoice == 2:
                            break
                        elif toolChoice == 3:
                            break
                        elif toolChoice == 0:
                            break
                        else:
                            continue
                    footer(bcolors.White)
                
                elif toolChoice == 2:
                    textList = ["Force Brute - Choose a option", "1) Combinaison", "2) Dictionnaire"]
                    header(bcolors.White, bcolors.Green, textList)
                    while True:
                        toolChoice = int(input(f"{bcolors.Black}{'Enter a number: ': >41}"))
                        if toolChoice == 1:
                            break
                        elif toolChoice == 2:
                            break
                        elif toolChoice == 0:
                            break
                        else:
                            continue
                    footer(bcolors.White)
                
                elif toolChoice == 3:
                    textList = ["Fichier Log - Choose a option", "1) Consulter"]
                    header(bcolors.White, bcolors.Green, textList)
                    while True:
                        toolChoice = int(input(f"{bcolors.Black}{'Enter a number: ': >41}"))
                        if toolChoice == 1:
                            break
                        elif toolChoice == 0:
                            break
                        else:
                            continue
                    footer(bcolors.White)
