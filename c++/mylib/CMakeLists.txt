cmake_minimum_required(VERSION 2.8.9)

aux_source_directory(. TOOL1FILE)  #搜索当前子目录下所有文件

add_executable(tool1lib ${TOOL1FILE})  #将文件编译为tool1lib的文件

