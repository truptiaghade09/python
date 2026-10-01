def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def greedy_mst(vertices, edges):
    edges.sort(key=lambda x: x[2])
    parent = list(range(vertices))
    rank = [0] * vertices
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == vertices - 1:
                break

    return mst, total_cost


v = int(input("Enter the nodes: "))
e = int(input("Enter the edges: "))

edges = []
print("Enter each edge (u v weight):")
for _ in range(e):
    u, vtx, w = map(int, input().split())
    edges.append((u, vtx, w))


mst, cost = greedy_mst(v, edges)

print("\nNodes:")
for i in range(v):
    print(i, end=" ")
print()

print("\nEdges:")
for u, vtx, w in edges:
    print(u, "--", vtx, "weight:", w)

print("\nMST:")
for u, vtx, w in mst:
    print(u, "--", vtx, "weight:", w)

print("\nTotal Cost:", cost)
