import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths import weighted 

G = nx.Graph()

G.clear()
G.add_nodes_from(["1","2", "3","4", "5"])
G.add_edge("1", "2", weight =5)
G.add_edge("1", "5", weight =8)
G.add_edge("1", "3", weight =4)
G.add_edge("2", "3", weight =7)
G.add_edge("2", "3", weight =8)
G.add_edge("3", "4", weight =6)
G.add_edge("4", "5", weight =5)

print(G.nodes(), G.edges())

pos = nx.spring_layout(G)
weights = nx.get_edge_attributes(G , "weight")
nx.draw_networkx(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels= weights)

plt.title("Grafos basicos con networkx")
plt.gcf().canvas.set_window_title("")
plt.show()

