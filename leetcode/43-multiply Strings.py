class Solution:
    def __init__(self):
        self.mapping = {'0' :0, '1' :1, '2' :2, '3' :3, '4' :4, '5' :5, '6' :6, '7' :7, '8' :8, '9' :9}
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        digits1 = [self.mapping[chr] for chr in num1[::-1]]
        digits2 = [self.mapping[chr] for chr in num2[::-1]]

        rank = 0
        product1 = None
        for i in range(len(digits1)):
            n = digits1[i]
            if n:
                product2 = [d for d in Solution.multiply_one_bit(digits2, n, rank)]
                if product1:
                    product1 = [d for d in Solution.add_digits_array(product1, product2)]
                else:
                    product1 = product2

            rank += 1

        return ''.join(self.digits[d] for d in product1[::-1])

    @staticmethod
    def add_digits_array(digits1, digits2):
        len1 = len(digits1)
        len2 = len(digits2)
        i = 0
        j = 0

        carry = 0
        while i < len1 and j < len2:
            result, carry = Solution.add_one_bit(digits1[i], digits2[j], carry)
            yield result

            i += 1
            j += 1

        while carry:
            if i < len1:
                result, carry = Solution.add_one_bit(digits1[i], 0, carry)
                i += 1
            elif j < len2:
                result, carry = Solution.add_one_bit(digits2[j], 0, carry)
                j += 1
            else:
                result, carry = 1, 0

            yield result

        while i < len1:
            yield digits1[i]
            i += 1

        while j < len2:
            yield digits2[j]
            j += 1

    @staticmethod
    def add_one_bit(n, m, c):
        r = n + m + c
        return (r, 0) if r < 10 else (r - 10, 1)

    @staticmethod
    def multiply_one_bit(digits, n, rank):
        while rank:
            rank -= 1
            yield 0

        carry = 0
        for i in range(len(digits)):
            m = digits[i]

            product = n * m + carry
            result = product % 10
            carry = int((product - result) / 10)

            yield result

        if carry:
            yield carry

    def multiply2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        digits1 = [self.mapping[chr] for chr in num1[::-1]]
        digits2 = [self.mapping[chr] for chr in num2[::-1]]

        result = list()
        result_len = 0

        for i in range(len(digits1)):
            for j in range(len(digits2)):
                product = digits1[i] * digits2[j]
                if i + j < result_len:
                    result[i + j] += product
                else:
                    result.append(product)
                    result_len += 1

        carry = 0
        for i in range(len(result)):
            n = result[i] + carry
            carry = int(n / 10)
            remainder = n - carry * 10
            result[i] = self.digits[remainder]

        if carry:
            result.append(self.digits[carry])

        return ''.join(result[::-1])


so = Solution()
# result = so.multiply('96', '9')
result = so.multiply2('96', '9')

print(result)
