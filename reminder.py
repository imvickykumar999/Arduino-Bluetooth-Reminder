
rem = input('\nEnter your remainder : ')
baddr = input('\nEnter device address : ')

resp = '\nYou have reached your location, you asked to remind : '
print('\nSearching for device ...')

channel = 4
# baddr = 'F8:70:9F:3A:19:24' # Airdopes 141
raddr = (baddr, channel)


def connect(raddr):
    import socket

    s = socket.socket(
        socket.AF_BLUETOOTH, 
        socket.SOCK_STREAM, 
        socket.BTPROTO_RFCOMM)
    
    s.connect(raddr)
    return s


while True:
    try:
        e = connect(raddr)
        # print(e)
        print(resp, f'"{rem}"')
        break

    except Exception as e:
        # print(e)
        pass

input('Press enter to exit.')
