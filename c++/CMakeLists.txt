cmake_minimum_required(VERSION 2.8.9)
project (test)  #指定工程名称

aux_source_directory(. PROGRAM_SOURCE) #搜索主目录下所有文件
aux_source_directory(./mylib SON_PROGRAM_SOURCE) #搜索子目录下所有文件

add_subdirectory(mylib)

add_executable(test ${PROGRAM_SOURCE} ${SON_PROGRAM_SOURCE})

