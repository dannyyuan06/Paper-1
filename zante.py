import itertools
import networkx as nx

# Sample directed graph
G = nx.DiGraph()  # Create a Directed Graph
edges = [
    (12, 1), (12, 2), (12, 3), (12, 4), (12, 6), (1, 12), (1, 2), (1, 3), (1, 4),
    (1, 6), (2, 5), (2, 7), (2, 8), (2, 9), (2, 6), (5, 9), (5, 7), (5, 8),
    (5, 9), (5, 6), (6, 8), (6, 12), (6, 6), (6, 3), (6, 2), (7, 5), (7, 2),
    (7, 10), (7, 6), (7, 4), (9, 5), (9, 10), (9, 8), (9, 2), (9, 6), (3, 4),
    (3, 12), (3, 6), (3, 5), (3, 2), (8, 5), (8, 10), (8, 9), (8, 2), (8, 6),
    (10, 5), (10, 8), (10, 9), (10, 2), (10, 6), (4, 12), (4, 1), (4, 3),
    (4, 7), (4, 2), (11, 2), (11, 9), (11, 7), (11, 10)
]
G.add_edges_from(edges)

# Helper function to calculate the total number of edges within subsets of the graph
def internal_edges_count(G, nodes):
    subgraph = G.subgraph(nodes)
    return subgraph.number_of_edges()

# All nodes in the graph
all_nodes = list(G.nodes)

# Best split initialization
best_split = None
max_internal_edges = -1

# Iterate over all possible combinations to split the nodes into two groups of 6
for nodes_group_1 in itertools.combinations(all_nodes, 6):
    # The second group consists of nodes not in the first group
    nodes_group_2 = tuple(set(all_nodes) - set(nodes_group_1))
    
    # Calculate the number of internal edges for both groups
    internal_edges_group_1 = internal_edges_count(G, nodes_group_1)
    internal_edges_group_2 = internal_edges_count(G, nodes_group_2)
    
    total_internal_edges = internal_edges_group_1 + internal_edges_group_2
    
    # Update best split if current split has more internal edges
    if total_internal_edges > max_internal_edges:
        max_internal_edges = total_internal_edges
        best_split = (nodes_group_1, nodes_group_2)

# Print the best split and the number of internal relationships (edges)
print("Best split:")
print("Maximum number of internal relationships:", max_internal_edges)