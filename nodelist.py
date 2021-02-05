class Solution:
    def mergeLists(self, lists):
        self.node = []
        for i in lists:
            while i:
                self.node.append(i.val)
                i = i.next
        start = end = ListNode(0)

        for i in sorted(self.node):
            start.next = ListNode(i)
            start = start.next
        return end.next

if __name__ == '__main__':
    sol = Solution()
    lists = [[2, 3, 4], [1, 4]]
    merger = sol.mergeLists()
    print(merger)
