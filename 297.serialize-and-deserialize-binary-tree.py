# @leet start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    separator = ','

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Preorder DFS
        # account for null nodes:
        print('test')
        if not root:
            return "None"
        lft = self.serialize(root.left)
        rht = self.serialize(root.right)
        # return string in order of val will be root, then left recursive, then right recursive, ending on null nodes
        result = f'{root.val}{Codec.separator}{lft}{Codec.separator}{rht}'
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(str(data))
        tree_as_list = deque(data.split(Codec.separator))
        print(tree_as_list)
        def deserial_dfs():
            next = tree_as_list.popleft()
            # specifically check None string
            if next == 'None':
                return None
            # repeats steps taken to dfs, using the string as a queue
            node = TreeNode(int(next))
            node.left = deserial_dfs()
            node.right = deserial_dfs()
            return node
        return deserial_dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @leet end
