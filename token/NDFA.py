class state(object):
    def __init__(self) -> None:
        self.next = {}
        self.id = 0
        self.label = ""

class DFAState(state):
    def __init__(self) -> None:
        super().__init__()
    
if __name__ == '__main__':
    state_ = DFAState()
    state_.label = "hello world"
    print(state_.label)