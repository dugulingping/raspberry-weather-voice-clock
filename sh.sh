#!/bin/sh
reset
echo 作者：独孤伶俜
echo 时间：2018.5.3
echo 最后修改时间：2018.5.23 11:30
echo 声明：本程序尊循GPL开源协议，意味着您可以自由的下载分发，但修改新增内容要遵循同样的协议，同时注明署名！
echo 声明2：本程序作者不对任何商业和非商业内容负责，请知晓！
echo 程序运行需网络通畅！

echo
echo 程序会在2秒后运行
cd ~/git-code/raspberry-clock/
echo 1
/home/pi/git-code/raspberry-clock/naoz/bin/python36 /home/pi/git-code/raspberry-clock/1.py
echo 2
/home/pi/git-code/raspberry-clock/naoz/bin/python36 /home/pi/git-code/raspberry-clock/2.py > /home/pi/git-code/raspberry-clock/wulala.log
echo 3
/home/pi/git-code/raspberry-clock/naoz/bin/python36 /home/pi/git-code/raspberry-clock/wulala.py

echo 
echo mp3文件生成完毕，在目录/home/pi/git-code/raspberry-clock/test_tmp.mp3

echo 
echo 会在3秒后自动播放刚刚生成的mp3,叫醒你起床～～

play /home/pi/git-code/raspberry-clock/test_tmp.mp3
echo rm test_tmp.mp3
echo 
echo 程序运行完毕！明天见哦～
echo 正在退出！
