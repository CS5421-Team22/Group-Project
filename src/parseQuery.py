from buildDataTree.buildTree import *
from complexPredicate.complexPredicate import *
from getAxis.getAxis import *

import re

# Part 1: parse query to list of dictionaries
def parseQuery(query):
    
    res = []
    
    # sample:
    #        query = "class//stundent/mark" 
    #        ['class', '//', 'stundent', '/', 'mark']   
    queryArray = re.split("(//)",query)
    temp = []
    for tmp in queryArray:
        if tmp !="//":
            temp.extend(re.split("(/)",tmp))
        else:
            temp.append(tmp)
    temp = [ tmp.strip() for tmp in temp]
    queryArray = [ tmp for tmp in temp if tmp]
    

#     whether first query is doc
    firstQuery = queryArray[0]
    if 'doc' in firstQuery:
        queryArray = queryArray[1:]
        end = firstQuery.index('.')
        collection = firstQuery[5 : end]
        res.append({'collection': collection})
    else:
        res.append({})

    # parse the rest of queries
    for i in range(len(queryArray)):
        query = queryArray[i]
        if query == "/" or  query == "//":
            i += 1
            continue
            
        n = len(query)
        name = ''
        axis = ''
        predicate = ''
        index_pred = n
#         parse predicate
        # if query[-1] == ']':
        if '[' in query:
            index_pred = query.index('[')
            predicate = query[index_pred + 1 : -1]
            query = query[ : index_pred]
#         parse name and axis
        if "::" in query:
            index_split = query.index('::')
            axis = query[: index_split]
            name = query[index_split + 2 : index_pred]
        else:
            if i>0 and queryArray[i-1] == "//":
                axis = 'descendant'
            else:
                axis = 'child'
            name = query[: index_pred]
        dict_query = {'name' : name, 'axis' : axis, 'predicate': predicate}
        res.append(dict_query)
        i += 1
    # print("query = ", res)
    return res

def singleQuery(nodes,query):
    new_nodes = getNodesFromAxisAndName(nodes, query["axis"], query["name"])
    res = []
    
    if query["predicate"]:
        for node in new_nodes:
            if complexPredicate(node,query['predicate']):
                res.append(node)
    else:
        res = new_nodes
    
    return res  

def wholeQuery(nodes,queries):
    for query in queries[1:]:
        nodes = singleQuery(nodes,query)
    
    return nodes

def getQuery(rootnode, query):

    queries = parseQuery(query)
    nodes = [rootnode]
    
    return wholeQuery(nodes, queries)