cmake_minimum_required(VERSION 2.8.9)
project (test)

aux_source_directory(. PROGRAM_SOURCE)
aux_source_directory(./mylib MYLIB_PROGRAM_SOURCE)

add_executable(test ${PROGRAM_SOURCE} ${MYLIB_PROGRAM_SOURCE})

