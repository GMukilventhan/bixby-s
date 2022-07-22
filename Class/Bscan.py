import socket
import threading
from time import time, sleep
from Class.Blogger import *


class Bscan:
    def __init__(self, ip):
        self.logger = Blogger()
        self.bscan = None
        self.ip = ip

    # Function that scan all ports of a host and return a list of open ports
    def scan_all_ports(self):
        self.logger.logWarning(
            "Scanning all ports of " +
            self.ip +
            " with scan_all_ports"
        )
        # get the start time
        st = time()
        self.bscan = []
        for port in range(1, 65536):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.ip, port))
                self.logger.logSuccess("Port " + str(port) + " is scanned with scan_all_ports and is open")
                # print("Port " + str(port) + " is scanned with scan_all_ports and is open")
                self.bscan.append(port)
                s.close()
            except:
                pass
        # get the end time
        et = time()
        # get the execution time
        elapsed_time = et - st
        print('scan_port: ', elapsed_time, 'seconds\n')
        return self.bscan

    # Function that scan a range of ports and return a list of open ports
    def scan_range_ports(self, port_range1, port_range2):
        self.logger.logWarning(
            "Scanning ports from " +
            str(port_range1) +
            " to " +
            str(port_range2) +
            " of " +
            self.ip +
            " with scan_range_ports"
        )
        self.bscan = []
        for port in range(int(port_range1), int(port_range2)):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.ip, port))
                self.logger.logSuccess("Port " + str(port) + " is scanned with scan_range_ports and is open")
                # print("Port " + str(port) + " is scanned with scan_range_ports and is open")
                self.bscan.append(port)
                s.close()
            except:
                # self.logger.logError("Port " + str(port) + " is scanned with scan_range_ports and is closed")
                pass
        return self.bscan

    # Function that scan a port and return a list of open ports
    def scan_port(self, port_souhaite):
        self.logger.logWarning(
            "Scanning port " +
            str(port_souhaite) +
            " of " +
            self.ip +
            " with scan_port"
        )
        self.bscan = []
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, port_souhaite))
            self.logger.logSuccess("Port " + str(port_souhaite) + " is scanned with scan_port and is open")
            # print("Port " + str(port_souhaite) + " is scanned with scan_port and is open")
            self.bscan.append(port_souhaite)
            s.close()
        except:
            self.logger.logError("Port " + str(port_souhaite) + " is scanned with scan_port and is closed")
            pass
        return self.bscan

    # Function that scan a port and return a list of open ports
    def scan_port_for_threads(self, port_souhaite):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, port_souhaite))
            self.logger.logSuccess("Port " + str(port_souhaite) + " is scanned with scan_port_for_threads and is open")
            # print("Port " + str(port_souhaite) + " is scanned with scan_port_for_threads and is open")
            self.bscan.append(port_souhaite)
            s.close()
        except:
            pass
        return self.bscan

    # Function that scan all ports using threads
    def scan_all_ports_thread(self):
        self.logger.logWarning(
            "Scanning all ports of " +
            self.ip +
            " with scan_all_ports_thread"
        )
        # get the start time
        st = time()
        self.bscan = []
        # Create a list of threads
        threads = []
        # Open sockets in threads and add them to the list
        for port in range(1, 65536):
            t = threading.Thread(target=self.scan_port_for_threads, args=(port,))
            threads.append(t)
        # Start all threads
        for t in threads:
            #print(t)
            t.start()
            sleep(0.001)
        # Wait for all threads to finish
        for t in threads:
            t.join()
        # get the end time
        et = time()
        # get the execution time
        elapsed_time = et - st
        print('scan_all_ports_thread: ', elapsed_time, 'seconds\n')
        return self.bscan
