'''
词法分析
'''
import logging

def readText(path_url):
    '''
        读取文本数据
    '''
    try:
        fd = open(path_url,'r')
        lines = fd.readlines()
        fd.close()
    except Exception as e:
        logging.error(e)
    return lines

if __name__ == '__main__':
    pass