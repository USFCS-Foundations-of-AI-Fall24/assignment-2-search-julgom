# Algorithm Analysis

| Algorithm | Time Complexity               | Space Complexity              | Complete?                                       | Optimal?                                      |
|-----------|-------------------------------|-------------------------------|-------------------------------------------------|-----------------------------------------------|
| BFS       | O(b^(d+1)), b - branching factor, d - depth of the solution                   | O(b^(d+1))                    | Yes (if the branching factor \(b\) is finite) | Yes (uniform cost), No (different costs)     |
| UCS       | O(b^(1+C/ε)), b - branching factor, C - cost of the optimal solution, ε - minimum cost between any two states
                 | O(b^(1+C/ε))                  | Yes                                             | Yes                                           |
| DFS       | O(b^n), n - depth of the
search tree
                       | O(b^n)                       | Yes (finite graph), No (infinitely large)      | No                                            |
| DLS       | O(b^l), l - depth limit                       | O(b^l)                       | Yes (if the solution is above the depth-limit), No (otherwise) | No                               |
| IDS       | O(b^d)                       | O(b^d)                       | Yes                                             | Yes                                           |
| A*        | O(b^d)                       | O(b^d)                       | Yes                                             | Yes (when heuristic is admissible)           |
