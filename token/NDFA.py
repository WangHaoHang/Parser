import json

class state(object):
    def __init__(self) -> None:
        self.next = {}
        self.id = 0
        self.label = ""
        self.info = []

    def append_follower(self,edge,follower):
        return True
class DFAState(state):
    def __init__(self) -> None:
        super().__init__()
    
    def append_follower(self,edge,follower:state):
        if self.next.get(edge) == None:
            self.next[edge] = [follower]
            return True
        else:
            print("follower happen conflic!",self.next[edge][0],follower)
            return False

class NFAState(state):
    
    def __init__(self) -> None:
        super().__init__()
    
    def append_follower(self, edge, follower):
        if self.next.get(edge) == None:
            self.next[edge] = [follower]
            
        else:
            self.next[edge].append(follower)
        return True
class StateUtils(object):
    def __init__(self) -> None:
        pass
    
    def create_dfa_state(self,label:str):
        node = DFAState()
        node.label = label
        return node
    
    def create_dfa_states(self,labels:[]):
        nodes = []
        for label in labels:
            nodes.append(self.create_dfa_state(label))
        return nodes
    
    def create_nfa_state(self,label:str):
        node = NFAState()
        node.label = label
        return node
    
    def create_nfa_states(self,labels:[]):
        nodes = []
        for label in labels:
            nodes.append(self.create_nfa_state(label))
        return nodes
    
    def append_follower(self,node:state, edge: str,follower:state):
        return node.append_follower(edge,follower)
    
    def append_followers(self,node:state,edge:str, followers:[]):
        flag = True
        for follower in followers:
            flag &= self.append_follower(node,edge,follower)
        return flag
    
    def edge(self, node:state, label:str) -> list:
        result = []
        followers = node.next.get(label)
        if followers is not None:
            for follower in followers:
                result.append(follower)
        return result
    
    
    def closure(self, S:[], label:str) -> set:
        T = set([])
        n_size = 0
        for s in S:
            T.add(s)
        n_size = len(T)
        while True:
            tmp = set([])
            for t in T:
                tmp = tmp.union(set(self.edge(t,label)))
            T = T.union(tmp)
            if n_size == len(T):
                break
            else:
                n_size = len(T)
        return T
    
    def DFAedage(self, D:[],c:str) -> set:
        T = self.closure(D,c)
        result = list(T)
        result = self.closure(result,'')
        return result
if __name__ == '__main__':
    T = set([])
    utils = StateUtils()
    node = utils.create_dfa_state('s')
    follower1 = utils.create_dfa_state("a")
    follower2 = utils.create_dfa_state("b")
    utils.append_follower(node,'a',follower1)
    utils.append_follower(node,'b',follower2)
    result = utils.closure([node],'a')
    result = list(result)
    for r in result:
        print(r.label)
