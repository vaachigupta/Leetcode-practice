class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq={}
        target=len(arr)//2
        for i in arr:
            freq[i]=freq.get(i,0)+1

        counts=list(freq.values())
        counts.sort(reverse=True)

        removed=0
        ans=0

        for i in counts:
            removed+=i
            ans+=1

            if removed>=target:
                return ans

        