## actions:
## pick up tool
## move_to_sample
## use_tool
## move_to_station
## drop_tool
## drop_sample
## move_to_battery
## charge

## locations: battery, sample, station
## holding_sample can be True or False
## holding_tool can be True or False
## Charged can be True or False

from copy import deepcopy
from search_algorithms import breadth_first_search
from search_algorithms import depth_first_search
from search_algorithms import depth_limited_search

class RoverState :
    def __init__(self, loc="station", sample_extracted=False, holding_sample=False, charged=False, holding_tool=False):
        self.loc = loc
        self.sample_extracted=sample_extracted
        self.holding_sample = holding_sample
        self.charged=charged
        self.holding_tool=holding_tool
        self.prev = None

    ## you do this.
    def __eq__(self, other):
       return (self.loc == other.loc and
                self.sample_extracted == other.sample_extracted and
                self.holding_sample == other.holding_sample and
                self.charged == other.charged and
                self.holding_tool == other.holding_tool)


    def __repr__(self):
        return (f"Location: {self.loc}\n" +
                f"Sample Extracted?: {self.sample_extracted}\n"+
                f"Holding Sample?: {self.holding_sample}\n" +
                f"Charged? {self.charged}\n" +
                f"Holding Tool? {self.holding_tool}")

    def __hash__(self):
        return self.__repr__().__hash__()

    def successors(self, list_of_actions):

        ## apply each function in the list of actions to the current state to get
        ## a new state.
        ## add the name of the function also
        succ = [(item(self), item.__name__) for item in list_of_actions]
        ## remove actions that have no effect

        succ = [item for item in succ if not item[0] == self]
        return succ

## our actions will be functions that return a new state.

def move_to_sample(state) :
    r2 = deepcopy(state)
    r2.loc = "sample"
    r2.prev=state
    return r2

def move_to_station(state) :
    r2 = deepcopy(state)
    r2.loc = "station"
    r2.prev = state
    return r2

def move_to_battery(state) :
    r2 = deepcopy(state)
    r2.loc = "battery"
    r2.prev = state
    return r2
# add tool functions here

def pick_up_tool(state):
    r2 = deepcopy(state)
    if state.loc == "station":
        r2.holding_tool = True
    r2.prev = state
    return r2

def drop_tool(state):
    r2 = deepcopy(state)
    if state.loc == "station":
        r2.holding_tool = False
    r2.prev = state
    return r2

def use_tool(state):
    r2 = deepcopy(state)
    if state.holding_tool and state.loc == "sample": 
        r2.sample_extracted = True
    r2.prev = state
    return r2

def pick_up_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "sample":
        r2.holding_sample = True
    r2.prev = state
    return r2

def drop_sample(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and state.loc == "station":
        r2.holding_sample = False
    r2.prev = state
    return r2

def charge(state) :
    r2 = deepcopy(state)
    if state.sample_extracted and not state.holding_sample and not state.holding_tool and state.loc == "battery":
        r2.charged = True
    r2.prev = state
    return r2

'''
action_list = [charge, drop_sample, pick_up_sample,
               move_to_sample, move_to_battery, move_to_station]

'''
action_list = [pick_up_tool, move_to_sample, use_tool, 
               pick_up_sample, move_to_station, drop_sample, 
               drop_tool, move_to_battery, charge]

action_list_1 = [pick_up_tool, move_to_sample]

action_list_2 = [use_tool, pick_up_sample]

action_list_3 = [move_to_station, drop_sample, drop_tool,
                move_to_battery, charge]

def battery_goal(state) :
    return state.loc == "battery"
## add your goals here.

def mission_complete(state) :
    return state.loc == "battery" and state.charged and state.sample_extracted 

# Subproblem 1: Move to Sample (with tool)
def goal_move_to_sample(state):
    return state.loc == "sample" and state.holding_tool

# Subproblem 2: Remove Sample (extract and hold)
def goal_remove_sample(state):
    return state.loc == "sample" and state.sample_extracted 

# Subproblem 3: Return to Charger (drop tool/sample, charge)
def goal_return_to_charger(state):
    return state.loc == "battery" and state.charged and state.sample_extracted and not state.holding_sample and not state.holding_tool

if __name__=="__main__" :
  
    s = RoverState()
   
    print("Running Breadth-First Search:")
    final_state_bfs, states_generated_bfs = breadth_first_search(s, action_list, mission_complete)
    print(f"Total states for BFS: {states_generated_bfs}")

    print("\nRunning Depth-First Search:")
    final_state_dfs, states_generated_dfs = depth_first_search(s, action_list, mission_complete)
    print(f"Total states for DFS: {states_generated_dfs}")

    print("\nRunning Depth-Limited Search:")
    final_state_dls, states_generated_dls = depth_limited_search(s, action_list, mission_complete, limit=7)
    print(f"Total states for DLS: {states_generated_dls}")
    print("-----------------------------------------------------")

    
    initial_state = RoverState()

    print("\nDECOMPOSITION: BFS")
    # Subproblem 1: Move to sample (with tool)
    print("\nRunning Breadth-First Search for Subproblem 1: (Move to Sample)")
    result_bfs_s1, states_generated_bfs_1 = breadth_first_search(initial_state, action_list_1, goal_move_to_sample)
    print(f"Generated states (BFS) for Subproblem 1: {states_generated_bfs_1}")

    #print(result_bfs_s1[0].prev)
    result_bfs_s1[0].prev = None
    # Subproblem 2: Remove sample
    print("\nRunning Breadth-First Search for Subproblem 2: (Remove Sample)")
    result_bfs_s2, states_generated_bfs_2 = breadth_first_search(result_bfs_s1[0], action_list_2, goal_remove_sample)
    print(f"Generated states (BFS) for Subproblem 2: {states_generated_bfs_2}")

    result_bfs_s2[0].prev = None
    # Subproblem 3: Return to charger (drop tool/sample, charge)
    print("\nRunning Breadth-First Search for Subproblem 3: (Return to Charger)")
    result_bfs_s3, states_generated_bfs_3 = breadth_first_search(result_bfs_s2[0], action_list_3, goal_return_to_charger)
    print(f"Generated states (BFS) for Subproblem 3: {states_generated_bfs_3}")
    print(f"Total states generated by decomposition for BFS: {states_generated_bfs_1 + states_generated_bfs_2 + states_generated_bfs_3}")
    print("-----------------------------------------------------")

    print("\nDECOMPOSITION: DFS")
    # Subproblem 1: Move to sample (with tool)
    print("\nRunning Depth-First Search for Subproblem 1: (Move to Sample)")
    result_dfs_s1, states_generated_dfs_1 = depth_first_search(initial_state, action_list_1, goal_move_to_sample)
    print(f"Generated states (DFS) for Subproblem 1: {states_generated_dfs_1}")

    result_dfs_s1[0].prev = None
    # Subproblem 2: Remove sample
    print("\nRunning Depth-First Search for Subproblem 2: Remove Sample)")
    result_dfs_s2, states_generated_dfs_2 = depth_first_search(result_dfs_s1[0], action_list_2, goal_remove_sample)
    print(f"Generated states (DFS) for Subproblem 2: {states_generated_dfs_2}")

    result_dfs_s2[0].prev = None
    # Subproblem 3: Return to charger (drop tool/sample, charge)
    print("\nRunning Depth-First Search for Subproblem 3: (Return to Charger)")
    result_dfs_s3, states_generated_dfs_3 = depth_first_search(result_dfs_s2[0], action_list_3, goal_return_to_charger)
    print(f"Generated states (DFS) for Subproblem 3: {states_generated_dfs_3}")
    print(f"Total states generated by decomposition for DFS: {states_generated_dfs_1 + states_generated_dfs_2 + states_generated_dfs_3}")
    print("-----------------------------------------------------")


    print("\nDECOMPOSITION: DLS")
    # Subproblem 1: Move to sample (with tool)
    print("\nRunning Depth-Limited Search for Subproblem 1: (Move to Sample)")
    result_dls_s1, states_generated_dls_1 = depth_limited_search(initial_state, action_list_1, goal_move_to_sample, limit=2)
    print(f"Generated states (DLS) for Subproblem 1: {states_generated_dls_1}")

    result_dls_s1[0].prev = None
    # Subproblem 2: Remove sample
    print("\nRunning Depth-Limited Search for Subproblem 2: (Remove Sample)")
    result_dls_s2, states_generated_dls_2 = depth_limited_search(result_dls_s1[0], action_list_2, goal_remove_sample, limit=1)
    print(f"Generated states (DLS) for Subproblem 2: {states_generated_dls_2}")

    result_dls_s2[0].prev = None
    # Subproblem 3: Return to charger (drop tool/sample, charge)
    print("\nRunning Depth-Limited Search for Subproblem 3: (Return to Charger)")
    result_dls_s3, states_generated_dls_3 = depth_limited_search(result_dls_s2[0], action_list_3, goal_return_to_charger, limit=4)
    print(f"Generated states (DLS) for Subproblem 3: {states_generated_dls_3}")
    print(f"Total states generated by decomposition for DLS: {states_generated_dls_1 + states_generated_dls_2 + states_generated_dls_3}")
    print("-----------------------------------------------------")

    