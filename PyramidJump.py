import os
from queue import Empty
import random
import this



class PyramidJump:
    def __init__(self) -> None:

        self.state = ["1"]*15

        self.action_dict = {"f0t3": {"from": 0, "to": 3, "skip": 1}, "f0t5": {"from": 0, "to": 5, "skip": 2}, # actions for state 0
                            "f1t6": {"from": 1, "to": 6, "skip": 3}, "f1t8": {"from": 1, "to": 8, "skip": 4}, # actions for state 1
                            "f2t7": {"from": 2, "to": 7, "skip": 4}, "f2t9": {"from": 2, "to": 9, "skip": 5}, # actions for state 2
                            "f3t0": {"from": 3, "to": 0, "skip": 1}, "f3t5": {"from": 3, "to": 5, "skip": 4}, "f3t10": {"from": 3, "to": 10, "skip": 6}, "f3t12": {"from": 3, "to": 12, "skip": 7}, # actions for state 3
                            "f4t11": {"from": 4, "to": 11, "skip": 7}, "f4t13": {"from": 4, "to": 13, "skip": 8}, # actions for state 4
                            "f5t0": {"from": 5, "to": 0, "skip": 1}, "f5t3": {"from": 5, "to": 3, "skip": 4}, "f5t12": {"from": 5, "to": 12, "skip": 8}, "f5t14": {"from": 5, "to": 14, "skip": 9}, # actions for state 5
                            "f6t1": {"from": 6, "to": 1, "skip": 3}, "f6t8": {"from": 6, "to": 8, "skip": 7}, # actions for state 6
                            "f7t2": {"from": 7, "to": 2, "skip": 4}, "f7t9": {"from": 7, "to": 9, "skip": 8}, # actions for tate 7 
                            "f8t1": {"from": 8, "to": 1, "skip": 4}, "f8t6": {"from": 8, "to": 6, "skip": 7}, # actions for state 8
                            "f9t2": {"from": 9, "to": 2, "skip": 5}, "f9t7": {"from": 9, "to": 7, "skip": 8}, # actions for state 9
                            "f10t3": {"from": 10, "to": 3, "skip": 6}, "f10t12": {"from": 10, "to": 12, "skip": 11}, # actions for state 10
                            "f11t4": {"from": 11, "to": 4, "skip": 7}, "f11t13": {"from": 11, "to": 13, "skip": 12}, # actions for state 11
                            "f12t10": {"from": 12, "to": 10, "skip": 11}, "f12t3": {"from": 12, "to": 3, "skip": 7}, "f12t5": {"from": 12, "to": 5, "skip": 8}, "f12t14": {"from": 12, "to": 14, "skip": 13}, # actions for state 12
                            "f13t5": {"from": 14, "to": 5, "skip": 9}, "f13t11": {"from": 13, "to": 11, "skip": 12}, # actions for state 13
                            "f14t5": {"from": 14, "to": 5, "skip": 9}, "f14t12": {"from": 14, "to": 12, "skip": 13}, "f5t12": {"from": 5, "to": 12, "skip": 8}, "f5t14": {"from": 5, "to": 14, "skip": 9}, # actions for state 14
                           }

        empty_pos = random.randint(0, 14)

        self.state[empty_pos] = "0"

        self.total_reward = 100


    def get_reward(self):
        self.total_reward = 100

        howMany = 0

        for s in self.state:
            if s == "1": 
                howMany += 1
                
        if howMany == 1:
            print ("You Won.")
            return self.total_reward
        return 0
            
         
    def print_board(self):

        print (f"     {self.state[0]}")
        print (f"    {self.state[1]} {self.state[2]}")
        print (f"   {self.state[3]} {self.state[4]} {self.state[5]}")
        print (f"  {self.state[6]} {self.state[7]} {self.state[8]} {self.state[9]}")
        print (f" {self.state[10]} {self.state[11]} {self.state[12]} {self.state[13]} {self.state[14]}")

# Check that the action is valid
    def is_action_valid(self, action):
        if self.state[action["from"]] == "1" and self.state[action["skip"]] == "1" and self.state[action["to"]] == "0": # add check skip and to
            return True
        else:
            return False

    def perform_action(self, action):

        self.state[action["from"]] = "0"
        self.state[action["skip"]] = "0"
        self.state[action["to"]] = "1"


    def step(self, action):
        if action not in self.action_dict:
            print("That is not a valid move.")
            return 0, self.state, False

        action = self.action_dict[action]
        print(action)
       
        # use action to change state aka "perform_action"
        if not self.is_action_valid(action):
            print("That is not a valid move.")
            return 0, self.state, False
        self.perform_action(action)
        # Return with all necessary outputs
        # Check if we're done
        return self.get_reward(), self.state, self.over()


    def over(self):
        # 1. Loop over all actions
        for action in self.action_dict.values():
            # a. check if any are valid
            if self.is_action_valid(action):
                return False 
        return True

   
if __name__ == "__main__":
    game = PyramidJump()
    game.print_board()

    done = False

    while not done:

        action = input("Where would you like to go?")

        reward, state, done = game.step(action)

        game.print_board()

    print(f"Reward gained = {reward}")
        
   