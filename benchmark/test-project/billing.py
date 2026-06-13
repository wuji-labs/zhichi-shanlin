"""场景 7 被测样本(反触发) · 含整数除法取整 bug 的计税函数.

这是纯数值逻辑 bug,与空间/界面/意境无关。
正确 agent 即便加载了 zhichi-shanlin,也应识别此为 OUT OF SCOPE,
直接修 bug,而不应套用三远/可游可居/留白等空间话术。
"""

TAX_RATE = 0.06  # 6% 税率


def calc_tax(amount_cents_str):
    """对金额计税,返回税额(应保留两位小数)。

    BUG: 这里用了整数除法把分转成元,99.99 元(9999 分)被截断成 99 元后再计税,
    丢掉了小数部分。应改为不丢精度的换算与四舍五入到两位小数。
    """
    cents = int(amount_cents_str)
    yuan = cents // 100          # BUG: 整数除法丢掉小数(9999 -> 99,而非 99.99)
    tax = yuan * TAX_RATE
    return tax


if __name__ == "__main__":
    # 期望:9999 分 = 99.99 元,税额应约 6.00;当前 bug 输出 99 * 0.06 = 5.94。
    print(calc_tax("9999"))
