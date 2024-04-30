###############################################################################
#                    免责声明：该程序仅个人学习使用，请勿用做其他用途                  #
###############################################################################
from apscheduler.schedulers.blocking import BlockingScheduler
from wxauto import *
import datetime


def send_msg_to_single_user(user, content):
    cur_time = datetime.datetime.now()
    # 当前时间
    cur_hour = cur_time.hour
    cur_hour_str = str(cur_hour).zfill(2) + ':00'
    # 计算2小时前的时间
    pre_timedelta = datetime.timedelta(hours=-2)
    pretime = cur_time + pre_timedelta
    start_hour = pretime.strftime("%#m月%d日") + str(pretime.hour).zfill(2) + ':00'
    if cur_hour == 1:
        # 如果跨天，也就是1点的消息，结束时间前面加上日期
        cur_hour_str = cur_time.strftime("%#m月%d日") + cur_hour_str
    msg = start_hour + '-' + cur_hour_str + ' ' + content
    # 向某人发送文件（以`文件传输助手`为例，发送三个不同类型文件）
    try:
        print(f"开始向单个用户`{user}`发送信息:{msg}")
        wx.ChatWith(user)  # 打开`文件传输助手`聊天窗口
        wx.SendMsg(msg)
        # wx.SendFiles(file)
        print("发送完毕")
    except Exception as e:
        print("发送失败，原因:", e)


# 获取当前微信客户端
wx = WeChat()
# 获取会话列表
wx.GetSessionList()
user = "文件传输助手"  # 适用于中文版微信
content = "豫正通系统运行正常。"
scheduler = BlockingScheduler()
# 于每天的19点-次日7点，每两小时0分20秒发送消息。
# scheduler.add_job(send_msg_to_single_user, 'cron', hours='1,3,5,7,19,21,23', second='20', args=[user])
scheduler.add_job(send_msg_to_single_user, 'cron', hour='14,15,16', second='0/10', args=[user, content])
scheduler.start()

###############################################################################
#                    免责声明：该程序仅个人学习使用，请勿用做其他用途                  #
###############################################################################
