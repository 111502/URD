#!/usr/bin/env python3
"""
图形界面计算器
使用 tkinter 构建的简单计算器应用程序
"""

import tkinter as tk
from tkinter import messagebox


class Calculator:
    """计算器类"""

    def __init__(self, root):
        self.root = root
        self.root.title("计算器")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#2d2d2d")

        # 当前输入的表达式
        self.expression = ""
        # 显示的文本
        self.display_text = tk.StringVar()
        self.display_text.set("0")

        self._create_display()
        self._create_buttons()

    def _create_display(self):
        """创建显示屏"""
        display_frame = tk.Frame(self.root, bg="#2d2d2d")
        display_frame.pack(pady=20, padx=10, fill="x")

        display = tk.Entry(
            display_frame,
            textvariable=self.display_text,
            font=("Arial", 32),
            justify="right",
            bd=0,
            bg="#1e1e1e",
            fg="#ffffff",
            insertbackground="#ffffff",
            state="readonly"
        )
        display.pack(fill="x", ipady=15)

    def _create_buttons(self):
        """创建按钮"""
        button_frame = tk.Frame(self.root, bg="#2d2d2d")
        button_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # 按钮布局
        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="]
        ]

        for row_idx, row in enumerate(buttons):
            for col_idx, text in enumerate(row):
                self._create_button(button_frame, text, row_idx, col_idx)

    def _create_button(self, parent, text, row, col):
        """创建单个按钮"""
        # 根据按钮类型设置颜色
        if text in ["÷", "×", "-", "+", "="]:
            bg_color = "#ff9500"
            fg_color = "#ffffff"
            hover_color = "#ffad33"
        elif text in ["C", "±", "%"]:
            bg_color = "#a5a5a5"
            fg_color = "#000000"
            hover_color = "#c0c0c0"
        elif text == "⌫":
            bg_color = "#ff3b30"
            fg_color = "#ffffff"
            hover_color = "#ff6961"
        else:
            bg_color = "#333333"
            fg_color = "#ffffff"
            hover_color = "#505050"

        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 20, "bold"),
            bg=bg_color,
            fg=fg_color,
            activebackground=hover_color,
            activeforeground=fg_color,
            bd=0,
            relief="flat",
            command=lambda t=text: self._on_button_click(t)
        )

        # 0 按钮横跨两列
        if text == "0":
            button.grid(row=row, column=col, columnspan=1, sticky="nsew", padx=2, pady=2)
        else:
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        # 设置行列权重
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)

        # 绑定悬停效果
        button.bind("<Enter>", lambda e, b=button, c=hover_color: b.configure(bg=c))
        button.bind("<Leave>", lambda e, b=button, c=bg_color: b.configure(bg=c))

    def _on_button_click(self, text):
        """处理按钮点击事件"""
        if text == "C":
            self._clear()
        elif text == "⌫":
            self._backspace()
        elif text == "±":
            self._toggle_sign()
        elif text == "%":
            self._percentage()
        elif text == "=":
            self._calculate()
        elif text in ["÷", "×", "-", "+"]:
            self._add_operator(text)
        else:
            self._add_digit(text)

    def _clear(self):
        """清除所有输入"""
        self.expression = ""
        self.display_text.set("0")

    def _backspace(self):
        """删除最后一个字符"""
        if self.expression:
            self.expression = self.expression[:-1]
            if self.expression:
                self.display_text.set(self.expression)
            else:
                self.display_text.set("0")

    def _toggle_sign(self):
        """切换正负号"""
        if self.expression and self.expression != "0":
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            else:
                self.expression = "-" + self.expression
            self.display_text.set(self.expression)

    def _percentage(self):
        """计算百分比"""
        try:
            result = float(self.expression) / 100
            self.expression = str(result)
            self.display_text.set(self._format_result(result))
        except (ValueError, ZeroDivisionError):
            pass

    def _add_operator(self, operator):
        """添加运算符"""
        if self.expression:
            # 如果最后一个字符是运算符，替换它
            if self.expression[-1] in ["+", "-", "×", "÷"]:
                self.expression = self.expression[:-1] + operator
            else:
                self.expression += operator
            self.display_text.set(self.expression)

    def _add_digit(self, digit):
        """添加数字或小数点"""
        if digit == ".":
            # 检查当前数字是否已有小数点
            parts = self.expression.replace("+", " ").replace("-", " ").replace("×", " ").replace("÷", " ").split()
            if parts and "." in parts[-1]:
                return
            if not self.expression or self.expression[-1] in ["+", "-", "×", "÷"]:
                self.expression += "0."
                self.display_text.set(self.expression)
                return

        self.expression += digit
        self.display_text.set(self.expression)

    def _calculate(self):
        """计算结果"""
        try:
            # 替换显示符号为 Python 运算符
            expr = self.expression.replace("×", "*").replace("÷", "/")

            # 安全地计算表达式
            if expr:
                result = eval(expr)
                self.expression = str(result)
                self.display_text.set(self._format_result(result))
        except ZeroDivisionError:
            messagebox.showerror("错误", "不能除以零！")
            self._clear()
        except Exception:
            messagebox.showerror("错误", "无效的表达式！")
            self._clear()

    def _format_result(self, result):
        """格式化结果显示"""
        if isinstance(result, float):
            # 如果是整数结果，显示为整数
            if result.is_integer():
                return str(int(result))
            # 限制小数位数
            return f"{result:.10g}"
        return str(result)


def main():
    """主函数"""
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
