class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map character count to list of anagrams - O(mn)
        result = defaultdict(list)
        
        # Iterate through each string in strs
        for s in strs:
            # Hashmap for each letter of alphabet
            count = [0] * 26 

            # Map the chars in the string to the count hashmap to create a key
            for char in s:
                # Use Ascii codes to map into index of hashmap
                count[ord(char) - ord('a')] += 1

            # Use Hashmap of this particular string as key and append this word
            result[tuple(count)].append(s)

        return list(result.values())