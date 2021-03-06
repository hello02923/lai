from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size=0

    def add(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        keycode = int(h.hexdigest(),16)
        index = keycode % self.capacity

        if not self.data[index]:##沒有就加上去
            self.data[index] = ListNode(keycode)
        else:##有就再最後面加上去
            temp = self.data[index]
            while temp.next:
                temp = temp.next
            temp.next = ListNode(keycode)

    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        keycode = int(h.hexdigest(),16)
        index = keycode % self.capacity
        
        if not self.data[index]:##先找有沒有這個東西
            return False
        else:
            temp=self.data[index]
            if temp.val == keycode:
                if temp.next is True:##.next有的話就直接連再下一個
                    self.data[index]=temp.next
                else:##沒有的話就是直接刪掉
                    self.data[index] = None
            else:
                while temp:##往鏈子下繼續找
                    if temp.next == keycode:
                        temp.next = temp.next.next
                        return
                    temp = temp.next
                return False

    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        keycode = int(h.hexdigest(),16)
        index = keycode % self.capacity 
        if self.data[index] is None:##找不到的情況
            return False     
        else:
            temp = self.data[index]
            while temp:##找到的情況以下
                if temp.val == keycode:
                    return True
                elif temp.val != keycode:##一條鍊子繼續往下找
                    temp = temp.next
                   
            return False
