cmake_minimum_required(VERSION 2.8.9)

project (test)

add_subdirectory(./mylib)

aux_source_directory(./ DIR_T)

add_executable(test ${DIR_T})

target_link_libraries(test mylib)
