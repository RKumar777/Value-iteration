# Value-iteration
Implementing reinforcement learning through value iteration method on a maze
There are four available actions 0, 1, 2, 3, at each state and they correspond to the directions “West”,
“North”, “East”, “South” respectively. 
The state the agent ends up in after taking any action at any state is deterministic: if an agent is at the initial state S and takes action 2 (East), then the next state of the agent is (1, 1). 
If the agent takes an action that would result in going into a state with an obstacle, it will instead stay in the same state. 
For example, if the agent takes action 2 (East) at state (0, 0) in the above example, the next state of the agent will still be (0, 0). 
If the agent takes an action that would result in hitting the wall, it will also stay in the same state. For example, if the agent takes action 0 (West) at state (0, 0) in the above example, the next state of the agent will still be (0, 0).
The goal of the agent is to take as few steps as possible to get to the goal state from the start state. 
Hence, the reward is −1 whenever an agent takes an action, regardless of the state at which it takes an action.

Value iteration is a planning method used when the model of the world is known. We assume that we have access to the following information about the world a priori.
• A set of states s ∈ S
• A set of actions a an agent could take at each state s ∈ S
• Transition probability T(s, a, s0): the probability of being at state s0 after taking action a at state s
• Reward function R(s, a, s0): the reward of being at state s0 after taking action a at state s

Arguments for the program include:
1. <maze input>: path to the environment input .txt described previously
2. <value file>: path to output the values V (s)
3. <q value file>: path to output the q-values Q(s, a)
4. <policy file>: path to output the optimal actions π(s)
5. <num epoch>: the number of epochs your program should train the agent for. In one epoch, your program should update the value V (s) once for each s ∈ S.
6. <discount factor>: the discount factor γ
