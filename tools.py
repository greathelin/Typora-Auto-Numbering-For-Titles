#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @User : helin
# @Date : 2024/11/9 6:17
# @Author : He Lin
# @Summary :

def num_to_chinese(num: int) -> str:
    chinese_numerals = "零一二三四五六七八九"
    chinese_units = ["", "十", "百", "千", "万", "亿"]

    if num == 0:
        return "零"

    result = ""
    num_str = str(num)
    length = len(num_str)

    for i, digit in enumerate(num_str):
        n = int(digit)
        if n != 0:
            result += chinese_numerals[n] + chinese_units[length - i - 1]
        else:
            if not result.endswith("零") and i != length - 1:
                result += "零"

    result = result.replace("一十", "十")  # 特殊情况：10 应为 十
    return result.rstrip("零")  # 去掉末尾的多余零


if __name__ == '__main__':
    print(num_to_chinese(1))
    print(num_to_chinese(5))
    print(num_to_chinese(10))
    print(num_to_chinese(16))
    print(num_to_chinese(23))
    print(num_to_chinese(100))
    print(num_to_chinese(107))
    print(num_to_chinese(1654))
