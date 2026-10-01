from collections import deque

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = {}
        
        for i in range(self.V):
            self.graph[i]=[]
            
    def add_edges(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def bfs(self,start):
        visited = [False] * self.V
        queue = deque()
        
        queue.append(start)
        visited[start] = False
        
        while queue:
            node = queue.popleft()
            print(node,end=" ")
            
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    
if __name__ == "__main__":
    V = int(input("enter number of vertex: "))
    g = Graph(V)
    
    E = int(input("enter number of edges: "))
    
    print("Enter edges (u v)")
    
    for i in range(E):
        u,v = map(int,input().split())
        g.add_edges(u,v)
    
    S = int(input("enter staring vertex: "))
    
    g.bfs(S)
    
    
