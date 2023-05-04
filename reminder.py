
channel = 4
baddr = 'F8:70:9F:3A:19:24'
raddr = (baddr, channel)


def connect(raddr):
    import socket

    s = socket.socket(
        socket.AF_BLUETOOTH, 
        socket.SOCK_STREAM, 
        socket.BTPROTO_RFCOMM)
    
    s.connect(raddr)
    return s


rem = input('Enter your remainder : ')

while True:
    try:
        e = connect(raddr)
        # print(e)
        print(rem)
        break

    except Exception as e:
        # print(e)
        print('Searching ...')
        pass
