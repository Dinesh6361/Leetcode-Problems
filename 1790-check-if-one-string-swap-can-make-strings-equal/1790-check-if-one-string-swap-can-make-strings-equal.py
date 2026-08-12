class Solution:
    def areAlmostEqual(self, s1,s2):
        a=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                a.append(i)
        if len(a)==0:
            return True
        if len(a)!=2:
            return False
        i,j=a
        return s1[i]==s2[j] and s1[j]==s2[i]