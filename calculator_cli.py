#!/usr/bin/env python3
"""
命令行计算器
在终端中运行的交互式计算器
"""


def calculate(expression):
    """计算表达式"""
    try:
        # 替换中文符号
        expr = expression.replace("×", "*").replace("÷", "/").replace("（", "(").replace("）", ")")
        result = eval(expr)
        return result
    except ZeroDivisionError:
        return "错误：不能除以零"
    except Exception:
        return "错误：无效的表达式"


def format_result(result):
    """格式化结果"""
    if isinstance(result, float):
        if result.is_integer():
            return str(int(result))
        return f"{result:.10g}"
    return str(result)


def print_help():
    """打印帮助信息"""
    print("""
╔══════════════════════════════════════╗
║          命令行计算器                ║
╠══════════════════════════════════════╣
║  支持的运算符:                       ║
║    +  加法      -  减法              ║
║    *  乘法      /  除法              ║
║    ** 幂运算    %  取余              ║
║    () 括号                           ║
║                                      ║
║  命令:                               ║
║    help  显示帮助                    ║
║    quit  退出程序                    ║
║    exit  退出程序                    ║
╚══════════════════════════════════════╝
""")


def main():
    """主函数"""
    print("\n" + "=" * 40)
    print("       欢迎使用命令行计算器")
    print("=" * 40)
    print("输入 'help' 查看帮助，'quit' 退出")
    print()

    while True:
        try:
            user_input = input(">>> ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["quit", "exit", "q"]:
                print("再见！")
                break

            if user_input.lower() == "help":
                print_help()
                continue

            result = calculate(user_input)
            print(f"= {format_result(result)}")
            print()

        except KeyboardInterrupt:
            print("\n再见！")
            break
        except EOFError:
            print("\n再见！")
            break


if __name__ == "__main__":
    main()
