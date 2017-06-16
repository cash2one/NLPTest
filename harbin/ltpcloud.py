# -*- coding:utf-8 -*-
import urllib
class Ltpnlp:
    #词性标注
    def cixing(self,s):
        #s='北京欢迎你'
        #print(type(s))
        #s= s.encode('UTF-8')
        #s= s.decode('UTF-8')
        #print(isinstance(s,ascii))
        #s=s.encode('utf8')
        #s=s.decode('utf8')
        url_get_base = "http://api.ltp-cloud.com/analysis/"
        args = {
            'api_key' :'89X001705x6XrXnRNYJzxnIFJvhw1MVsDRuJgahN',
            'text' : s,
            'pattern' : 'pos',
            'format' : 'plain'
        }
        result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
        print result
        content = result.read().strip()
        #print("nini")
        return content
    #分词
    def fenci(self,s):
        #s='北京欢迎你'
        #print(type(s))
        #s= s.encode('UTF-8')
        #s= s.decode('UTF-8')
        #print(isinstance(s,ascii))
        #s=s.encode('utf8')
        #s=s.decode('utf8')
        url_get_base = "http://api.ltp-cloud.com/analysis/"
        args = {
            'api_key' :'89X001705x6XrXnRNYJzxnIFJvhw1MVsDRuJgahN',
            'text' : s,
            'pattern' : 'srl',
            'format' : 'plain'
        }
        result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
        print result
        content = result.read().strip()
        #print("nini")
        return content
    #命名实体识别
    def lexicalAnalysis(self,s):
        #s='北京欢迎你'
        #print(type(s))
        #s= s.encode('UTF-8')
        #s= s.decode('UTF-8')
        #print(isinstance(s,ascii))
        #s=s.encode('utf8')
        #s=s.decode('utf8')
        url_get_base = "http://api.ltp-cloud.com/analysis/"
        args = {
            'api_key' :'89X001705x6XrXnRNYJzxnIFJvhw1MVsDRuJgahN',
            'text' : s,
            'pattern' : 'ner',
            'format' : 'plain'
        }
        result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
        print result
        content = result.read().strip()
        #print("nini")
        return content
    #语义依存分析
    def textDependency(self,s):
        #s='北京欢迎你'
        #print(type(s))
        #s= s.encode('UTF-8')
        #s= s.decode('UTF-8')
        #print(isinstance(s,ascii))
        #s=s.encode('utf8')
        #s=s.decode('utf8')
        url_get_base = "http://api.ltp-cloud.com/analysis/"
        args = {
            'api_key' :'89X001705x6XrXnRNYJzxnIFJvhw1MVsDRuJgahN',
            'text' : s,
            'pattern' : 'sdp',
            'format' : 'plain'
        }
        result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
        print result
        content = result.read().strip()
        #print("nini")
        return content
    #依存句法分析
    def wordDependency(self,s):
        #s='北京欢迎你'
        #print(type(s))
        #s= s.encode('UTF-8')
        #s= s.decode('UTF-8')
        #print(isinstance(s,ascii))
        #s=s.encode('utf8')
        #s=s.decode('utf8')
        url_get_base = "http://api.ltp-cloud.com/analysis/"
        args = {
            'api_key' :'89X001705x6XrXnRNYJzxnIFJvhw1MVsDRuJgahN',
            'text' : s,
            'pattern' : 'dp',
            'format' : 'plain'
        }
        result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
        print result
        content = result.read().strip()
        #print("nini")
        return content
    #语义角色标注
    def wordmark(self,s):
        #s='北京欢迎你'
        #print(type(s))
        #s= s.encode('UTF-8')
        #s= s.decode('UTF-8')
        #print(isinstance(s,ascii))
        #s=s.encode('utf8')
        #s=s.decode('utf8')
        url_get_base = "http://api.ltp-cloud.com/analysis/"
        args = {
            'api_key' :'89X001705x6XrXnRNYJzxnIFJvhw1MVsDRuJgahN',
            'text' : s,
            'pattern' : 'srl',
            'format' : 'plain'
        }
        result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
        print result
        content = result.read().strip()
        #print("nini")
        return content
if __name__ == '__main__':
    nlp=Ltpnlp()
    s='北京欢迎你'
    #print("词性标注结果")
    #print(nlp.cixing(s))
    #print("分词")
    #print(nlp.fenci(s))
    #print("命名实体识别")
    #print(nlp.lexicalAnalysis(s))
    #print("依存句法分析")
    #print(nlp.textDependency(s))
    print("语义依存分析")
    print(nlp.wordDependency(s))
    print("语义角色标注")
    print(nlp.wordmark(s).encode('UTF-8'))