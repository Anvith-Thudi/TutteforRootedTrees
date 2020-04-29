# label which index is the parent and which is the child
parent = 0
child = 1


# takes binary tree and creates list of all nodes
def nodes(tree):
    length = len(tree)
    items = []

    for x in range(0, length):
        if tree[x][parent] not in items:
            items.append(tree[x][0])

        if tree[x][child] not in items:
            items.append(tree[x][1])

    return items


# takes parent tree and gives the size
def find_size(tree):
    items = nodes(tree)

    return len(items)


# find leafs from a parent tree
def find_leafs(tree):
    items = nodes(tree)
    leafs = []
    for item in items:
        x = 0
        while x < len(tree) and item != tree[x][parent]:
            x = x + 1
        if x == len(tree):
            leafs.append(item)

    return leafs


# finds root from a parent tree
def find_root(tree):
    items = nodes(tree)
    root = "a"
    for item in items:
        x = 0
        while x < len(tree) and item != tree[x][child]:
            x = x + 1
        if x == len(tree):
            root = item

    return root


# find parent of a node given parent list (assumes not root)
def find_parent(node, tree):
    the_parent = 'a'

    for x in range(0, len(tree)):
        if node == tree[x][child]:
            the_parent = tree[x][parent]

    return the_parent


# find children of a node (assumes not a leaf)
def find_children(node, tree):
    children = []

    for x in range(0, len(tree)):
        if node == tree[x][parent]:
            children.append(tree[x][child])

    return children


# removes a leaf from the tree and gives new subtree
def remove_leaf(node, tree):
    # print(node)
    par = find_parent(node, tree)
    new_tree = tree.copy()
    edge = []
    if parent < child:
        edge.append(par)
        edge.append(node)
    else:
        edge.append(node)
        edge.append(par)

    # print(edge)
    new_tree.remove(edge)

    return new_tree


# return list of edges in tree and non-leaf edges in
def tree_term(tree):
    return [len(tree), len(tree) - len(find_leafs(tree))]


# Returns a list of all the subtrees of a tree (with duplicants)
# we don't use this but kept it for future reference
def subtrees(tree):
    if tree == []:
        return [['empty']]

    trees = [tree]
    leafs = find_leafs(tree)
    # print("these are leafs")
    # print(leafs)

    for x in range(0, len(leafs)):
        # print(leafs[x])
        sub = remove_leaf(leafs[x], tree)
        if sub not in trees:
            subs = subtrees(sub)
            trees = trees + subs

    return trees


# adds all the subtrees to a list without duplicants
def get_subs(tree, subs):
    if tree not in subs:
        if tree == []:
            subs.append([])

        else:
            subs.append(tree)
            leafs = find_leafs(tree)
            # print("these are leafs")
            # print(leafs)

            for x in range(0, len(leafs)):
                # print(leafs[x])
                subtree = remove_leaf(leafs[x], tree)
                get_subs(subtree, subs)


# Returns list without  redundancies
# we don't use this but kept it for future reference
def remove_duplicants(listsubtrees):
    new_list = []
    for x in range(0, len(listsubtrees)):
        if listsubtrees[x] not in new_list:
            new_list.append(listsubtrees[x])

    return new_list


# returns polynomial formed by iterating over all the subgraphs (by recursively removing leafs)
def polynomial(tree):
    # subs = remove_duplicants(subtrees(tree))
    subs = []
    get_subs(tree, subs)

    poly = []

    for item in subs:
        if item == []:
            poly.append([0, 0])

        else:
            poly.append(tree_term(item))

    return poly


# simplify a list of terms
def simplify(terms):
    new_list = []
    coefficients = []
    for item in terms:
        if item not in new_list:
            new_list.append(item)
            coefficients.append(1)
        else:
            place = new_list.index(item)
            coefficients[place] = coefficients[place] + 1

    final_list = []
    for x in range(0, len(new_list)):
        final_list.append([coefficients[x]] + new_list[x])

    return final_list

