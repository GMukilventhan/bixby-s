
from Class.Bftp import *

ftpConnexion = Bftp("192.168.1.67", 21, "root", "root")
# ftpConnexion.open()

ftpConnexion.list()
#ftpConnexion.rename("1655917042.100679", "test")
#ftpConnexion.delete("history_2022-06-22.log")
#ftpConnexion.download("history.log")

# TO DO: Fix the bug with the upload function
# PROBLEM HERE: the file is not uploaded when outside the directory
# ftpConnexion.upload("/Users/smveer/Downloads/documentCirculationKhushvir-merged-compressed.pdf")
# But when it's in it works
#ftpConnexion.upload("history_2022-06-23.log")
