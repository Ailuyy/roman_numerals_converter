# TODO: roman -> binary
# TODO: Once a letter has been used as a subtraction modifier,
# that letter cannot appear again in the string, unless that letter itself is subtracted from. For example, CDC is not valid (you would be subtracting 100 from 500, then adding it right back) – but CDXC (for 490) is valid. Similarly, XCX is not valid, but XCIX is.
# To summarize:
# C cannot follow CM or CD except in case of XC.
# X cannot follow XC or XL except in the case of IX.
# Once a letter has been subtracted from, neither it nor the next lowest multiple of 5 may appear again in the string - so neither X nor V can follow IX, neither C nor L may follow XC, and neither M nor D may follow CM.
# A letter cannot be used as a subtraction modifier if that letter, or the next highest multiple of 5, appears previously in the string - so IV or IX cannot follow I or V, XL or XC cannot follow X or L, and CD or CM cannot follow C or D.

class Roman:

    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def correctRoman(self, s: str):
        if not isinstance(s, str):
            raise TypeError('The given argument is not of type `str`.')
        else:
            prev_char = ''
            count = 0
            s = s.replace(' ', '').replace(',', '').replace('.', '').replace(';', '')

            if 1 <= len(s) <= 15:
                for char in s:
                    if char not in Roman.dic:
                        return False

                    if char in ['V', 'L', 'D'] and prev_char == char:
                        return False

                    if char == prev_char:
                        count += 1
                        if count > 3:
                            return False
                    else:
                        count = 1

                    if prev_char in ['V', 'L', 'D'] and Roman.dic[char] > Roman.dic[prev_char]:
                        return False

                    if prev_char in ['I', 'X', 'C'] and Roman.dic[prev_char] * 10 < Roman.dic[char]:
                        return False

                    if char == prev_char and char not in ['I', 'X', 'C']:
                        return False

                    prev_char = char

            return True

    def romanToInt(self, s: str):
        number = 0
        s = s.replace(' ', '').replace(',', '').replace('.', '').replace(';', '')
        if 1 <= len(s) <= 15: #3999 - max num
            for i in range(len(s)):
                if s[i] in Roman.dic:
                    if i < len(s) - 1 and Roman.dic[s[i]] < Roman.dic[s[i+1]]:
                        number -= Roman.dic[s[i]]
                    else:
                        number += Roman.dic[s[i]]
        return f'Your Roman number converted to integer: {number}'
