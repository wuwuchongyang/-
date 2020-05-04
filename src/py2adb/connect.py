#from package import *
import re
import os
import yaml

def establish():
    data=read_config_file()
    print("等待连接中...(请确保手机设置正确)")
    if data['type'] == 'ip':
        for i in range(5):
            os.system("adb connect "+data['addr'])
            try:
                get_addr()
            except DeviceError:
                print("请先连接手机...")
                os.system("adb wait-for-device")
                os.system("adb kill-server")
                os.system("adb tcpip 5555")
            else:
                return get_addr
        raise DeviceError("尝试失败")
    if data['type'] == 'usb':
        os.system("adb wait-for-device")
        return get_addr()
def get_addr():
    device=os.popen("adb devices").read().split('\n')[1].split('\t')[0]
    print(device)
    if re.match(r'(\d+\.){3}\d+:\d+',device):
        return { 'type':'ip', 'addr':device }
    if re.match(r'\w+', device):
        return { 'type':'usb', 'addr':device }
    raise DeviceError("获取状态失败")
def read_config_file():
    with open(r'./config.yaml', 'r') as f:
        data=yaml.load(f)
    return data

class DeviceError(ValueError):
    pass
