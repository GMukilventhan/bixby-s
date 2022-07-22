import socket

server = "127.0.0.1"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# méthode scanport: fonction
def scanport(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False
    s.close()


# scan tous les ports
for port in range(1, 65536):
    if scanport(port):
        print("port", port, "est ouvert")
    else:
        print("port", port, "est fermer")

# scan range

port_range1 = input("Enter range port: ")
port_range2 = input("Enter range port: ")
print("Scan port range" + str(port_range1) + "to" + str(port_range2))
for port in range(int(port_range1), int(port_range2)):
    if scanport(port):
        print("port", port, "est ouvert")
    else:
        print("port", port, "est fermer")


# scan 1 port souhaité
port_souhaite = input("Enter le port que vous voulez scanner: ")
print("Scan" + str(port_souhaite))
for port in range(int(port_souhaite)):
    if scanport(port_souhaite):
        print("port", port_souhaite, "est ouvert")
    else:
        print("port", port_souhaite, "est fermer")
