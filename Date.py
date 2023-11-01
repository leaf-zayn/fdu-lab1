import datetime

from datetime import datetime
# 获取当前时间
def getCurrentTime():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d %H:%M:%S")
    return formatted_time
#计算两者的时间差
def timeDiff(time1_str,time2_str):
    time_format = "%Y%m%d %H:%M:%S"
    time1 = datetime.strptime(time1_str,time_format)
    time2 = datetime.strptime(time2_str,time_format)
    time_diff=time2-time1
    total_seconds = time_diff.total_seconds()
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{int(hours)} 小时 {int(minutes)} 分钟"

#测试
print(timeDiff('20231030 13:42:02','20231030 15:45:02'))
