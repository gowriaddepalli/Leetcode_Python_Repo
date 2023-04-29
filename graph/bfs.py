# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from collections import deque

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'F'],
  'C' : ['G'],
  'D' : [],
  'E' : [],
  'F' : ['H'],
  'G' : ['I'],
  'H' : [],
  'I' : []
}

def bfs(graph, node):
    print(f"node:{node}")
    visited = []
    queue = deque()
    
    # Add node to visited and queue
    visited.append(node)
    queue.append(node)
    
    print(visited)
    print(queue)
    
    while queue:
        #popleft
        s = queue.popleft()
        print(s)
        
        for child in graph[s]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
        
def main():
    bfs(graph, 'A')

main()      
        



# Reference: https://github.com/msambol/youtube/blob/master/search/breadth_first_search.py
# https://www.youtube.com/watch?v=HZ5YTanv5QE
