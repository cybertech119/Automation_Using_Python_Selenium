class Solution:
    def romanToInt(self, s):
        A ={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        E ={}
        for i, value in A.items():
            for j, value1 in A.items():
                if(i=="I"):
                    pass
                elif(value1<value):
                        E[j+i] = value-value1
        print(E)

        for k in E.items():
            print(k)
        # B = [*s]
        # D=B[::-1]
        # print(D)
        C=0
        # if s in
        #     C = C+A[B[i]]
        # print(C)

sol = Solution()
sol.romanToInt("IV")