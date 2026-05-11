INF = int(1e9 + 7)

def floyd_warshall(dist, length):
		### added code
    # Initialize 'next' matrix for path reconstruction
    next_node = [[None] * length for _ in range(length)]
    
    # If there's a direct edge, the next hop from p to q is q itself
    for p in range(length):
        for q in range(length):
            if dist[p][q] != INF and p != q:
                next_node[p][q] = q # reset next_node 
		###
		
    # Main Floyd-Warshall loop — modified min to also track path
    for r in range(length):
        for p in range(length):
            for q in range(length):
	            
	            ### modified code
                if dist[p][r] + dist[r][q] < dist[p][q]:
                # routing r is
                    dist[p][q] = dist[p][r] + dist[r][q]
                    next_node[p][q] = next_node[p][r]  
							###
							
    print_dist(dist, length)
    return next_node

### added code
def shortest_path(next_node, start, dst):
    # Reconstruct the full path from start to dst.
    if next_node[start][dst] is None:
        return []  # No path exists
    path = [start]
    while start != dst:
        start = next_node[start][dst]
        path.append(start)
    return path
###

def print_dist(dist, length):
    for p in range(length):
        temp = ""
        for q in range(length):
            if dist[p][q] == INF:
                temp += "INF "
            else:
                temp += str(dist[p][q]) + " "
        print(temp)

# Step 2
W = [
    [0,   3,   INF, 7  ],
    [8,   0,   2,   INF],
    [5,   INF, 0,   1  ],
    [2,   INF, INF, 0  ]
]

length = 4
next_node = floyd_warshall(W, length)

# Step 3
print("\nShortest path from v1 to v3:", shortest_path(next_node, 1, 3))
print("Shortest path from v0 to v2:", shortest_path(next_node, 0, 2))