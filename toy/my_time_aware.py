"""
根据起床时间计算个人的相对时间, 帮助理解自身的作息.

使用方法:
    通过命令行运行本脚本，根据提示输入起床时间或直接查看当前设定的作息时间信息。
"""
import datetime
import os
import re

# 手动参数
sleep_duration = datetime.timedelta(hours=7, minutes=40)  # 睡眠时长
ideal_awake_time = datetime.timedelta(hours=7, minutes=40)  # 理想起床时间
bed_to_sleep = datetime.timedelta(hours=1, minutes=40)  # 睡前准备时间
now = datetime.datetime.now()  # 当前时间


def get_awake_time():
    """从文件中获取起床时间。

    Returns:
        datetime.time: 起床时间作为 datetime.time 对象返回。

    Raises:
        ValueError: 如果文件中的时间格式不正确。
    """
    with open(os.path.join(
            os.path.dirname(__file__), 'awake_time.txt'), 'r', encoding='utf-8') as f:
        awake_time = f.read()
    try:
        awake_time = datetime.time(
            int(awake_time.split(':')[0]), int(awake_time.split(':')[1]))
    except ValueError:
        set_awake_time('请小于23:59\n')
        awake_time = get_awake_time()
    return awake_time


def set_awake_time(ask):
    """
    设置并保存起床时间到文件。

    Args:
        ask (str): 提示用户输入的文本
    """

    input_time = input(ask)  # 第一次问问

    while not re.match(r'^\d{1,2}:\d{1,2}$', input_time):  # 不对就循环问
        if input_time == '':
            exit()
        input_time = input('应该是xx:xx\n')

    with open(os.path.join(
            os.path.dirname(__file__), 'awake_time.txt'), 'w', encoding='utf-8') as f:  # 对了就写入
        f.write(input_time)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n修改成功')
    return True

# 计算和显示


def calculate_and_show():
    """
    计算并显示相关时间信息，包括起床时间、已清醒时间、距离睡前准备时间和超出正常清醒时间。

    Returns:
        None
    """

    awake_time = get_awake_time()  # 获取起床时间

    awake_duration = now - \
        datetime.datetime.combine(
            datetime.datetime.now().date(), awake_time)  # 计算清醒时长

    if awake_duration < datetime.timedelta(0):
        awake_duration += datetime.timedelta(days=1)  # 可能是负的，加上一天

    print(f'起床时间    {awake_time.hour:02d}:{awake_time.minute:02d}')
    # 显示
    print(
        f'已经清醒    {awake_duration.seconds // 3600:02d}小时{awake_duration.seconds % 3600 // 60}分钟')

    # 计算睡前准备. 24小时减去睡前准备时间减去睡眠时长减去清醒时长
    bed_time = datetime.timedelta(
        days=1) - bed_to_sleep - sleep_duration - awake_duration

    # 如果大于0且小于4小时，就显示睡前准备, 否则不显示
    if bed_time > datetime.timedelta(0) and bed_time < datetime.timedelta(hours=4):
        print(
            f'距离洗漱    {bed_time.seconds // 3600}小时{bed_time.seconds % 3600 // 60}分钟')

    # 正常时间
    should_time = datetime.timedelta(hours=24) - sleep_duration - bed_to_sleep

    # 显示
    if awake_duration > should_time:
        overed_time = awake_duration - should_time
        print(
            f'要知道自己在做什么哦, 已经超过了{overed_time.seconds // 3600}小时{overed_time.seconds % 3600 // 60}分钟')
    # 计算参考时间
    ideal_time = awake_duration + ideal_awake_time
    # 计算小时和分钟
    i_hours = ideal_time.seconds // 3600
    i_minutes = ideal_time.seconds % 3600 // 60
    # 使用格式化字符串清晰打印("line too long"修复)
    print(f"\n\n\n参考时间    {i_hours:02d}:{i_minutes:02d}\n\n\n\n\n")
    set_awake_time('')


print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

if __name__ == '__main__':
    while True:
        calculate_and_show()
