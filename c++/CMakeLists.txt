cmake_minimum_required(VERSION 2.8.9)
project (main)  #指定工程名称

add_subdirectory(mylib)   #添加子目录

aux_source_directory(. PROGRAM_SOURCE) #搜索主目录下所有文件

add_executable(main ${PROGRAM_SOURCE})

target_link_libraries(main tool1lib)   #指明可执行文件需要连接一个tool1lib的链接库
