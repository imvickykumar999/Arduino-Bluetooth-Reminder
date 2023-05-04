
channel = 4
baddr = 'F8:70:9F:3A:19:24' # Airdopes
raddr = (baddr, channel)


def discover():
    # pip install pybluez
    import bluetooth

    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print(f"Found {len(nearby_devices)} devices.")

    for addr, name in nearby_devices:
        print(f"  {addr} - {name}")


# discover()

'''
import bluetooth  # from pip install pybluez
ModuleNotFoundError: No module named 'bluetooth'
'''


def mac_address():
    # Python 3 code to print MAC
    # in formatted way.

    import uuid

    # joins elements of getnode() after each 2 digits.

    print ("The MAC address in formatted way is : ", end="")
    print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))

# mac_address()


def connect(raddr):
    import socket

    s = socket.socket(socket.AF_BLUETOOTH, 
                      socket.SOCK_STREAM, 
                      socket.BTPROTO_RFCOMM
                      )

    s.connect(raddr)
    print(s)


try:
    connect(raddr)
    print('YOUR REMAINDER')
except Exception as e:
    print(e)

'''
OUTPUT :

<socket.socket fd=304, 
family=AddressFamily.AF_BLUETOOTH, 
type=SocketKind.SOCK_STREAM, 
proto=3, 
laddr=('80:91:33:C8:ED:18', 0), 
raddr=('F8:70:9F:3A:19:24', 4)>
'''
