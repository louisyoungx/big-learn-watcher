import json

import requests


def send_group_message(message, groupid):
    if True:
        URL = "http://www.louisyoung.site:8088/v1/LuaApiCaller"
        params = {
            'qq': 2782594859,  #bot的QQ
            'funcname':'SendMsgV2', #调用方法类型
            }

        body = {
            "ToUserUid": groupid,
            "SendToType": 2,
            "SendMsgType": "TextMsg",
            "Content": message
        }

        # body = {
        #     "toUser":groupid,  #发到哪个QQ或者群号
        #     "sendToType":1,   #自己选择对应会话的数值
        #     "sendMsgType":"TextMsg",
        #     "content":message,   #要发送的文字内容
        #     "groupid":groupid,  #群号
        # }

        r = requests.post(URL, params = params, data=json.dumps(body))
        print("（Group Message）：{}".format(message.replace("\n", " ")))
        print(r.text)
        return True



infoDict = {'DoMember': [{'index': '18085127', 'name': '王保国'}, {'index': '17111407', 'name': '周星帆'}, {'index': '18085104', 'name': '刘倩雯'}, {'index': '18085104', 'name': '刘倩雯'}, {'index': '18085114', 'name': '许宇'}], 'NotMember': [{'index': '18085101', 'name': '罗德洁'}, {'index': '18085102', 'name': '盛智洋'}, {'index': '18085103', 'name': '梁飘飘'}, {'index': '18085106', 'name': '朱燕'}, {'index': '18085107', 'name': '黎璟乐'}, {'index': '18085108', 'name': '陈俊炜'}, {'index': '18085109', 'name': '丁小聪'}, {'index': '18085110', 'name': '谢青松'}, {'index': '18085112', 'name': '邓祯卓'}, {'index': '18085116', 'name': '黄宇坤'}, {'index': '18085117', 'name': '刘冬虎'}, {'index': '18085119', 'name': '沈永汪'}, {'index': '18085120', 'name': '万义理'}, {'index': '18085121', 'name': '徐心良'}, {'index': '18085122', 'name': '杨熙'}, {'index': '18085123', 'name': '张志林'}, {'index': '18085124', 'name': '张忠姚'}, {'index': '18085125', 'name': '周涛'}, {'index': '18085126', 'name': '李澳'}, {'index': '18085128', 'name': '冯卓'}, {'index': '18085129', 'name': '董一洲'}, {'index': '18085130', 'name': '赵读惟'}, {'index': '18085132', 'name': '刘洋兴'}, {'index': '17085127', 'name': '肖力华'}, {'index': '17085105', 'name': '朱聪聪'}, {'index': '17085110', 'name': '苏东岳'}, {'index': '17085117', 'name': '王志文'}], 'AllNum': 31, 'DoNum': 5, 'DontNum': 27, 'Time': '2021-03-17'}

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

MESSAGE = '''180851班共{}人
已完成{}人，未完成{}人\n
已完成
{}
{}
未完成
{}
{}'''.format(AllNum, DoNum, DontNum, Time, DoStr, Time, DontStr)
print(MESSAGE)


send_group_message('今天还是没用', 791031608)