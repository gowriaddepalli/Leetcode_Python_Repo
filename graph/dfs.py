# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
graph = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [],
}

def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s)

        # reverse iterate through edge list so results match recursive version
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                stack.append(n)

def main():
    dfs(graph, 'A')

main()



