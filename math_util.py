# -*- coding: utf-8 -*-
from collections import OrderedDict

def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])

def write_aegean(num):
    aegean = [
        (90000, "𐄳"),(80000, "𐄲"),(70000, "𐄱"),(60000, "𐄰"),(50000, "𐄯"),(40000, "𐄮"),(30000, "𐄭"),(20000, "𐄬"),(10000, "𐄫"),        
        (9000, "𐄪"),(8000, "𐄩"),(7000, "𐄨"),(6000, "𐄧"),(5000, "𐄦"),(4000, "𐄥"),(3000, "𐄤"),(2000, "𐄣"),(1000, "𐄢"),
        (900, "𐄡"),(800, "𐄠"),(700, "𐄟"),(600, "𐄞"),(500, "𐄝"),(400, "𐄜"),(300, "𐄛"),(200, "𐄚"),(100, "𐄙"),
        (90, "𐄘"),(80, "𐄗"),(70, "𐄖"),(60, "𐄕"),(50, "𐄔"),(40, "𐄓"),(30, "𐄒"),(20, "𐄑"),(10, "𐄐"),
        (9, "𐄏"),(8, "𐄎"),(7, "𐄍"),(6, "𐄌"),(5, "𐄋"),(4, "𐄊"),(3, "𐄉"),(2, "𐄈"),(1, "𐄇")																										
    ]

    def aegean_num(num):
        for (k,v) in aegean:
            x, y = divmod(num, k)
            yield v * x
            num -= (k * x)
            if num <= 0:
                break

    return "".join([a for a in aegean_num(num)])

def _enumerate_digits(number):
    """
    :type number: int|long
    :rtype: collections.Iterable[int, int]
    """
    position = 0
    while number > 0:
        digit = number % 10
        number //= 10
        yield position, digit
        position += 1


# Reference: https://blog.gocalf.com/number-to-chinese
def write_chinese(num):

    CHINESE_ZERO = '零'
    CHINESE_DIGITS = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    CHINESE_UNITS = ['', '十', '百', '千']
    CHINESE_GROUP_UNITS = ['', '万', '亿', '兆']

    def translate_number_to_chinese(number):
        """
        :type number: int|long
        :rtype: string
        """
        if not isinstance(number, int) and not isinstance(number, long):
            raise ValueError('number must be integer')

        if number == 0:
            return CHINESE_ZERO

        words = []

        # Begin core loop.
        # Version 0.1
        group_is_zero = True
        need_zero = False
        for position, digit in reversed(list(_enumerate_digits(number))):
            unit = position % len(CHINESE_UNITS)
            group = position // len(CHINESE_UNITS)

            if digit != 0:
                if need_zero:
                    words.append(CHINESE_ZERO)

                if digit != 1 or unit != 1 or not group_is_zero or (group == 0 and need_zero):
                    words.append(CHINESE_DIGITS[digit])

                words.append(CHINESE_UNITS[unit])

            group_is_zero = group_is_zero and digit == 0

            if unit == 0 and not group_is_zero:
                words.append(CHINESE_GROUP_UNITS[group])

            need_zero = (digit == 0 and (unit != 0 or group_is_zero))

            if unit == 0:
                group_is_zero = True

        # End core loop.

        return ''.join(words)

    return translate_number_to_chinese(num)