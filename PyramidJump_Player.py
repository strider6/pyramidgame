class PyramidJump_Player:
    def __init__(self) -> None:
        self.all_states = [0]*(2**15)
        print ("start my program")
        number = 15
        binary_string = bin(number)[2:]
        binary_list = list(binary_string)
        print("the result is:")
        print (binary_list)

    def convert_number_to_state(self, number):
        pass

    def convert_state_to_number(self, state):
        pass
        
# test_instace = PyramidJump_Player()
        
print("Testing if this works")      
        
my_player = PyramidJump_Player()

