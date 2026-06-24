class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1 , t2, t3 = target

        curr = [0 , 0 , 0]

        for x , y ,z in triplets:
            if x > t1 or y > t2 or z > t3 :
                continue

            curr[0] = max(curr[0], x)            
            curr[1] = max(curr[1], y)            
            curr[2] = max(curr[2], z)       
        return curr == target         