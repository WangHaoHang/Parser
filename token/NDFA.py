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
            print("follower happen conflic!",self.next[edge][0].label,follower.label)
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
    '''_summary_

    :param object: _description_
    :type object: _type_
    '''
    def __init__(self) -> None:
        pass
    
    def create_dfa_state(self,label:str):
        '''_summary_

        :param label: _description_
        :type label: str
        :return: _description_
        :rtype: _type_
        '''
        node = DFAState()
        node.label = label
        return node
    
    def create_dfa_states(self,labels:[]):
        '''_summary_

        :param labels: _description_
        :type labels: _type_
        :return: _description_
        :rtype: _type_
        '''
        nodes = []
        for label in labels:
            nodes.append(self.create_dfa_state(label))
        return nodes
    
    def create_nfa_state(self,label:str):
        '''_summary_

        :param label: _description_
        :type label: str
        :return: _description_
        :rtype: _type_
        '''
        node = NFAState()
        node.label = label
        return node
    
    def create_nfa_states(self,labels:[]):
        '''_summary_

        :param labels: _description_
        :type labels: _type_
        :return: _description_
        :rtype: _type_
        '''
        nodes = []
        for label in labels:
            nodes.append(self.create_nfa_state(label))
        return nodes
    
    def append_follower(self,node:state, edge: str,follower:state):
        '''_summary_

        :param node: _description_
        :type node: state
        :param edge: _description_
        :type edge: str
        :param follower: _description_
        :type follower: state
        :return: _description_
        :rtype: _type_
        '''
        return node.append_follower(edge,follower)
    
    def append_followers(self,node:state,edge:str, followers:[]):
        '''_summary_

        :param node: _description_
        :type node: state
        :param edge: _description_
        :type edge: str
        :param followers: _description_
        :type followers: _type_
        :return: _description_
        :rtype: _type_
        '''
        flag = True
        for follower in followers:
            flag &= self.append_follower(node,edge,follower)
        return flag
    
    def edge(self, node:state, label:str) -> list:
        '''_summary_

        :param node: _description_
        :type node: state
        :param label: _description_
        :type label: str
        :return: _description_
        :rtype: _type_
        '''
        result = []
        followers = node.next.get(label)
        if followers is not None:
            for follower in followers:
                result.append(follower)
        return result
    
    
    def closure(self, S:[], label:str) -> set:
        '''_summary_

        :param S: _description_
        :type S: _type_
        :param label: _description_
        :type label: str
        :return: _description_
        :rtype: _type_
        '''
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
        '''_summary_

        :param D: _description_
        :type D: _type_
        :param c: _description_
        :type c: str
        :return: _description_
        :rtype: _type_
        '''
        
        T = self.closure(D,c)
        result = list(T)
        result = self.closure(result,'')
        return result
    def NFA2DFA(self,start_state:state,dict_:[]):
        '''_summary_

        :param start_state: _description_
        :type start_state: DFAState
        :param dict_: _description_
        :type dict_: _type_
        '''
        
        dfa_states = []
        state1 = self.create_dfa_state('1')
        state1.info = list(self.closure([start_state],''))
        dfa_states.append(state1)
        p = 1
        j = 0
        while(j < p):
            for c in dict_:
                tmp = self.DFAedage(dfa_states[j].info,c)
                size = len(dfa_states)
                flag = True
                for i in range(size-1):
                    if dfa_states[i].info == tmp:
                        flag = False
                        if not self.append_follower(dfa_states[j],c,dfa_states[i]):
                            print('append conflict:',size-1,i)
                if(flag):
                    p = p + 1
                    new_state = self.create_dfa_state(str(p))
                    new_state.info = tmp
                    self.append_follower(dfa_states[j],c,new_state)
                    dfa_states.append(new_state)
            j += 1
        return dfa_states
                        
        
        
if __name__ == '__main__':
    # T = set([])
    utils = StateUtils()
    # node = utils.create_dfa_state('s')
    # follower1 = utils.create_dfa_state("a")
    # follower2 = utils.create_dfa_state("b")
    # utils.append_follower(node,'a',follower1)
    # utils.append_follower(node,'b',follower2)
    # result = utils.closure([node],'a')
    # result = list(result)
    # for r in result:
    #     print(r.label)
    
    # NFA2DFA test case
    dict_ = ['x','y']
    nfa_states = utils.create_nfa_states(['1','2','3','4','5','6','7'])
    utils.append_follower(nfa_states[0],'x',nfa_states[4])
    utils.append_follower(nfa_states[0],'',nfa_states[1])
    utils.append_follower(nfa_states[1],'',nfa_states[2])
    utils.append_follower(nfa_states[1],'y',nfa_states[5])
    utils.append_follower(nfa_states[2],'',nfa_states[3])
    utils.append_follower(nfa_states[3],'',nfa_states[0])
    utils.append_follower(nfa_states[4],'',nfa_states[5])
    utils.append_follower(nfa_states[4],'x',nfa_states[1])
    utils.append_follower(nfa_states[5],'',nfa_states[6])
    
    dfa_states = utils.NFA2DFA(nfa_states[0],dict_=dict_)
    print(len(dfa_states))
    for dfa_state in dfa_states:
        print(dfa_state.label,':')
        for state in dfa_state.info:
            print('label:   ',state.label)
        for k in dfa_state.next.keys():
            print('map:    ',k,len(dfa_state.next[k]),dfa_state.next[k][0].label)
    
