# 获取CPU序列号
import wmi

def getPCInfo():
    c = wmi.WMI()
    mainboard=c.Win32_BaseBoard()[0].SerialNumber.strip()   #获取主板序列号
    #BSN12345678901234567

    cpu=c.Win32_Processor()[0].ProcessorId.strip()  #获取cpu序列号
    #BFEBFBFF000306A9

    disk=c.Win32_DiskDrive()[0].SerialNumber.strip()  #硬盘序列号
    #S2Y4J9ADA29166

    ram=c.Win32_PhysicalMemory()[0].SerialNumber.strip()  #内存序列号
    #E3806262

    #网卡mac地址：
    def macAddress():#获取网卡mac信息函数
        macs = []
        for n in  c.Win32_NetworkAdapter():
            mactmp = n.MACAddress
            if mactmp and len(mactmp.strip()) > 5:
                tmpmsg = {}
                tmpmsg['MACAddress'] = n.MACAddress
                tmpmsg['Name'] = n.Name
                tmpmsg['DeviceID'] = n.DeviceID
                tmpmsg['AdapterType'] = n.AdapterType
                tmpmsg['Speed'] = n.Speed
                macs.append(tmpmsg)
        return [macs[0]['MACAddress'], macs]  #返回第一个网卡的mac地址【24:FD:52:3C:ED:8F】。macs包含所有网卡信息

    [mac, macs]=macAddress()
    print('cpu:', cpu)
    print('主板：', mainboard)
    print('disk:', disk)
    print('ram:', ram)
    print('mac:', mac)
    print('macs:', macs)

if __name__ == '__main__':
    getPCInfo()

