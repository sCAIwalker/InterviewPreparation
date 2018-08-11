#Assume defaultdict(set)

from collections import deque

def routeBetweenNodes(graph, node1, node2):
    if (node1 == node2):
        return True
    
    queue = deque()
    node1.visited = True
    queue.append(node1)

    while (len(queue) != 0):
        currNode = queue.popleft()

        if (currNode == node2):
            return True

        for node in graph[currNode]:
            if (node.visited == False):
                node.visited = True
                queue.append(node)
                
    return False