#!/bin/sh
reset
echo 作者：独孤伶俜
echo 时间：2018.5.3
echo 最后修改时间：2018.5.14 16:30
echo 声明：本程序尊循GPL开源协议，意味着您可以自由的下载分发，但修改新增内容要遵循同样的协议，同时注明署名！
echo 声明2：本程序作者不对任何商业和非商业内容负责，请知晓！
echo 程序运行需网络通畅！
sleep 3s
echo
echo 程序会在2秒后运行
sleep 2s
/home/pi/git-code/naozhong/naoz/bin/python2 /home/pi/git-code/naozhong/wulala.py > /home/pi/git-code/naozhong/wulala.log
sleep 1s
echo 
echo mp3文件生成完毕，在目录/home/pi/git-code/naozhong/test_tmp.mp3
sleep 1s
echo 
cat /home/pi/git-code/naozhong/wulala.log
echo 
sleep 1s
echo 会在3秒后自动播放刚刚生成的mp3,叫醒你起床～～
sleep 3s
play /home/pi/git-code/naozhong/test_tmp.mp3
sleep 2s
echo 
echo 程序运行完毕！明天见哦～
echo 正在退出！