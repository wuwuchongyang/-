#!/bin/bash

# 测试脚本: 按键模拟和返回一张手机截图

# 测试连接
connect(){
    local Device=$(adb devices | awk 'BEGIN { FS="\t" } NR==2 {print $1}')
    if [[ "$Device" == "" ]]; then
        echo "检测到第一次连接"
        echo "请将手机用USB连上电脑,并开启开发者模式"
    fi
    echo -e '\e[5m验证连接中\e[0m'
    adb wait-for-device
    echo -e '\e[2J 连接成功'
    if [[ "${Device##*:}" != '5555' ]]; then
        read -t 5 -n 1 -p "是否开启wifi连接 [Y/N]?" answer
        case $answer in
        Y | y)
             wifi_connect;;
        *)
             ;;
        esac
    fi
}

wifi_connect(){
    adb tcpip 5555
    echo "请先断开usb连接"
    echo "请输入手机IP地址:"
    read phone_ip
    adb connect $phone_ip
    # 验证连接
    echo -e '\e[5m验证连接中\e[0m'
    adb wait-for-device
    local Device=$(adb devices | awk 'BEGIN { FS="\t" } NR==2 {print $1}')
    if [[ "${Device}" == "5555" ]]; then
        echo "连接成功"
    else
        echo "失败"
        adb kill-server
        exit 0
    fi
}

# 按键测试
touch_screen(){
    if [[ $# == 4 ]];then
       adb shell input swipe $1 $2 $3 $4
    else
       adb shell input tap $1 $2
    fi 
}
# 保存截图
save_screen(){
    adb shell screencap -p /sdcard/1.png
    adb pull /sdcard/1.png ../../tmp/img/${1:-'screen_cache'}.png
}
# 清理缓存
tmp_dump(){
    # 手机截图清理
    adb shell rm /sdcard/1.png
}
connect
touch_screen 23 489
save_screen
tmp_dump
