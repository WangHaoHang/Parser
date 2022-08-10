class state_node(object):
    def __init__(self) -> None:
        self.state = 0
        self.desc = ''
        self.next = None
        self.condition = None
        
        
def createStateVm(word:str):
    state = 0
    start = state_node()
    start.state = state
    start.desc= 'start_state'
    cur_node = start
    for i in word:
        state += 1
        node1 = state_node()
        node1.state = state
        cur_node.condition = i
        cur_node.next = node1
        cur_node = node1
    cur_node.desc='end_state'
    return start

if __name__ == '__main__':
    start_node = createStateVm("while")
    cur_node = start_node
    while cur_node is not None:
        print(cur_node.state,cur_node.condition,cur_node.desc)
        cur_node = cur_node.next