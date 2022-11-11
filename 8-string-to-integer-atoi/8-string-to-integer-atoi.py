class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        int_max = pow(2,31)-1
        int_min = -pow(2,31)
        index = 0
        sign = 1
        n = len(s)

        while index<n and s[index] == " ":
            index +=1
        
        if index < n and s[index] == "+":
            index +=1
            sign = 1
        elif index < n and s[index] == '-':
            index +=1
            sign = -1
        
        while index < n and s[index].isdigit():
            digit = ord(s[index])-ord('0')
            
            if (res > int_max//10) or (res == int_max//10 and digit > int_max % 10):
                return int_max if sign == 1 else int_min
            res = res*10 + digit
            index +=1
        return res*sign