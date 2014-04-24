Implementation of algorithm to find the top k influentials for weighted graphs, incorporating the concept of time stamps:
In this algorithm , we have considered edges with weights, where weight is the frequency of communication between the two nodes. For each node we find the number of nodes it can influence in one time stamp. For example if A and B have an edge weighted x, the time needed by A to influence B is 1/x.

REQUIREMENTS
------------
Python, along with the Python libarary Networkx.


ASSUMPTIONS
-----------
Right now, we have only considered #timestamps = 1, i.e. here, K=1.

INPUT FORMAT
------------
This program takes as input a weighted social network graph where the weights on the edges denote the frequency of communication between two nodes. The graph is to be given as input in a text file. 
The format of the text file is as follows- Each line contains three space-separated fields. The first and second fields represent node IDs, while the third field represents the weight on the edge between those two nodes.

OUTPUT
------
This program prints the node IDs of the nodes being added, at each step, to the set of seed nodes which would eventually spread the influence to the entire graph. We can call this the dominating set.

ALGORITHM
---------
Phase 1: For each node, we use controlled iterative DFS to find the number of nodes it will influence. We do this by proceeding until the summation of the time taken to reach that node does not exceed one time stamp. This assumption of one timestamp is temporary. We intend to extend it to multiple timestamps.

Phase 2: Initially all the nodes are white, when one node is influenced, we change its colour to grey and, when we make one node the seed, we make it black. We begin with the node that has the maximum influence, colour it black, and colour all the nodes that it can influence grey. Next we choose a non-black node which can influence the maximum white nodes and continue in the similar fashion. Finally the set of black nodes is our dominating set.
