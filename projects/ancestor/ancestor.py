from collections import defaultdict
from util import Queue, Stack

def earliest_ancestor(ancestors, starting_node):
   graph = defaultdict(set)
   for (parent, child) in ancestors:
        if not graph[parent]:
            graph[parent] = set()
        graph[parent].add(child)
   return bfs(graph, starting_node, ancestors)

def bfs(graph, starting_vertice, ancestors):
    visited = set()
    queue = Queue()
    queue.enqueue([starting_vertice])
    while queue.size() > 0:
        path = queue.dequeue()
        nodes = set(path) - visited
        for vertex in nodes:
            parents = [parent for (parent, child) in ancestors if child == vertex]
            if len(parents) != 0:
                parents = [min(parents)]
            parentsOfParents = [parent for (parent, child) in ancestors if child in parents]
            if len(parentsOfParents) == 0:
                return -1 if len(parents) == 0 else min(parents)
            for parent in parents:   
                new_path = list(path)
                new_path.append(parent)
                queue.enqueue(new_path)
            visited.add(vertex)