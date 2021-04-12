import math


if __name__ == '__main__':
     #path = "hightemp.txt"
    path = "hightemp - 副本.txt"


    try:
        file = open(path, "r", encoding="UTF-8")
    except FileExistsError:
        print("file is not  found")
    else:
        contents = file.readlines()

    print(len(contents))

    N = int(input())
    for i in range(math.ceil(len(contents) / N)):
        print(i)
        if((i+1)*N >= len(contents)):
            for j in range(i*N, len(contents)):
                print(contents[j])
            print("-----------------------------")
        else:
            for j in range(i*N, (i + 1) * N):
                print(contents[j])
            print("-----------------------------")
