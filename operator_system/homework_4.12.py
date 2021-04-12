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




    N = int(input())
    files = []
    for i in range(math.ceil(len(contents) / N)):
        if((i+1)*N >= len(contents)):
            files.append(contents[i * N: len(contents)])

        else:
            files.append(contents[i * N: (i + 1) * N])


    for i in range(len(files)):
        k = ""
        for j in files[i]:
            k = k + j

        with open(str(i)+".txt", "w", encoding="UTF-8") as f:
            f.write(k)


