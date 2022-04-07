class dataTreeNode:
    
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.child = []
        self.value = None
        
    def __repr__(self):
        return f"<{self.name}>"
        
    # Set
    def setValue(self, value):
        self.value = value
    
    def setChild(self, child):
        self.child = child
    
    # Get
    def getName(self):
        return self.name
    
    def getParent(self):
        return self.parent
    
    def getChild(self):
        return self.child
    
    def getValue(self):
        return self.value
    
    def getSibling(self):
        return [ sibling for sibling in self.parent.child if sibling != self ]
    
    
    # Judgement -> True/False
    def isRoot(self):
        if self.parent:
            return False
        else:
            return True
    

    def haveChild(self):
        if self.child:
            return True
        else:
            return False
    
    def haveValue(self):
        if self.value is None:
            return False
        else:
            return True
    
    def haveSibling(self):
        if len(self.getSibling()) < 1:
            return False
        else:
            return True

    
