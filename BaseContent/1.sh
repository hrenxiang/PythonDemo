#!/bin/bash

get_file_type() {
    file_path='/path/to/some/213'
    FILE_HASH=$(basename -- ${file_path} | tr -d '/\\')
    echo 文件哈希值: "$FILE_HASH"
    set -x
    sleep 10
    FILE_TYPE=$(mysql -h 127.0.0.1 -u root -p12345678 -D pos -Nse "select * from es_activity where id = \"$FILE_HASH\"")
    echo 文件类型: "$FILE_TYPE"
    set +x
}

# 调用函数
get_file_type