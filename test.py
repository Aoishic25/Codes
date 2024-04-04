def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in graph:
        dist[u][v] = w
        dist[v][u] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def find_largest_shortest_distance(graph):
    n, m = map(int, graph[0].split())
    graph = [list(map(int, line.split())) for line in graph[1:]]
    
    # Compute all pairs shortest paths
    dist = floyd_warshall(graph, n)
    
    max_distance = -1
    max_distance_pairs = []
    
    # Find the maximum shortest distance and corresponding pairs of vertices
    for i in range(n):
        for j in range(i+1, n):
            if dist[i][j] > max_distance:
                max_distance = dist[i][j]
                max_distance_pairs = [(i, j)]
            elif dist[i][j] == max_distance:
                max_distance_pairs.append((i, j))
    
    return max_distance_pairs, max_distance

# Read graph data from a text file
def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        graph_data = file.readlines()
    return graph_data

# Example usage with graph data from a text file
file='/Users/aoishonthgo/Downloads/graph-large.txt'  # Replace 'your_graph_data.txt' with the actual filename
graph_data = read_graph_from_file(file)
pairs, distance = find_largest_shortest_distance(graph_data)

print("For the larger graph, Pairs with maximum shortest distance:")
for pair in pairs:
    source, target = pair
    print("Source:", {source})
    print("Target:", {target})
    print("Distance:", {distance})


# Example usage with graph data from a text file
file1='/Users/aoishonthgo/Downloads/graph-small.txt'  # Replace 'your_graph_data.txt' with the actual filename
graph=read_graph_from_file(file1)
pairs, distance = find_largest_shortest_distance(graph)

print("For the smaller graph, Pairs with maximum shortest distance:")
for pair in pairs:
    source, target = pair
    print("Source:", {source})
    print("Target:", {target})
    print("Distance:", {distance})
