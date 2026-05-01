"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # opening up my own little "clone shop!"
        
        # ok the clone shop doesn't have any clients today, we end business
        if not node: return None

        # we need to have a book to keep track of our clients
        old_to_new = {}

        # we're gonna make them line up here to produce clones of themselves
        q = deque()

        ##### first client!
        q.append(node)
        
        # every time we append to queue, there must be an action that follows to mark this as processed
        # in this case, we need to add it to the old_to_new
        
        # we are also going to write them into our fast book for easy retrieval later
        old_to_new[node] = Node(node.val)
        ####

        # bfs traversal
        # while we have clients in the line...
        while q:
            # ok next up! show me your Id please...
            curr = q.popleft()

            # nice! seems like you have neighbors, lets go through them
            # and check if any of them are in our file. if not, we can register them for you!
            for n in curr.neighbors:
                if n not in old_to_new: # first timer! we dont have them on file
                    # let me register them for you
                    old_to_new[n] = Node(n.val)
                    # all set, and they need to be processed later too,
                    # i'll put them in line (the original one gets in line)
                    q.append(n)
                
                # ok now let's add them as your neighbor!
                # BUT have to make sure that we are adding the COPY of the neighbor,
                # not the original neighbor, because the original neighbor might be busy (need to copy his clone)
                old_to_new[curr].neighbors.append(old_to_new[n])
            
        return old_to_new[node] # find the original, first client's clone



        
            

