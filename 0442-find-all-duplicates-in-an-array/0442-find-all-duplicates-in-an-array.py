class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count_dict={}
        for num in nums:
            if num in count_dict:
                count_dict[num]+=1
            else:
                count_dict[num]=1
                
        dup = []
        for num,count in count_dict.items():
            if count>1:
                dup.append(num)
        return dup        
            
        
        