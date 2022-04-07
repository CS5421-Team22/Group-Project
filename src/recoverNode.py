def recoverNode(node):
    
    node_name = node.getName()
    
    node_dict = dict()
    node_dict[node_name] = dict()

    if node.haveChild():

        child_nodes = node.getChild()
        
        # child_dict is like { name1:[<name1>,<name1>], name2:[<name2>]}
        child_dict = dict()
        for child_node in child_nodes:
            child_name = child_node.getName()
            if child_name in child_dict:
                child_dict[child_name].append(child_node)
            else:
                child_dict[child_name] = [child_node]

        for child_name in child_dict:
            
            # child_name_nodes is like  [<name1>,<name1>]
            child_name_nodes = child_dict[child_name]

            tmp = []
            for child_name_node in child_name_nodes:
                tmp.append(recoverNode(child_name_node)[child_name])
                
            if len(tmp) == 1:
                node_dict[node_name][child_name] = tmp[0]
            else:
                node_dict[node_name][child_name] = tmp

    else:
        node_dict[node_name] = node.getValue()
        
    
    # return a dictionary
    return node_dict