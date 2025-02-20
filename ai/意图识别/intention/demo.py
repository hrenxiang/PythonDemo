# import traceback
#
# try:
#     result = 1 / 0  # 引发一个异常
# except Exception as e:
#     error_message = traceback.format_exc()  # 获取堆栈信息
#     error_type = type(e).__name__  # 获取异常的类型（例如：ZeroDivisionError）
#     error_msg = str(e)  # 获取异常的具体信息（例如：division by zero）
#
#     print(f"An error occurred: Type: {error_type}, Message: {error_msg}, Stack Trace: {error_message}")
import datetime

# import os
# import pandas as pd
#
#
# def save_error_log(error_log_list, output_date_path):
#     # 将传入的错误日志列表转换为 DataFrame
#     error_df = pd.DataFrame(error_log_list)
#
#     # 检查文件是否存在
#     file_exists = os.path.exists(f"{output_date_path}/error_log_list.csv")
#
#     # 使用 mode='a' 来追加到文件末尾，header=False 表示不写入列标题
#     error_df.to_csv(f"{output_date_path}/error_log_list.csv", index=False, sep=',', encoding='utf-8',
#                     mode='a', header=not file_exists)
#
#     print("错误日志已保存或追加到 error_log_list.csv")
#
#
# # 示例 1：第一次写入数据
# error_log_list1 = [{'datetime': '2025-02-18', 'serial_number': '123456'},
#                    {'datetime': '2025-02-19', 'serial_number': '654321'}]
# save_error_log(error_log_list1, '/Users/hrenxiang/Downloads')
#
# # 示例 2：追加数据
# error_log_list2 = [{'datetime': '2025-02-20', 'serial_number': '112233'},
#                    {'datetime': '2025-02-21', 'serial_number': '445566'}]
# save_error_log(error_log_list2, '/Users/hrenxiang/Downloads')


current_time = datetime.datetime.now() + datetime.timedelta(hours=8)

# 判断是否已经是晚上11点半后但还没到第二天零点
if current_time.hour == 23 and current_time.minute >= 20:
    current_time += datetime.timedelta(days=1)

# 格式化日期为YYYYMMDD
current_date_day = current_time.strftime("%Y%m%d")

print(current_date_day)
