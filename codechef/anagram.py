class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
            print (sorted(s))
        return sorted(s)==sorted(t)

class Solution2:
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True


class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            a=list(set(s))
            for i in a:
                c1=s.count(i)
                c2=t.count(i)
                if c1!=c2:
                    return False
            return True
        return False


if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    sol=Solution()
    if sol.isAnagram(s, t):
        print("yes")
    else:
        print("no")