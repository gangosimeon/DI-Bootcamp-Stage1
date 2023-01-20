class Pagination():
    def __init__(self,items,pageSize):
        self.items =items
        self.pageSize = 4
        
    def getVisibleItems(self):
        visibleItems = []
        i=0
        while i < self.pageSize:
            visibleItems.append(self.items[i])
            i+=1
        print(visibleItems)

#liste=list("abcdefghijklmnopqrstuvwxyz")
#p=Pagination(liste,4)
#p.getVisibleItems()
"""
    def prevPage(self):
        pass
    
    
    def nextPage(self):
        for val in self.items:
            if val in visibleItems:
                self.items.remove(val)

liste=list("abcdefghijklmnopqrstuvwxyz")
p=Pagination(liste,4)
p.getVisibleItems()
p.nextPage()
p.getVisibleItems()
"""