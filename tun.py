from pytun import TunTapDevice

tun = TunTapDevice(name='mytun')
tun.addr = '192.168.137.1'
tun.dstaddr = '192.168.137.10'
tun.netmask = '255.255.255.255'
tun.mtu = 1500
tun.persist(True)
tun.up()
buf = tun.read(tun.mtu)
tun.write(buf)