class Solution:
    def decodeString(self, s: str) -> str:
        brk, num, alp = [], [], []
        res = ""
        num_temp, string_temp = "", ""

        # Initialize alp with an empty string to handle content outside brackets
        alp.append("")

        for c in s:
            if c.isdigit():
                if string_temp != "":
                    alp[-1] += string_temp
                    string_temp = ""
                num_temp += c
            elif c == "[":
                num.append(int(num_temp))
                num_temp = ""
                alp.append("")
                brk.append('[')
            elif c == "]":
                if string_temp != "":
                    alp[-1] += string_temp
                    string_temp = ""
                
                brk.pop()
                n = num.pop()
                a = alp.pop()
                mult = n * a
                
                alp[-1] += mult
            elif c.isalpha():
                string_temp += c

        return alp[0] + string_temp