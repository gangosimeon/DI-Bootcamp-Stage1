#1/ et 2/
class Pagination():
    livre=[]
    def __init__(self,items,pageSize):
        self.items =items
        self.pageSize = 4
        
    def getVisibleItems(self):
        visibleItems = []
        if len(self.items)>self.pageSize:
            i=0
            while i < self.pageSize:
                visibleItems.append(self.items[i])
                i+=1
            for mot in visibleItems:
                self.items.remove(mot)
            self.livre.append(visibleItems)
        else:
            taille=len(self.items)
            i=0
            while i < taille:
                visibleItems.append(self.items[i])
                i+=1
            for mot in visibleItems:
                self.items.remove(mot)
            self.livre.append(visibleItems)
        print(visibleItems)

#print(p.livre)

    def prevPage(self,pageActuNum):
        while pageActuNum-1<=0:
            print("Cette page est inexistant0 !")
            break
        else:
            print(f"La page precedant {self.livre[pageActuNum-1]} est: {self.livre[pageActuNum-2]}")
    
    def nextPage(self,pageActuNum):
        while pageActuNum > (len(self.livre)-1):
            print("C'est la derniere page !")
            break
        else:
            print(f"La page suivant {self.livre[pageActuNum-1]} est: {self.livre[pageActuNum]}")
        
    
    def firstpage(self):
        print(f"La premiere page est: {self.livre[0]}")
    
    def lastpage(self):
        print(f"La derniere page est: {self.livre[-1]}")
    
    def goToPage(self,pageNum):
        print(f"La page {pageNum} est: {self.livre[pageNum-1]}")
    
    def CreatePages(self,liste):
        while liste!=[]:
            self.getVisibleItems()   
        print(self.livre)    
        
liste=list("abcdefghijklmnopqrstuvwxyz")
p=Pagination(liste,4)
p.CreatePages(liste)
print()
p.prevPage(5)
p.goToPage(4)
p.nextPage(2)
p.firstpage()
p.lastpage()