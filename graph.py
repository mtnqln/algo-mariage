import networkx as nx

def solve_with_graph(people:list[str],
                     positions:list[tuple[str,str,float]],
                     num_per_tables:int):
    # Build graph
    G = nx.Graph(people) # nodes
    G.add_weighted_edges_from(positions) # weighted edges
