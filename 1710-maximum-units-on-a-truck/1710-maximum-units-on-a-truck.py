class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x: x[1], reverse=True)
        units=0

        for boxes, unitPerBox in boxTypes:
            if truckSize>=boxes:
                units+=boxes*unitPerBox
                truckSize-=boxes

            else:
                units+=truckSize*unitPerBox
                break
        
        return units