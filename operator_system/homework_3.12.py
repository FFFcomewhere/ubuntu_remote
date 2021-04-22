import pandas as pd

if __name__ == '__main__':
    path = "hightemp.txt"
    #path = "hightemp.txt"

    with open(path, "r", encoding="UTF-8") as fp:
        file = fp.readlines()
    file = list(file)

    print(file)

    for i in range(len(file)):
        file[i] = file[i].replace('\t', ' ')

    print(file)

    open(path, "w", encoding="UTF-8").write((str(file))).close()

