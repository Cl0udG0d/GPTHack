import sys

if getattr(sys, 'frozen', False):
    # 在可执行文件中运行
    print("当前是可执行文件（exe）运行状态")
else:
    # 在 Python 文件中运行
    print("当前是Python文件运行状态")
