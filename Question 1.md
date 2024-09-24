# Question 1: Algorithm Analysis

| Algorithm | Time Complexity       | Space Complexity    | Complete?                                           | Optimal?                                      |
|-----------|-----------------------|---------------------|-----------------------------------------------------|-----------------------------------------------|
| **BFS**   | O(b^(d+1))            | O(b^(d+1))          | Yes (if the branching factor b is finite)            | Yes (uniform cost), No (different costs)      |
| **UCS**   | O(b^{1 + \frac{C}{\epsilon}})
          | O(b^(1+C/ε))        | Yes                                                 | Yes                                           |
| **DFS**   | O(b^n)                | O(bn)              | Yes (finite graph), No (infinitely large)            | No                                            |
| **DLS**   | O(b^l)                | O(bl)              | Yes (if the solution is above the depth-limit), No (otherwise) | No                                            |
| **IDS**   | O(b^d)                | O(bd)              | Yes                                                 | Yes                                           |
| **A\***   | O(b^d)                | O(b^d)              | Yes                                                 | Yes (when heuristic is admissible)            |


**BFS**  
b - branching factor  
d - depth of the solution  

**UCS**  
b - branching factor  
C - cost of the optimal solution   
ε - minimum cost between any two states  

**DFS**   
n - depth of the search tree  

**DLS**  
l - depth limit  