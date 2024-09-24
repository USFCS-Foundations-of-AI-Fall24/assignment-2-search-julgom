# Question 1: Algorithm Analysis

| Algorithm | Time Complexity       | Space Complexity    | Complete?                                           | Optimal?                                      |
|-----------|-----------------------|---------------------|-----------------------------------------------------|-----------------------------------------------|
| **BFS**   | O(b^(d+1))            | O(b^(d+1))          | Yes (if the branching factor b is finite)            | Yes (uniform cost), No (different costs)      |
| **UCS**   | O(b^(1+C/ε))          | O(b^(1+C/ε))        | Yes                                                 | Yes                                           |
| **DFS**   | O(b^n)                | O(b^n)              | Yes (finite graph), No (infinitely large)            | No                                            |
| **DLS**   | O(b^l)                | O(b^l)              | Yes (if the solution is above the depth-limit), No (otherwise) | No                                            |
| **IDS**   | O(b^d)                | O(b^d)              | Yes                                                 | Yes                                           |
| **A\***   | O(b^d)                | O(b^d)              | Yes                                                 | Yes (when heuristic is admissible)            |
