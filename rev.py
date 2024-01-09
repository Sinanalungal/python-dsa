
def dfs(node,start,visited=None):
    if visited is None:
        visited=set()
    
    if start not in visited:
        print(start,end='   ')
        visited.add(start)
        for i in node[start]:
            dfs(i,visited)
        