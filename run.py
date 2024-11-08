#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @User : helin
# @Date : 2024/11/9 6:08
# @Author : He Lin
# @Summary :
import os.path

from tools import num_to_chinese


def numbering_titles(file_path: str, new_path: str, encoding="utf-8"):
    new_content = ""
    title_1_num = 0
    title_2_num = 0
    title_3_num = 0
    title_4_num = 0
    title_5_num = 0
    title_6_num = 0

    with open(file_path, "r", encoding=encoding) as f:
        content = f.readlines()

    for text in content:
        if text.startswith("# "):
            title_1_num += 1
            title_2_num = 0
            title_3_num = 0
            title_4_num = 0
            title_5_num = 0
            title_6_num = 0
            text = f"# {num_to_chinese(title_1_num)}、{text[2:]}"
        elif text.startswith("## "):
            title_2_num += 1
            title_3_num = 0
            title_4_num = 0
            title_5_num = 0
            title_6_num = 0
            text = f"## {title_1_num}.{title_2_num} {text[3:]}"
        elif text.startswith("### "):
            title_3_num += 1
            title_4_num = 0
            title_5_num = 0
            title_6_num = 0
            text = f"### {title_1_num}.{title_2_num}.{title_3_num} {text[4:]}"
        elif text.startswith("#### "):
            title_4_num += 1
            title_5_num = 0
            title_6_num = 0
            text = f"#### {title_1_num}.{title_2_num}.{title_3_num}.{title_4_num} {text[5:]}"
        elif text.startswith("##### "):
            title_5_num += 1
            title_6_num = 0
            text = f"##### {title_1_num}.{title_2_num}.{title_3_num}.{title_4_num}.{title_5_num} {text[6:]}"
        elif text.startswith("###### "):
            title_6_num += 1
            text = f"###### {title_1_num}.{title_2_num}.{title_3_num}.{title_4_num}.{title_5_num}.{title_6_num} {text[7:]}"

        new_content += text

    # 保存新的文件
    with open(new_path, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == '__main__':
    input_file_path = input("请输入需要添加编号的.md文件路径: ").strip().strip('"').strip("'")
    output_path = input_file_path.replace(".md", "_new.md")
    if os.path.exists(input_file_path):
        numbering_titles(input_file_path, output_path)
        print("编号添加完成:", input_file_path.replace(".md", "_new.md"))
    else:
        print("文件不存在，请重新输入")
