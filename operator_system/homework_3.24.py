if __name__ == '__main__':
    # #path = "hightemp.txt"
    # path = "hightemp - 副本.txt"
    #
    # data_col1 = []
    # data_col2 = []
    #
    # try:
    #     file = open(path, "r", encoding="UTF-8")
    # except FileExistsError:
    #     print("file is not  found")
    # else:
    #     contents = file.readlines()
    #
    #     for content in contents:
    #         temp1 = content.split('\t')[0]
    #         data_col1.append(temp1)
    #
    #         temp2 = content.split('\t')[1]
    #         data_col2.append(temp2)
    #
    #     str_col1 = ""
    #     str_col2 = ""
    #     for (i, j) in zip(data_col1, data_col2):
    #         str_col1 = str_col1 + " " + i
    #         str_col2 = str_col2 + " " + j
    #
    #
    #
    #     with open("col1.txt", "w", encoding="UTF-8") as f:
    #         f.write(str_col1)
    #     with open("col2.txt", "w", encoding="UTF-8") as f:
    #         f.write(str_col2)

    try:
        col_1 = open("col1.txt", "r", encoding="UTF_8")
        col_2 = open("col2.txt", "r", encoding="UTF_8")
    except FileExistsError:
        print("no found file")
    else:
        data1 = col_1.readlines()[0].split(" ")
        data2 = col_2.readlines()[0].split(" ")
        new_data = ""


        for (word1, word2) in zip(data1, data2):
            new_data = new_data + word1+'\t'+word2+'\n'

        print(new_data)

        open("new_data.txt", "w", encoding="UTF-8").write(new_data)