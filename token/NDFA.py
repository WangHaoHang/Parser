class State(object):
    next_state_num = int(0)
    def __init__(self) -> None:
        self.cur_state = State.next_state_num
        State.next_state_num += 1
        self.next_state = []
        self.content = None
    
    def append_next_state(self, state):
        self.next_state.append(state)
        
    def append_next_states(self, *states):
        for state in states:
            self.next_state.append(state)
    
    def get_cur_state(self):
        return self.cur_state
    
    def modify_cur_state(self,state_num):
        self.cur_state = state_num
    
    def is_next_state(self, state):
        result = False
        if len(self.next_state) == 0:
            return False
        for s in self.next_state:
            if s.cur_state == state.cur_state:
                result = True
                break
        return result
    
    def get_content(self):
        return self.content
    
    def set_content(self, content):
        self.content = content

if __name__ == '__main__':
    state1 = State()
    print(state1.cur_state)
    state2 = State()
    print(state2.cur_state)
    state1.append_next_state(state2)
    print(len(state1.next_state))