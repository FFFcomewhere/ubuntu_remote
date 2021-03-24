cmake_minimum_required(VERSION 2.9.0)
project (test)
aux_source_directory(./ DIR_T)
add_executable(test ${DIR_T})
