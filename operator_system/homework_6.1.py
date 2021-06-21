if __name__ == '__main__':
    path = "hightemp.txt"

    data_col1 = []
    data_col2 = []

    try:
        file = open(path, "r", encoding="UTF-8")
    except FileExistsError:
        print("file is not  found")
    else:
        contents = file.readlines()

        for content in contents:
            temp1 = content.split('\t')[0]
            data_col1.append(temp1)

            temp2 = content.split('\t')[1]
            data_col2.append(temp2)

        str_col1 = ""
        str_col2 = ""

        for (i, j) in zip(data_col1, data_col2):
            str_col1 = str_col1 + i + "\n"
            str_col2 = str_col2 + j + "\n"

        with open("col1.txt", "w", encoding="UTF-8") as f:
            f.write(str_col1)

        dir_col1 = {}

        for i in data_col1:
            dir_col1[i] = str_col1.count(i)

        for i in sorted(dir_col1.items(), key=lambda x:x[1], reverse=True):
            print(i)