from Class.Bscan import *

scanner = Bscan("127.0.0.1")
#print(scanner.scan_all_ports())
print(scanner.scan_all_ports_thread())