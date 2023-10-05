class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict={}
        occur = set()
        for num in arr:
            if num in count_dict:
                count_dict[num]+=1
            else:
                count_dict[num]=1
                
        for num, count in count_dict.items():
            if count in occur:
                return False
            occur.add(count)
            
        return True    