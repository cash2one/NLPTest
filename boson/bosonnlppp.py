# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import datetime


class BosonNlpp:
    def __init__(self):
        self.bonlp = BosonNLP('IKBIoANy.14545.A7GCYBnT9jIB')
    #情感分析
    def testSentiment(self,s):
        result=self.bonlp.sentiment(s)
        return result
        #print(result)
    #命名实体识别
    def lexicalAnalysis(self,s):
        result=self.bonlp.ner(s)[0]
        return result
    #依存文法分析
    def textDependency(self,s):
        result = self.bonlp.depparser(s)
        return result
    #关键词提取
    def testKeywords(self,s):
        result = self.bonlp.extract_keywords(s, top_k=10)
        return result
    #新闻分类
    def textClassify(self,s):
        resultlist=self.bonlp.classify(s)
        classifys={0:'体育',1:'教育',2:'财经',3:'社会',4:'娱乐',5:'军事',6:'国内',7:'科技',8:'互联网',9:'房产',10:'国际',11:'女人',12:'汽车',13:'游戏'}
        return(classifys[resultlist[0]])
    #语义联想
    def lexicalSynonym(self,term):
        result=self.bonlp.suggest(term, top_k=10)
        return result
    #分词与词性标注
    def fenci(self,s):
        result = self.bonlp.tag(s)
        return result
    def newssubstract(self,s):
        #s=s.encode('utf8')
        s=s.decode('utf-8')
        result = self.bonlp.summary('', s)
        return result

if __name__ == "__main__":
    nl=BosonNlpp()
    s=['对于该小孩是不是郑尚金的孩子，目前已做亲子鉴定，结果还没出来，'
     '纪检部门仍在调查之中。成都商报记者 姚永忠']
    #调用情感分析接口
    print(nl.testSentiment(s))
    #命名实体识别
    resultlex=nl.lexicalAnalysis(s)
    words = resultlex['word']
    entities = resultlex['entity']
    for entity in entities:
        print(''.join(words[entity[0]:entity[1]]), entity[2])
    #依存文法分析
    resultdep=nl.textDependency(s)
    print(' '.join(resultdep[0]['word']))
    print(' '.join(resultdep[0]['tag']))
    print(resultdep[0]['head'])
    print(' '.join(resultdep[0]['role']))

    #新闻字段
    xinwen=['俄否决安理会谴责叙军战机空袭阿勒颇平民',
     '邓紫棋谈男友林宥嘉：我觉得我比他唱得好',
     'Facebook收购印度初创公司']
    #新闻分类
    resultclass=nl.textClassify(xinwen)

    guanjian='对于该小孩是不是郑尚金的孩子，目前已做亲子鉴定，结果还没出来,纪检部门仍在调查之中。成都商报记者 姚永忠'
    resultkey=nl.testKeywords(guanjian)
    for weight, word in resultkey:
            print(weight, word)
    term='元宝'
    #语义联想
    resultsyn=nl.lexicalSynonym(term)
    for score, word in resultsyn:
            print(score, word)
    #分词
    resultfenci=nl.fenci(s)
    for d in resultfenci:
            print(' '.join(['%s/%s' % it for it in zip(d['word'], d['tag'])]))

    content = (
    '腾讯科技讯（刘亚澜）10月22日消息，前优酷土豆技术副总裁黄冬已于日前正式加盟芒果TV，出任CTO一职。资料显示，黄冬历任土豆网技术副总裁、优酷土豆集团产品技术副总裁等职务，曾主持设计、运营过优酷土豆多个大型高容量产品和系统。此番加入芒果TV或与芒果TV计划自主研发智能硬件OS有关。今年3月，芒果TV对外公布其全平台日均独立用户突破3000万，日均VV突破1亿，但挥之不去的是业内对其技术能力能否匹配发展速度的质疑，亟须招揽技术人才提升整体技术能力。芒果TV是国内互联网电视七大牌照方之一，之前采取的是“封闭模式”与硬件厂商预装合作，而现在是“开放下载”+“厂商预装”。黄冬在加盟土豆网之前曾是国内FreeBSD（开源OS）社区发起者之一，是研究并使用开源OS的技术专家，离开优酷土豆集团后其加盟果壳电子，涉足智能硬件行业，将开源OS与硬件结合，创办魔豆智能路由器。未来黄冬可能会整合其在开源OS、智能硬件上的经验，结合芒果的牌照及资源优势，在智能硬件或OS领域发力。公开信息显示，芒果TV在今年6月对外宣布完成A轮5亿人民币融资，估值70亿。')
    #新闻摘要
    #print(content[0])
    #print(isinstance(content[0], unicode))
    resultsub=nl.newssubstract(content)
    #print(isinstance(resultsub, unicode))#判断编码是否是unicode编码
    #print(isinstance(resultsub, basestr))
    #f=chardet.detect(resultsub)
    #print(f)
    print (resultsub)
    #chardet.detect(nl.newssubstract(content))