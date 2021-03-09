###############################################
### CMPLXSYS425 - Evolution in silico       ###
### Lab 4.1 -- GP 1.0                       ###
### ####################################### ###

import numpy as np
from matplotlib import pyplot

# This is the code from the Jupyter Notebook 

# Base Class for our GP Node objects
class GPNode:
    def __init__(self, node_type=None):
        self.parent = None
        self.node_type = node_type
        self.children = []
        self.depth = 0

    def add_child(self, child_node):
        child_node.depth = self.depth+1
        self.children.append(child_node)
        child_node.parent = self

# Const Nodes hold a constant value
class GPConstNode(GPNode):
    def __init__(self, value=None):
        super().__init__(node_type="Const")
        self.const_value = value
    
    def evaluate(self, input_state):
        return self.const_value
        
    def pretty_print(self, indents=0):
        print('  '*indents + str(self.const_value) 
              + ' : ' + str(self.depth))
        
    def deepcopy(self):
        new_node = GPConstNode(value=self.const_value)
        new_node.depth = self.depth;
        return new_node
        
# Variable node
class GPVariableNode(GPNode):
    def __init__(self, variable_name=None):
        super().__init__(node_type="Variable")
        self.variable_name = variable_name
    
    def evaluate(self, input_state):
        return input_state[self.variable_name]
    
    def pretty_print(self, indents=0):
        print('  '*indents + str(self.variable_name)
              + ' : ' + str(self.depth))
        
    def deepcopy(self):
        new_node = GPVariableNode(variable_name = self.variable_name)
        new_node.depth = self.depth
        return new_node

## Brief test!
var_node = GPVariableNode(variable_name='x')
var_node.pretty_print()
print(var_node.evaluate({'x':42, 'y':128}))


# We can programatically query the value of our expression tree over a range
# of values for x! 
values = [var_node.evaluate({'x':x_val}) for x_val in range(100)]
pyplot.plot(values)
pyplot.show()



### ####################################### ###
# Bring in the Addition function node, and make sure it's working
# before going on and trying to build up the more complicated expression
# trees! 
### ####################################### ###