class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set()
        num2 = set()
        for num in nums1:
            num1.add(num)
        for num in nums2:
            num2.add(num)
        print(num1)    
        print(num2)
        
        l1 = list(num1)
        l2 = list(num2)
        out= []
        for num in l1:
            if num in l2:
                out.append(num)
        return out        