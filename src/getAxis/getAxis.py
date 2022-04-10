def getNodesFromAxisAndName(nodes, axis, name):
    if type(nodes) != list:
        nodes = [nodes]
    res = getNodesFromAxis(nodes, axis)
    res = getNodesFromName(res, name)
    return res

def getNodesFromAxis(nodes, axis):
    if type(nodes) != list:
        nodes = [nodes]
    res = []
    if (axis == 'child'):
        for node in nodes:
            res.extend(node.getChild())
    elif (axis == 'parent'):
        for node in nodes:
            res.append(node.getParent())
    elif (axis == 'sibling'):
        for node in nodes:
            res.extend(node.getSibling())
    elif (axis == 'ancestor'):
        for node in nodes:
            temp = node.getParent()
            if temp.name == "root" and temp.parent is None:
                continue
            if temp.parent:
                res.extend(getNodesFromAxis(temp, axis))
            res.append(temp)
    elif (axis == 'descendant'):
        for node in nodes:
            if node.child:
                temp = node.getChild()
                res.extend(getNodesFromAxis(temp, axis))
                res.extend(temp)
    res2 = []
    for node in res:
        if not(node in res2):
            res2.append(node)
    return res2

def getNodesFromName(nodes, name):
    if type(nodes) != list:
        nodes = [nodes]
    res = []
    for node in nodes:
        if node.getName() == name:
            res.append(node)
    return res
