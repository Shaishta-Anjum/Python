class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s=s[::-1]
        print(s)

val=["h","e","l","l","o"]
print(Solution().reverseString(val))