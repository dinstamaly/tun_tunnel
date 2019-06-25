from pytun import TunTapDevice

tun = TunTapDevice(name='mytun')
print(tun.name)
tun.addr = '192.168.137.1'
tun.dstaddr = '192.168.137.10'
tun.netmask = '255.255.255.255'
tun.mtu = 1500
tap.hwaddr = '\x00\x11\x22\x33\x44\x55'
print(tap.hwaddr)
tun.persists(True)
tun.up()
buf = tun.read(tun.mtu)
tun.write(buf)
tun.close()
