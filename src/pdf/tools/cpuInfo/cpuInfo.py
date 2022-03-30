# 获取CPU序列号
import wmi
c = wmi.WMI()
# CPU序列号
for index, cpu in enumerate(c.Win32_Processor()):
    print("CPU {0} 序列号：{1}".format(index, cpu.ProcessorId.strip()))