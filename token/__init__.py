print('token --- init')

class state_node(object):
    def __init__(self) -> None:
        self.state = 0
        self.desc = ''
        self.next = None
        
class word_table(object):
    '''存放词法分析数据

    :param object: _description_
    :type object: _type_
    '''
    def __init__(self) -> None:
        
        self.identifier=['while','for','if','else','int','float','byte','double','str','break','continue'] #标识符
        self.words=[] # 存放的数据
    
    def print(self):
        '''_summary_

        :return: _description_
        :rtype: _type_
        '''
        print('words:',self.words)
if __name__ == '__main__':
    print('token')