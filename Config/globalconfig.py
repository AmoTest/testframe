import os
from Public.Common.ReadConfig import ReadConfig


# 读取配置文件
# 获取config.ini的路径

print(os.path.realpath(__file__))
print(os.path.realpath('.'))
print(os.path.abspath(__file__))
print(os.path.abspath('.'))
file_path = os.path.split(os.path.realpath(__file__))[0]
print(file_path)

#读取配置文件
read_config = ReadConfig(os.path.join(file_path, "config.ini"))

#借助config.ini获取项目的参数
project_path = read_config.getConfigValue("project", "project_path")

# 日志路径
log_path = os.path.join(project_path, "Report", "Log")
print(log_path)

# 测试用例路径
TestCase_path = os.path.join(project_path, "TestCase")
print(TestCase_path)

# 测试数据路径
data_path = os.path.join(project_path, "Data")
print(data_path)

