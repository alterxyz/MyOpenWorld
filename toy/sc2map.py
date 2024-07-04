import random


def main():
    # 定义地图词库
    map = ["虚空降临", "机会渺茫", "湮灭快车", "营救矿工", "聚铁成兵"]

    # 随机选择一个词
    selected_map = random.choice(map)

    # 定义角色词库
    player = [
        "泰凯斯",
        "炸鸡",
        "暗影卫队",
        "凯拉克斯",
        "阿巴斯",
        "诺娃",
        "德哈卡",
        "狗男女",
        "泰凯斯",
        "泽叔",
    ]

    # 随机选择一个词
    selected_player = random.choice(player)

    # 定义难度词库
    level = ["休闲", "普通", "困难", "残酷"]

    # 随机一个难度, 其中随机比例是1:3:3:1
    level_decision = random.randint(1, 8)
    if level_decision == 1 or level_decision == 2 or level_decision == 3:
        selected_level = level[1]
    elif level_decision == 4 or level_decision == 5 or level_decision == 6:
        selected_level = level[2]
    elif level_decision == 7:
        selected_level = level[1]
    else:
        selected_level = level[3]

    # 开还是不开, 进行一个随机的决策. 123表示开, 4表示不开
    decision = random.randint(1, 6)
    if decision == 1 or decision == 2 or decision == 3:
        print("时机挺好, GLHF\n")
        print("地图: ", selected_map)
        print("角色: ", selected_player)
        print("难度: ", selected_level)
    elif decision == 4:
        print("还是下个棋吧")
    elif decision == 5:
        print("嗯哼")
    else:
        print("还是先搞别的事情吧")
        print("粗暴对待猴子哦")
        # https://waitbutwhy.com/2013/10/why-procrastinators-procrastinate.html


if __name__ == "__main__":
    main()
