# 產生1000字元隨機內容

import random
import os


def random_string(num):
    f = open("test.txt", "w")
    for i in range(num):
        f.write(chr(random.randint(0, 127)))
    f.close()


# 使用指令產生git分支
def git_branch(branch_name):
    os.system("git branch " + branch_name)
