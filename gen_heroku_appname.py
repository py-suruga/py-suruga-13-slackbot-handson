# coding:utf-8

# herokuのアプリ名を決めるスクリプト
# DEFAULT_PREFIXのあとに数字6桁をランダムで生成する

import random

DEFAULT_PREFIX = "pysurugabot"


def main():
    random_number = random.randint(1, 999999)
    print("生成したアプリ名は '{}-{:06}'".format(DEFAULT_PREFIX, random_number))


if __name__ == "__main__":
    main()
