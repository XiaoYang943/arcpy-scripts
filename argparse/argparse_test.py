import argparse

def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="示例 Python 脚本，支持命令行参数")

    # 定义命令行选项
    parser.add_argument('-t', '--task', type=str, help='指定任务类型', required=True)
    parser.add_argument('-p', '--path', type=str, help='指定路径或文件', required=True)
    parser.add_argument('-v', '--verbose', action='store_true', help='启用详细输出')
    parser.add_argument('-o', '--output', type=str, help='指定输出文件路径')

    # 解析命令行参数
    args = parser.parse_args()

    # 打印传入的参数（如果启用详细模式）
    if args.verbose:
        print("启用详细输出模式")
        print("任务类型: {}".format(args.task))
        print("文件路径: {}".format(args.path))
        if args.output:
            print("输出路径: {}".format(args.output))

    # 根据任务类型执行不同的操作
    if args.task == 'convert':
        print("执行转换操作，目标路径: {}".format(args.path))
        if args.output:
            print("结果将保存到 {}".format(args.output))
    elif args.task == 'generate':
        print("执行生成操作，目标路径: {}".format(args.path))
    else:
        print("未识别的任务类型: {}".format(args.task))

if __name__ == "__main__":
    main()
