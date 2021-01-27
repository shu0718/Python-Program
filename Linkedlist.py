class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.start = None
    def insertlast(self,data):
        newnode = node(data)
        if self.start == None:
            self.start=newnode
        else:
            temp=self.start
            while temp.next!=None:
                temp = temp.next
            temp.next=newnode
    def deletefirst(self):
        if self.start == None:
            print("Linked list is empty")
        else:
            self.start=self.start.next
    def viewlist(self):
        if self.start == None:
            print("Linked list is empty")
        else:
            temp = self.start
            while temp.next!=None:
                print(temp.data,end=' ')
                temp=temp.next



mylist = Linkedlist()
mylist.insertlast(10)
mylist.insertlast(11)
mylist.insertlast(12)
mylist.viewlist()
print()
mylist.deletefirst()
mylist.viewlist()

print()
