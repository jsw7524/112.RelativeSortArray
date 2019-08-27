class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dict = { a:order for order,a in zip(range(len(arr2)),arr2)}
        arr1.sort(key=lambda a: dict[a] if a in dict else 1001+a )
        return arr1

sln=Solution()
assert [22,28,8,6,17,44]==sln.relativeSortArray([28,6,22,8,44,17],[22,28,8,6])