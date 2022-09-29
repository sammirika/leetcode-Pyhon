# 字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。
#
# 示例1:
#
#  输入：s1 = "waterbottle", s2 = "erbottlewat"
#  输出：True
# 示例2:
#
#  输入：s1 = "aa", s2 = "aba"
#  输出：False
# 提示：
#
# 字符串长度在[0, 100000]范围内。
# 说明:
#
# 你能只调用一次检查子串的方法吗？
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        len1 = len(s1);
        len2 = len(s2);
        if (len1 != len2):
            return False;
        return s1 in s2 * 2


def main():
    s1 = 'ab'
    s2 = 'ba'
    print(Solution.isFlipedString(Solution,s1, s2))


if __name__ == '__main__':
    main()
