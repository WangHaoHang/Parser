'''
词法分析
'''
import logging

class text_process(object):
    def __init__(self):
        self.lines = []
    
    def process_symbol(self):
        '''
            处理符号 + - * / =
        '''
        pass
    
    def readText(path_url):
        '''
            读取文本数据
        '''
        try:
            fd = open(path_url,'r')
            self.lines = fd.readlines()
            fd.close()
        except Exception as e:
            logging.error(e)
        return self.lines

if __name__ == '__main__':
    pass