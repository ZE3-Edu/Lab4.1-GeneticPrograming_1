# Evolution *in silico* Lab 4.1 - Genetic Programing pt 1
## Overview
In this lab, you'll start developing a genetic programing framework. We'll build it up slowly, starting with making a few **nodes** for our expression trees (i.e., programs).

We will add two different kinds of *terminal* nodes (sometimes also called leaf nodes), one that holds a constant value (like π), and one that represents a variable. Like in the lecture, variables can take on values programatically. If that doesn't make sense, hopefully it will after looking through the Jupyter notebook! 

Next, you'll start playing with function nodes. These are only slightly more complicated than variable nodes, since they will have arguments. Arguments are *children* nodes that we connect to the function node. Already, with just these few types of nodes, we can build up arbitrarily large expression trees.

## What to do
#### First Steps
After you've understood the bits of code already provided, add the function nodes required to build up the following expressions:

- x^2
- max(x, 2.2)
- 1 + x * 7
- 12/x

#### Next Steps
See if you can take your list of nodes and write a function that grows a random expression tree! 

#### Stretch Goals
See if you can write an **If Then Else** node, or am **Automatically Defined Variable** node, where the value returned by a subtree under this node can be referenced with a variable name. 