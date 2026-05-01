from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list
        visited = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # dfs
       
        def dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    stack.extend(graph[curr]) # adds all the neigbors of curr to stack
        
        cc = 0
        for node in range(n): # goes through every node in graph
            if node not in visited:
                dfs(node)
                visited.add(node)
                cc+=1
        return cc


        # # dfs method, keep counter for # of connected components
        # def explore(node, edges, visited):
        #     visited.add(node)
        #     for edge in edges:
        #         if edge[0]==node and edge[1] not in visited:
        #             explore(edge[1], edges, visited)

        # def dfs(node, nodes, edges, visitedNodes):
        #     cc = 0
        #     for n in nodes:
        #         if n not in visitedNodes:
        #             cc += 1
        #             visitedNodes.add(n)
        #             visited = set()
        #             # explore method
        #             explore(n, edges, visited)
        #     return cc

        # cc = dfs(edges[0][0], nodes, edges, set())
        # return cc


        