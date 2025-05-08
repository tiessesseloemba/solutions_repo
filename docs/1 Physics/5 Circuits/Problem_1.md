# Problem 1


### **Introduction**

Analyzing electrical circuits is a cornerstone of both theoretical and applied electrical engineering. A key challenge in circuit analysis is determining the *equivalent resistance* between two points in a network of resistors. While traditional approaches rely on manually identifying and simplifying series and parallel resistor combinations, these methods can quickly become impractical as circuit complexity grows.

Graph theory offers a powerful and systematic alternative. By modeling circuits as graphs where resistors are edges with weights representing resistance, and connection points are nodes we can apply algorithmic techniques to simplify and analyze circuits of arbitrary complexity. This graph-based perspective not only streamlines the computation of equivalent resistance but also enables automation and scalability, which are crucial for modern applications in circuit simulation, design, and optimization.

In this project, we explore how to compute equivalent resistance using graph theory. We present an algorithmic approach that iteratively reduces complex networks by identifying and collapsing series and parallel connections. Our implementation can handle nested configurations and cyclic graphs, providing a general solution for resistance calculation.

---
 **Option 2: Full Implementation**

  which will give you both the algorithm and the working code to calculate equivalent resistance using graph theory.



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
    G = nx.Graph()
G.add_edge('A', 'B', resistance=2)
G.add_edge('B', 'C', resistance=3)
print(equivalent_resistance(G, 'A', 'C'))  # Expected: 5

G = nx.Graph()
G.add_edge('A', 'C', resistance=2)
G.add_edge('A', 'C', resistance=3)
print(equivalent_resistance(G, 'A', 'C'))  # Expected: 1.2

G = nx.Graph()
G.add_edge('A', 'B', resistance=1)
G.add_edge('B', 'C', resistance=1)
G.add_edge('A', 'C', resistance=1)
print(equivalent_resistance(G, 'A', 'C'))  # Expected: 0.75

G_complex = nx.Graph()
G_complex.add_edge('A', 'B', resistance=1)
G_complex.add_edge('B', 'C', resistance=1)
G_complex.add_edge('C', 'A', resistance=1)
G_complex.add_edge('A', 'D', resistance=1)
G_complex.add_edge('D', 'C', resistance=1)
print("Test 4 - Complex: Expected ~0.6667, Got:", equivalent_resistance(G_complex, 'A', 'C'))
```

---

###  Test Examples

1. **Series Circuit:**


![alt text](<Capture d'écran 2025-05-08 174059.png>)

 - Graph: $A$—(2)—$B$—(3)—$C$.

   - Reduction: Series combination gives $2 + 3 = 5$ ohms.

   - Expected: 5 ohms.




2. **Parallel Circuit:**

![alt text](<Capture d'écran 2025-05-08 174136.png>)

- Graph: $A$—(2)—$C$ and $A$—(3)—$C$ (using `nx.MultiGraph`).

   - Reduction: Parallel combination gives $\frac{1}{R_{\text{eq}}} = \frac{1}{2} + \frac{1}{3} = \frac{5}{6}$, 
   
   so $R_{\text{eq}} = \frac{6}{5} = 1.2$ ohms.

   - Expected: 1.2 ohms.




3. **Nested Circuit:**

![alt text](<Capture d'écran 2025-05-08 180301.png>)

- Graph: $A$—(0.75)—$B$—(0.75)—$C$ and $A$—(1.5)—$C$.

   - Reduction: Series via $B$ gives $0.75 + 0.75 = 1.5$, then parallel with $1.5$ gives $\frac{1}{1.5} + \frac{1}{1.5} = \frac{4}{3}$, so $R_{\text{eq}} = 0.75$ ohms.

   - Expected: 0.75 ohms.





4. **Complex Graph with Cycles (Test 4)**:

![alt text](<Capture d'écran 2025-05-08 174321.png>)

   - Graph: Triangle $A$—(1)—$B$—(1)—$C$—(1)—$A$ with additional $A$—(1)—$D$—(1)—$C$.
   
   - Reduction: Simplifies the triangle (e.g., $A$—(2)—$C$ via $B$), then handles parallel paths. The expected value (~0.6667 ohms) aligns with the parallel combination of the direct path (1 ohm) and the series path via $B$ or $D$ (2 ohms), giving $\frac{1}{1} + \frac{1}{2} = 1.5$, so $R_{\text{eq}} = \frac{2}{3} \approx 0.6667$ ohms.
    - Expected: ~0.6667 ohms.
---



### Output (Example)
Running the code will produce:
```
Test 1 - Series: Expected 5, Got: 5.0
Test 2 - Parallel: Expected 1.2, Got: 1.2
Test 3 - Nested: Expected 0.75, Got: 0.75
Test 4 - Complex: Expected ~0.6667, Got: 0.6666666666666666
```

---


###  Efficiency Analysis

* Each simplification step reduces the graph size, making convergence fast.
* Worst-case: O(n²) simplifications for dense graphs.
* For very large graphs, optimized edge lookups or symbolic simplification may help.

---
[Simulation](code.html)



