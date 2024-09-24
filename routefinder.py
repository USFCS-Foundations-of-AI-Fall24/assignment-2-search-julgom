from queue import PriorityQueue
from Graph import Graph, Node, Edge
import math


class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'
    
    def neighbors(self, heuristic_fn):
        neighbors = []
        for edge in self.mars_graph.get_edges(Node(self.location)):
            neighbor_location = edge.dest.value
            neighbor = map_state(neighbor_location, self.mars_graph, prev_state = self)
            neighbor.g = self.g + edge.val
            neighbor.h = heuristic_fn(neighbor)
            neighbor.f = neighbor.g + neighbor.h
            neighbors.append(neighbor)
        return neighbors


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True):
    search_queue = PriorityQueue()
    closed_list = {}
    state_count = 1

    search_queue.put(start_state)
    closed_list[start_state] = True

    while not search_queue.empty():
        current_state = search_queue.get()

        if goal_test(current_state):
            print("Goal found")
            #ptr = current_state
            #while ptr.location != '8,8': 
            #    ptr = ptr.prev_state
            #    print(ptr.location,"\n")
            return current_state, state_count
       
        else :
            neighbors = current_state.neighbors(heuristic_fn)
            if use_closed_list :
                neighbors = [neighbor for neighbor in neighbors
                                    if neighbor not in closed_list]
                
                for neighbor in neighbors :
                    closed_list[neighbor] = True
                    search_queue.put(neighbor)
                    
            state_count += len(neighbors)
            
    return None, state_count

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state):
    # Extract current position from state
    x, y = map(int, state.location.split(','))
    goal_x, goal_y = 1, 1
    
    # Compute the straight-line distance
    distance = math.sqrt((x - goal_x) ** 2 + (y - goal_y) ** 2)
    return distance


## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    mars_graph = Graph()
    
    with open(filename, 'r') as file:
        for line in file:
            # Remove any trailing newline or space characters
            line = line.strip()
            if not line:
                continue
                
            # Split the line into the node and its edges
            src, dest_str = line.split(':')
            src = src.strip()
            src_node = Node(src)

            # Add node to the graph if it doesn't exist
            mars_graph.add_node(src_node)
            
            # Split edges and add to the graph
            dests = dest_str.split()
            for dest in dests:
                dest = dest.strip()
                dest_node = Node(dest)
                edge = Edge(src_node, dest_node, 1)
                mars_graph.add_edge(edge)
    
    return mars_graph

if __name__ == "__main__":
    mars_graph = read_mars_graph("MarsMap")

    # Set starting location (e.g., "8, 8")
    start_location = "8,8"

    start_state_ucs = map_state(start_location, mars_graph)
    start_state_ucs.h = h1(start_state_ucs)
    start_state_ucs.f = start_state_ucs.g + start_state_ucs.h

    start_state_astar = map_state(start_location, mars_graph)
    start_state_astar.h = sld(start_state_astar)
    start_state_astar.f = start_state_astar.g + start_state_astar.h

    # Define the goal test
    goal_test = lambda state: state.is_goal()

    # Run Uniform Cost Search (UCS)
    print("Running Uniform Cost Search (UCS):")
    final_state_ucs, states_generated_ucs = a_star(start_state_ucs, h1, goal_test)
    print(f"UCS Result: {final_state_ucs}")
    print(f"Total states generateds for UCS: {states_generated_ucs}")

    # Run A* search with the straight-line distance heuristic
    print("\nRunning A* Search:")
    final_state_astar, states_generated_astar = a_star(start_state_astar, sld, goal_test)
    print(f"A* Result: {final_state_astar}")
    print(f"Total states generated for A*: {states_generated_astar}")
    print("-----------------------------------------------------")

