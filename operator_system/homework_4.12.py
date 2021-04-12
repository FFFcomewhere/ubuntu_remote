if __name__ == '__main__':
     #path = "hightemp.txt"
    path = "hightemp - 副本.txt"


    try:
        file = open(path, "r", encoding="UTF-8")
    except FileExistsError:
        print("file is not  found")
    else:
        contents = file.readlines()


    file_list = list(contents)

    N = int(input())
    for i in range(len(file_list) // N):
        if((i+1)*N >= len(file_list)):
            print(file_list[i * N: len(file_list)])
        else:
            print(file_list[i * N: (i + 1) * N])