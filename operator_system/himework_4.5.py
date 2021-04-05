import pandas as pd

if __name__ == '__main__':
    #path = "hightemp.txt"
    path = "hightemp - 副本.txt"

    print("输入head为输出前N行\n输入tail为输出后N行")
    op = input()

    if (op == "head"):
        """前N行"""
        print("请输入你想输出的行数N")
        with open(path, "r", encoding="UTF-8") as fp:
            file = list(fp.readlines())

            for i in range(int(input())):
                print(file[i])
    elif(op == "tail"):
        """后N行"""
        print("请输入你想输出的行数N")
        with open(path, "r", encoding="UTF-8") as fp:
            file = list(fp.readlines())

            for i in range(len(file)-1, len(file)-1-int(input()), -1):
                print(file[i])
    else:
        print("输入指令有误,退出")
        exit()