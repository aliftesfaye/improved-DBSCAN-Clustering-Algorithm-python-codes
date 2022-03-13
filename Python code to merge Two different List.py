class MergeList:
    
    def __init__(self,list1,list2):
        self.list1 = list1
        self.list2 = list2
        
    def mergeList(self):
        merged_list = [[self.list1[i],self.list2[i]] for i in range(0,len(self.list1))]
        return merged_list
   
list1 = [1,2,5,4,7,8,6]
list2 = [6,8,7,5,9,6,7]
ListObject = MergeList(list1,list2)
print(ListObject.mergeList())
