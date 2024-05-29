#https://leetcode.com/problems/add-binary/
#Add Binary
class Solution():
    def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]
    a="1010"
    b="1011"
    print(addBinary(a,b))
