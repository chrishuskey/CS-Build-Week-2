# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def remove_kth_from_end(head, k):
    """
    Remove element from linked list that is the kth-last element of the linked list.
    """    
    # Initiate variables to hold node_to_replace and the nodes before/after it:
    prev = None
    node_to_replace = None
    next_node = None
    # Find the tail of the LL, while keeping track of the kth-last element (if any) 
    # and the nodes before/after it:
    last = head
    index = 0
    while last is not None and k != 0:
        if index == k - 1:
            prev = None
            node_to_replace = head
            next_node = node_to_replace.next
        elif index == k:
            prev = head
            node_to_replace = prev.next
            next_node = node_to_replace.next
        elif index > k:
            prev = node_to_replace
            node_to_replace = next_node
            next_node = next_node.next
        
        # Move to next node in the LL:
        index += 1
        last = last.next
    
    # If there is a kth-last element in the LL, replace it:
    if node_to_replace is not None:
        # If node_to_replace is the head of the LL, remove the head:
        if prev is None:
            head = next_node
        # If node_to_replace is the tail of the LL, remove the tail:
        elif next_node is None:
            prev.next = None
        # Otherwise, remove node_to_replace from the LL:
        else:
            prev.next = next_node
            # node_to_replace.next = None
    
    # Return the LL (with kth-last node removed, if applicable):
    return head
