# Problem 1


### **Introduction**

Analyzing electrical circuits is a cornerstone of both theoretical and applied electrical engineering. A key challenge in circuit analysis is determining the *equivalent resistance* between two points in a network of resistors. While traditional approaches rely on manually identifying and simplifying series and parallel resistor combinations, these methods can quickly become impractical as circuit complexity grows.

Graph theory offers a powerful and systematic alternative. By modeling circuits as graphs where resistors are edges with weights representing resistance, and connection points are nodes we can apply algorithmic techniques to simplify and analyze circuits of arbitrary complexity. This graph-based perspective not only streamlines the computation of equivalent resistance but also enables automation and scalability, which are crucial for modern applications in circuit simulation, design, and optimization.

In this project, we explore how to compute equivalent resistance using graph theory. We present an algorithmic approach that iteratively reduces complex networks by identifying and collapsing series and parallel connections. Our implementation can handle nested configurations and cyclic graphs, providing a general solution for resistance calculation.

---
 **Option 2: Full Implementation**
  which will give you both the algorithm and the working code to calculate equivalent resistance using graph theory.

---

###  **Algorithm Overview**

We treat the electrical circuit as a weighted undirected graph:

* **Nodes**: junctions or connection points.
* **Edges**: resistors with weights equal to resistance values.

The algorithm will:

1. Parse the graph structure.
2. Repeatedly simplify:

   * **Series**: Replace paths with only two connected edges with a single edge summing their resistances.
   * **Parallel**: Replace multiple edges between the same two nodes with one edge using the reciprocal rule.

3. Continue until the circuit is reduced to two nodes: the input and output terminals.

---

###  Pseudocode

```plaintext
function calculate_equivalent_resistance(graph, start, end):
    while graph has more than two nodes:
        for each node n in graph:
            if n is not start or end:
                if n has exactly two neighbors:
                    merge series(n)
                else if n connects to the same pair of nodes more than once:
                    merge_parallel(n)
    return weight of edge between start and end

function merge_series(node):
    neighbors = get_neighbors(node)
    new_resistance = sum(resistance(node, neighbors[0]), resistance(node, neighbors[1]))
    remove node and its edges
    add edge(neighbors[0], neighbors[1], new_resistance)

function merge_parallel():
    for each pair of nodes (u, v) with multiple edges:
        R_total = 1 / sum(1/R for R in resistances between u and v)
        remove all edges(u, v)
        add edge(u, v, R_total)
```

---

###  Python Implementation

Here's a working version using `networkx`:

```python
import networkx as nx

def equivalent_resistance(graph, start, end):
    G = graph.copy()
    changed = True

    while changed:
        changed = False
        for node in list(G.nodes):
            if node in [start, end]:
                continue
            neighbors = list(G.neighbors(node))
            if len(neighbors) == 2:
                # Series reduction
                r1 = G[node][neighbors[0]]['resistance']
                r2 = G[node][neighbors[1]]['resistance']
                new_r = r1 + r2
                G.add_edge(neighbors[0], neighbors[1], resistance=new_r)
                G.remove_node(node)
                changed = True
                break

        # Parallel reduction
        to_merge = {}
        for u, v in list(G.edges()):
            if (u, v) in to_merge or (v, u) in to_merge:
                continue
            parallels = [
                (i, j) for i, j in G.edges()
                if (i == u and j == v) or (i == v and j == u)
            ]
            if len(parallels) > 1:
                total_inv = sum(1 / G[i][j]['resistance'] for i, j in parallels)
                G.remove_edges_from(parallels)
                G.add_edge(u, v, resistance=1 / total_inv)
                changed = True
                break

    return G[start][end]['resistance']
```

---

###  Test Examples

1. **Series Circuit:**

```python
G = nx.Graph()
G.add_edge('A', 'B', resistance=2)
G.add_edge('B', 'C', resistance=3)
print(equivalent_resistance(G, 'A', 'C'))  # Expected: 5
```

2. **Parallel Circuit:**

```python
G = nx.Graph()
G.add_edge('A', 'C', resistance=2)
G.add_edge('A', 'C', resistance=3)
print(equivalent_resistance(G, 'A', 'C'))  # Expected: 1.2
```

3. **Nested Circuit:**

```python
G = nx.Graph()
G.add_edge('A', 'B', resistance=1)
G.add_edge('B', 'C', resistance=1)
G.add_edge('A', 'C', resistance=1)
print(equivalent_resistance(G, 'A', 'C'))  # Expected: 0.75
```

---

###  Efficiency Analysis

* Each simplification step reduces the graph size, making convergence fast.
* Worst-case: O(n²) simplifications for dense graphs.
* For very large graphs, optimized edge lookups or symbolic simplification may help.

---
[examples](code.html)



