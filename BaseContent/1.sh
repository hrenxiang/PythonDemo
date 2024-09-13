#!/bin/bash

get_file_type() {
    file_path='/path/to/some/213'
    FILE_HASH=$(basename -- ${file_path} | tr -d '/\\')
    echo "文件哈希值: $FILE_HASH" >&2
    set -x
    FILE_TYPE=$(mysql -h 127.0.0.1 -u root -p12345678 -D pos -Nse "select * from es_activity where id = \"$FILE_HASH\"")
    echo "$FILE_TYPE"
    set +x
}

# 定义 test 函数
test() {
    # 捕获 get_file_type 函数的输出
    local result
    result=$(get_file_type)
    echo "get_file_type 函数的输出:"
    echo "$result"
}

# 调用 test 函数
test