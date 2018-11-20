graph = {'A': [{'B':15}, {'C':75}],
		'B': [{'A':10}, {'D':30}, {'E':100}],
         # 'B': set(['A', 'D', 'E']),
         'C': [{'A':150}, {'F':20}]}
         # 'D': set(['B']),
         # 'E': set(['B', 'F']),
         # 'F': set(['C', 'E'])}
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

#dfs(graph, 'A')
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)

        for next in graph[vertex] - [path]:
        	print("next:"+str(next))
            if next == goal:
            	yield path + [next]
            else:
                queue.append((next, path + [next]))

print(list(bfs_paths(graph, 'A', 'B'))) 
