class PyramidJump_Player:
    def __init__(self) -> None:
        self.value_function = [0]*(2**15)

    def convert_number_to_state(self, number):
        binary_string = bin(number)[2:]
        pl = 15 - len(binary_string)
        binary_string = "0" * pl + binary_string 
        return list(binary_string)

    def convert_state_to_number(self, state):
         return int("".join(state), 2)
     
        
print("Testing if this works")      
my_player = PyramidJump_Player()

test_state = ['0', '0', '0', '0', '1', '1', '1', '0','0','1','1','1','0','0','1']
idx = my_player.convert_state_to_number(test_state)

print(f"The value of state {test_state} is {my_player.value_function[idx]}")

print(idx)
converted_state = my_player.convert_number_to_state(idx)
print(converted_state == test_state) 