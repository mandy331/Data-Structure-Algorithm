# 如果不知道Node的個數的話，不能用for的時候，可以用while。
# for: 明確知道什麼時候要停止
# while: 條件結束後停止


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# head: 以單個Node為節點所組成的list
class Solution:
    def insertionSortList(self, head) -> Node:
        if head is None:
            return None
        Head = ListNode(-1)
        Head.next = InsertNode = head
        # 依次確認list裡的每個Node(處理值)
        while head and head.next:
            # 如果此處理值(head)小於下一項，則需要重新定義插入值
            if head.val > head.next.val:
                #Define InsertNode
                InsertNode = head.next
                #Define PreNode: before InsertNode的Node
                PreNode = Head
                #依次確認PreNode
                while PreNode.next.val < InsertNode.val:
                    PreNode = PreNode.next
                #Save the nodes behind InsertNode
                head.next = InsertNode.next
                
                #add InsertNode between PreNode and head
                InsertNode.next = PreNode.next
                PreNode.next = InsertNode
            else:
                head = head.next
        return Head.next