# coding:utf-8

# herokuのアプリ名を決めるスクリプト
# DEFAULT_PREFIXのあとに数字6桁をランダムで生成する

import random

DEFAULT_PREFIX = "pysurugabot"


def main():

    random_number = random.randint(1, 999999)
    appname = "{}-{:06}".format(DEFAULT_PREFIX, random_number)
    print("Generate Slack/Heroku App name:", appname)

    with open("appname.txt", "w") as appname_file:
        appname_file.write(appname)


if __name__ == "__main__":
    main()
