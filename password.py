class Solution(object):

    def LengthCheck(self, s):

        # make a list to track the number of >3 repeated characters
        l = []
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                if curr > 2:
                    l.append(curr)
                curr = 1
        if (curr > 2):
            l.append(curr)
        return l
    #functions to check if the password has it's required characters

    def uppercaseCheck(self, s:str):
        if any('A' <= c <= 'Z' for c in s): return 0
        return 1

    def lowercaseCheck(self, s:str):
        if any('a' <= c <= 'z' for c in s): return 0
        return 1

    def numberCheck(self, s:str):
        if any('0' <= c <= '9' for c in s): return 0
        return 1

    def strongPasswordChecker(self, s: str) -> int:
        leng = len(s)
        lis = self.LengthCheck(s)
        # if the length is less than 4, then we just need 6-len to make the password meets the conditions
        if (leng < 4):
            return 6 - leng
        # since we have three conditions (different characters), then we need to make sure if it has all of them or not
        if (leng == 4):
            if (self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s) == 3): return 3
            return 2

        # add three more required characters if it does not have those, 2 if it has just one of them, 1 (to make it 6 and/or the missing
        # required characters
        if (leng == 5):
            if (self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s) == 3): return 3
            if (self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s) == 2): return 2
            return 1



        # If the length is acceptable, then we need to make sure it has the requirements and we can modify the
        # missing part with replacing
        if (leng <= 20):
            print(lis)
            steps_for_repeated = sum(int(x / 3) for x in lis)
            print(steps_for_repeated)
            exit()
            return max(steps_for_repeated, self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s))

        # for >20 passw
        if (leng > 20):
            numdel = leng - 20
            repalces_for_repeated = sum(int(x / 3) for x in lis)

            l = list(x % 3 + 1 for x in lis)
            l.sort()

            # variable to keep track of how many deletions are left
            rem = numdel

            # the optimal way to get rid of extras and not allowed repreated
            for i in range(0, len(l)):
                if (rem >= l[i]):
                    rem -= l[i]
                    repalces_for_repeated -= 1

            repalces_for_repeated -= int(rem / 3)

            #making sure that that after deletion we have other conditions for the strong password

            if (repalces_for_repeated < self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(
                s)):
                repalces_for_repeated= self.uppercaseCheck(s) + self.lowercaseCheck(s) + self.numberCheck(s)

            # total changes
            return numdel + repalces_for_repeated
        return 0
if __name__ == "__main__":
    s = 'aabb11'
    new_class = Solution()
    A = new_class.strongPasswordChecker(s)
    print(A)
