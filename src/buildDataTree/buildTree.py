from . import dataTreeNode as dt


# The input of buildTree is a dictionary
def buildTree(data):
    # get the name of the root node from the key of dictionary
    root_name = list(data.keys())[0]
    
    # initialize the tree node without parent
    root_node = dt.dataTreeNode(root_name, None )
    
    # modify the child/value attribute of the root node
    modifyNode(root_node, data[root_name])
    
    return root_node
    
    
#  The node may contain:

# 1. a basic element without structure , like a string/integer/float
#    -> this node is a leaf node
#    -> we need to modify node.value

# 2. a dictionary 
#    -> this node has child nodes
#    -> we need to modify node.child
# (1) {  child_name: [...] }, a group of siblings with the same name, eg: album, artist, song, genre
# (2) { child_name1, child_name2, ...}, a group of siblings with different names
# (3) a mix of (1) and (2), { child_name1:[...], childname2, childname3, ...}

def modifyNode(node, data):
    if isinstance(data,dict):
        setChild(node, data)
    else:
        node.setValue(data)

# data is a dictionary
def setChild(node, data):
    child_list = []
    for key in data:
        if isinstance(data[key],list):
            #there are multiple child nodes with the same name
            child_list.extend(sameName(parent = node,name = key ,data = data[key]))
        else:
            new_node = dt.dataTreeNode(key,node)
            modifyNode(new_node,data[key])
            child_list.append(new_node)
    node.setChild(child_list)
    
    
# "data" is a list 
def sameName(parent,name,data):
    res_list = []
    for ele in data:
        new_node = dt.dataTreeNode(name,parent)
        modifyNode(new_node,ele)
        res_list.append(new_node)
    return res_list
