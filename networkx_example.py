# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:34:52 2018

@author: laman
"""

%matplotlib inline
import networkx as nx

# define an empty network variable G
G = nx.Graph()

# make a for loop from 0 to 49
for i in range(50):
    print('Loop number %d' % i)
    # add a node named i
    G.add_node(i)

# visualize 50 nodes in the network variable G
pos = nx.spring_layout(G)
nx.draw_networkx_edges(G, pos, alpha=1);
nx.draw_networkx_nodes(G, pos, node_size=50);

# make a for loop from 0 to 99
for i in range(100):
    print('Loop number %d' % i)
    # generate two random numbers from 0 to 49
    randint_1, randint_2 = random.randint(0, 50), random.randint(0, 50)

    print('Random numbers are {0} and {1}'.
          format(randint_1, randint_2))

    # add an edge using the generated random number pair
    G.add_edge(randint_1, randint_2)

# visualize nodes and edges in the variable G using spring algorithm
pos = nx.spring_layout(G)
nx.draw_networkx_edges(G, pos, alpha=1);
nx.draw_networkx_nodes(G, pos, node_size=50);