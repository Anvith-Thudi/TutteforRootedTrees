# TutteforRootedTrees

# This is a python implementation of an algorithm I devised to compute the tutte polynomial of rooted trees, given a parent list of the format [[parent,child],[parent,child],....]

# To use it, simply import ComputeTutte(RootedTrees).py and call simplify(polynomial()) from the module. The output is of the form [[coefficient,# of edges, # of non-leaf edges]], and simplify() simply adds up the coefficient of like-terms.

# I've tested it substantially, and have had no issues. However, by the NP nature of finding and iterating over the subgraphs of a tree, the code becomes unreasonable for trees size 30 and over; at size 29 it takes me- using an average laptop and pycharm- on average half an hour to compute the polynomial.

# I also included a converter from the simplified polynomial to an excel sheet, where it form a matrix with column = # of non-leaf edges and row = # of edges. Simply import ConvertPolytoExcelMatrix.py and use the convert_excel() function.

# I've not tested the converter in its current format, but it's simple enough that I assume it will work.

