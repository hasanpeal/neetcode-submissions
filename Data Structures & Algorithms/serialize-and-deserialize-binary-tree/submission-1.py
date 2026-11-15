# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                res.append("N")
                continue
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(",") # Array of nodes val
        if val[0] == "N":
            return None
        root = TreeNode(int(val[0]))
        q = deque()
        q.append(root)
        i = 1

        while q:
            node = q.popleft()
            if i < len(val) and val[i] != "N":
                node.left = TreeNode(int(val[i]))
                q.append(node.left)
            i += 1
            if i < len(val) and val[i] != "N":
                node.right = TreeNode(int(val[i]))
                q.append(node.right)
            i += 1

        return root
            

