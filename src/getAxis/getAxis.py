def getNodesFromAxisAndName(nodes, axis, name):
    if type(nodes) != list:
        nodes = [nodes]
    res = getNodesFromAxis(nodes, axis)
    res = getNodesFromName(res, name)
    return res

def getNodesFromAxis(nodes, axis):
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
            res.extend(getNodesFromAxis(temp, axis))
            res.extend(temp)
    elif (axis == 'descendant'):
        for node in nodes:
            temp = node.getChild()
            res.extend(getNodesFromAxis(temp, axis))
            res.extend(temp)
    return res

def getNodesFromName(nodes, name):
    res = []
    for node in nodes:
        if node.getName() == name:
            res.append(node)
    return res
