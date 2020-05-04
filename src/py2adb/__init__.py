import py2adb.connect
import os

# init
class Phone():
    def __init__(self):
        self.addr=connect.establish()
    def touch(self,li):
        # 数据检查
        ## 这部分取得及其丑陋 但是python没有好的类型检查机制 出此下策
        assert(type(li)==type([]))
        assert(len(li)==2)
        assert(len(list(filter(lambda x: type(x)==type(1), li)))==2)
        os.system("adb shell input tap %d %d"%tuple(li))
    def wipe(self,li):
        # 数据检查
        assert(type(li)==type([]))
        assert(len(li)==4)
        assert(len(list(filter(lambda x: type(x)==type(1), li)))==4)
        os.system("adb shell input swipe %d %d %d %d"%tuple(li))
    def screen(self, fileName='screen_cache'):
        # 手机截图
        os.system("adb shell screencap -p /sdcard/1.png")
        # 移动到电脑
        os.system("adb pull /sdcard/1.png "+"../tmp/img/"+fileName+".png")
    def __del__(self):
        # 清理缓存
        os.popen("adb shell rm /sdcard/1.png").read()

if __name__=="__main__":
    phone=Phone()
    phone.touch([100,1000])
    phone.wipe([0,0,100,500])
    phone.screen()
    del phone
