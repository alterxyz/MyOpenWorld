import datetime
import os
import re

# 手动参数
sleep_duration = datetime.timedelta(hours=7, minutes=40) # 睡眠时长
ideal_awake_time = datetime.timedelta(hours=7, minutes=40) # 理想起床时间
bed_to_sleep = datetime.timedelta(hours=1, minutes=40) # 暖床时间
now = datetime.datetime.now() # 当前时间


# 获取起床时间
def get_awake_time():
    with open(os.path.join(os.path.dirname(__file__), 'awake_time.txt'), 'r') as f:
        awake_time = f.read()
    try:
        awake_time = datetime.time(int(awake_time.split(':')[0]), int(awake_time.split(':')[1]))
    except:
        set_awake_time('请小于23:59\n')
        awake_time = get_awake_time()
    return awake_time

# 修改起床时间
def set_awake_time(ask):
    # 第一次问问
    input_time = input(ask)
    # 不对就循环问
    while not re.match(r'^\d{1,2}:\d{1,2}$', input_time):
        if input_time == '':
            exit()
        input_time = input('应该是xx:xx\n')
    # 对了就写入
    with open(os.path.join(os.path.dirname(__file__), 'awake_time.txt'), 'w') as f:
        f.write(input_time)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n修改成功')
    return True

# 计算和显示
def calculate_and_show():
    # 获取起床时间
    awake_time = get_awake_time()

    # 计算清醒时长
    awake_duration = now - datetime.datetime.combine(datetime.datetime.now().date(), awake_time)
    # 可能是负的，加上一天
    if awake_duration < datetime.timedelta(0):
        awake_duration += datetime.timedelta(days=1)
    # 显示
    print('已经清醒    {}小时{}分钟'.format(awake_duration.seconds // 3600, awake_duration.seconds % 3600 // 60))

    # 计算暖床. 24小时减去暖床时间减去睡眠时长减去清醒时长
    bed_time = datetime.timedelta(days=1) - bed_to_sleep - sleep_duration - awake_duration
    # 如果大于0且小于4小时，就显示暖床, 否则不显示
    if bed_time > datetime.timedelta(0) and bed_time < datetime.timedelta(hours=4):
        print('距离暖床    {}小时{}分钟'.format(bed_time.seconds // 3600, bed_time.seconds % 3600 // 60))
    
    # 正常时间
    should_time = datetime.timedelta(hours=24) - sleep_duration - bed_to_sleep
    # 显示
    if awake_duration > should_time:
        overed_time = awake_duration - should_time
        print('要知道自己在做什么哦, 已经超过了{}小时{}分钟'.format(overed_time.seconds // 3600, overed_time.seconds % 3600 // 60))


    # 计算参考时间
    ideal_time = awake_duration + ideal_awake_time
    # 显示
    print('\n\n\n参考时间    {:02d}:{:02d}\n\n\n\n\n'.format(ideal_time.seconds // 3600, ideal_time.seconds % 3600 // 60))
    set_awake_time('')

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

while True:
    calculate_and_show()
