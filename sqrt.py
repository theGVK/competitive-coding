#square root using binary search

def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        start,end,mid=1,x,-1
        while start<=end:
            mid=start+(end-start)/2
            if(mid*mid >x):
                end=mid-1
            elif mid*mid==x:
                return mid
            else:
                start=mid+1
        return int(round(end))
