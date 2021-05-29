"""
In search.py, you will implement generic search algorithms
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()




def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

	print("Start:", problem.get_start_state().state)
    print("Is the start a goal?", problem.is_goal_state(problem.get_start_state()))
    print("Start's successors:", problem.get_successors(problem.get_start_state()))
    """
    "*** YOUR CODE HERE ***"
    fringe = []
    path = set()
    final = []
    acts = dict()
    state = problem.get_start_state()
    fringe.append(state)

    while(len(fringe) > 0):
        state = fringe.pop()
        path.add(state)
        states = problem.get_successors(state)
        acts[state] = states[:]
        if problem.is_goal_state(state):
            break

        #states = problem.get_successors(state)
        for stat in states:
            if stat[0] not in path and stat[0] not in fringe:
                fringe.append(stat[0])

    while(True):
        if state == problem.get_start_state():
            break
        for key, val in acts.items():
            for va in val: #( x, y, z)
                if va[0] == state:
                    final.append(va[1])
                    state = key
                    break
            else:
                continue
            break

    final.reverse()

    return final



def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    fringe = []
    path = set()
    final = []
    acts = dict()
    state = problem.get_start_state()
    fringe.append(state)

    while (True):
        state = fringe[0]
        del fringe[0]
        path.add(state)
        states = problem.get_successors(state)
        acts[state] = states[:]
        if problem.is_goal_state(state):
            break

        #states = problem.get_successors(state)
        for stat in states:
            if stat[0] not in path and stat[0] not in fringe:
                fringe.append(stat[0])

    while (True):
        if state == problem.get_start_state():
            break
        for key, val in acts.items():
            for va in val:
                if va[0] == state:
                    final.append(va[1])
                    state = key
                    break
            else:
                continue
            break

    final.reverse()

    return final


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    path = set()
    final = []
    acts = dict()
    state = problem.get_start_state()
    fringe.push(state, 0)

    while (True):
        state = fringe.pop()
        path.add(state)
        states = problem.get_successors(state)
        acts[state] = states[:]
        if problem.is_goal_state(state):
            break

        #states = problem.get_successors(state)
        # push into fringe
        for stat in states:
            if stat[0] not in path:
                fringe.push(stat[0], stat[1].piece.get_num_tiles()) #problem.get_cost_of_actions([stat[1]])

    while (True):
        if state == problem.get_start_state():
            break
        for key, val in acts.items():
            for va in val:
                if va[0] == state:
                    final.append(va[1])
                    state = key
                    break
            else:
                continue
            break

    final.reverse()

    return final


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    path = set()
    final = []
    acts = dict()
    state = problem.get_start_state()
    fringe.push(state, 0)

    while (True):
        state = fringe.pop()
        path.add(state)
        states = problem.get_successors(state)
        acts[state] = states[:]
        if problem.is_goal_state(state):
            break

        states = problem.get_successors(state)
        # push into fringe
        for stat in states:
            if stat[0] not in path:
                """
                it does worse in corners problems, to work better needs heavy huristic, not worth in
                in corners problem expandend nodes grow expo
                all others are better
                counter = 0 # in some situation it helps, in some it doesnt
                #print(stat[0].pieces)
                for x in stat[0].pieces[0]:
                    if x:
                        counter += 1
                """
                counter = 0
                fringe.push(stat[0], stat[2] + counter + heuristic(stat[0], problem))  # problem.get_cost_of_actions([stat[1]])

    while (True):

        for key, val in acts.items():
            for va in val:
                if va[0] == state:
                    final.append(va[1])
                    state = key
                    break
            else:
                continue
            break
        if state == problem.get_start_state():
            break

    final.reverse()

    return final



# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
