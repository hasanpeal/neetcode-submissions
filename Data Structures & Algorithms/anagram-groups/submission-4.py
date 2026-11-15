class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Creates hashmap where value defaults to list[] (in this case) before append/add
        for s in strs:
            count = [0] * 26 # Array of length 26, initialized each index's value to 0
            for c in s:
                count[ord(c) - ord('a')] += 1 # ord gives the ASCCI and the difference gives the index
            res[tuple(count)].append(s) # Key can't be array, has to be variable, and tuple is a variable
        return list(res.values())