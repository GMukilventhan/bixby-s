#!/usr/bin/python3
from ftpFunctions import *
from Class.Blogger import *

logger = Blogger()

try:
    checkFtp("10.33.1.203")
    logger.logSuccess("FTP OK")
except Exception as e:
    logger.logError(str(e))
