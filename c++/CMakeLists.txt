cmake_minimum_required(VERSION 2.8.9)
project (test)  #指定工程名称

aux_source_directory(. PROGRAM_SOURCE) #搜索主目录下所有文件
add_subdirectory(mylib)  #将mylib文件夹加入子目录

add_executable(test ${PROGRAM_SOURCE})
target_link_libraries(out_file tool1lib)

