class Solution:
    def countGoodRectangles(self, rectangles):
        big=0
        c=0
        for a,b in rectangles:
            side=min(a,b)
            if side>big:
                big=side
                c=1
            elif side==big:
                c+=1
        return c
        