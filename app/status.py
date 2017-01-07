from dot3k.menu import MenuOption

import time
import socket
import fcntl
import struct

class Status(MenuOption):

    def __init__(self):
        MenuOption.__init__(self)

    def redraw(self, menu):
        menu.write_option(
                row=0,
                margin=1,
                icon="",
                text=time.strftime(' %a %H:%M:%S ')
                )
        menu.write_option(
                row=1,
                margin=1,
                icon="",
                text=self.get_ip_address()
                )
        menu.clear_row(2)

    def get_ip_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
        )[20:24])
