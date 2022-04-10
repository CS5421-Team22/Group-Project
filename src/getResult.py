from buildDataTree.buildTree import *
from complexPredicate.complexPredicate import *
from getAxis.getAxis import *

from parseQuery import *
from recoverNode import *


def getResult(data,query):
    root_node = buildTree(data)
    res_nodes = getQuery(root_node,query)
    
    return [ recoverNode(res_node) for res_node in res_nodes]


def getResultFromRoot(root,query):
    res_nodes = getQuery(root,query)
    return [ recoverNode(res_node) for res_node in res_nodes]
