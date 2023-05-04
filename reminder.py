
# pip install pybluez
baddr = 'F8:70:9F:3A:19:24'

def discover():
    import bluetooth  # from pip install pybluez

    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print(f"Found {len(nearby_devices)} devices.")

    for addr, name in nearby_devices:
        print(f"  {addr} - {name}")


def connect(baddr):
    import socket

    # baddr = 'F8:70:9F:3A:19:24'
    channel = 4

    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect((baddr,channel))

    print(s)

    # s_sock = server_sock.accept()
    # print ("Accepted connection from " + address)

    # data = s_sock.recv(1024)
    # print ("received [%s]" % data)

    # s.listen(1)


connect(baddr)

'''
OUTPUT :

<socket.socket fd=304, 
family=AddressFamily.AF_BLUETOOTH, 
type=SocketKind.SOCK_STREAM, 
proto=3, 
laddr=('80:91:33:C8:ED:18', 0), 
raddr=('F8:70:9F:3A:19:24', 4)>
'''

# discover()

'''
import bluetooth  # from pip install pybluez
ModuleNotFoundError: No module named 'bluetooth'
'''

# (work on progress ...)
# error 404, progress not found :P
