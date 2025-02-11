class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort() # tc=nlogn
        for i in range(len(intervals)):
            a=intervals[i][0]
            b=intervals[i][1]
            if len(res)>0:
                if b<=res[-1][1]:
                    continue
            for j in range(i,len(intervals)-1):
                    if b>=intervals[j+1][0] :
                        b=max(b,intervals[j+1][1]) #considering ek subarray poora hi andar ajaega previous ke 
                    else: 
                        break
            res.append([a,b])
        return res        