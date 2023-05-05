
def connected_wifi():
    import subprocess
    wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
    data = wifi.decode('utf-8')
    print(data)

# connected_wifi()

'''
There is 1 interface on the system:

    Name                   : Wi-Fi
    Description            : Realtek 8822CE Wireless LAN 802.11ac PCI-E NIC
    GUID                   : 70673e8d-7ce9-4927-91b9-5fc3b44c492e
    Physical address       : 80:91:33:c8:ed:19
    Interface type         : Primary
    State                  : connected
    SSID                   : Vicky
    BSSID                  : e8:65:d4:1d:b2:d0
    Network type           : Infrastructure
    Radio type             : 802.11n
    Authentication         : WPA2-Personal
    Cipher                 : CCMP
    Connection mode        : Auto Connect
    Band                   : 2.4 GHz
    Channel                : 10
    Receive rate (Mbps)    : 300
    Transmit rate (Mbps)   : 300
    Signal                 : 100%
    Profile                : Vicky

    Hosted network status  : Not available
'''


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

'''
The MAC address in formatted way is : 80:91:33:c8:ed:18
'''


def connect(raddr):
    import socket
    
    channel = 4
    baddr = 'F8:70:9F:3A:19:24' # Airdopes
    raddr = (baddr, channel)

    s = socket.socket(socket.AF_BLUETOOTH, 
                      socket.SOCK_STREAM, 
                      socket.BTPROTO_RFCOMM
                      )

    s.connect(raddr)
    print(s)

# try:
#     connect(raddr)
#     print('YOUR REMAINDER')
# except Exception as e:
#     print(e)

'''
OUTPUT :

<socket.socket fd=304, 
family=AddressFamily.AF_BLUETOOTH, 
type=SocketKind.SOCK_STREAM, 
proto=3, 
laddr=('80:91:33:C8:ED:18', 0), 
raddr=('F8:70:9F:3A:19:24', 4)>
'''
