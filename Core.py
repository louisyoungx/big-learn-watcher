import time

from BigLearnAPI import big_learn_api
from Log import log
from QQBotMessage import send_group_message, send_user_message
from Scheduler import time_in_work, min_sleep
from settings import WorkTimeStart


def cruise():
    now = time.localtime(time.time())
    start_hour = int(WorkTimeStart[:2])
    log.update("(Core): Daily Task Initialized Successfully")
    if now.tm_wday - 1 < 5: # 如果是工作日
        log.update("(Core): Working Day")
        if time_in_work(): # 执行当日任务时间
            working()
        elif now.tm_hour < start_hour: # 今日任务未开始
            log.update("(Core): Waiting to Start")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday, WorkTimeStart)
            min_sleep(now_str_time, end_time)
        else: # 今日任务已结束
            log.update("(Core): Today's Mission Completed")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+1, WorkTimeStart)
            min_sleep(now_str_time, end_time)
    else: # 周末
        log.update("(Core): Over The Weekend")
        if now.tm_wday == 5: # 周六
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+2, WorkTimeStart)
            min_sleep(now_str_time, end_time)
        if now.tm_wday == 6: # 周日
            log.update("(Core): Over The Weekend")
            now_str_time = "{}-{}-{} {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
            end_time = "{}-{}-{} {}".format(now.tm_year, now.tm_mon, now.tm_mday+1, WorkTimeStart)
            min_sleep(now_str_time, end_time)

def working():
    '''工作模式'''
    log.update("(Core): Trigger Working Mode")

    infoDict = big_learn_api() # 获取API数据
    DoMember = infoDict['DoMember']
    NotMember = infoDict['NotMember']
    AllNum = infoDict['AllNum']
    DoNum = infoDict['DoNum']
    DontNum = infoDict['DontNum']
    Time = infoDict['Time']

    DoStr = ""
    for Mem in DoMember:
        uid = "{}-{}".format(Mem['index'], Mem['name'])
        DoStr += uid + '\n'

    DontStr = ""
    for Mem in NotMember:
        uid = "{}-{}".format(Mem['index'], Mem['name'])
        DontStr += uid + '\n'

    MESSAGE = '180851班共{}人\n' \
              '已完成{}人，未完成{}人\n\n' \
              '未完成\n' \
              '{}\n' \
              '{}'.format(AllNum, DoNum, DontNum, Time, DontStr)
    # print(MESSAGE)

    send_group_message(MESSAGE) # 发送群消息
    send_user_message(MESSAGE, 1462648167) # 发送个人消息
    log.update("(Core): Waiting 5 Minutes")
    time.sleep(60 * 5)

def running():
    '''死循环执行'''
    while True:
        cruise()

if __name__ == '__main__':
    running()