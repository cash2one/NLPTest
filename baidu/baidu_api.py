# encoding: utf-8
from __future__ import print_function
from aip import AipNlp
from pprint import pprint
#APP_ID='9519234'
#API_KEY='CIwEvSR9m9hEWnQp2GK7LGKI'
#SECRET_KEY='s4hA4YTO1SjqIkRzTCT5uHSa715BKHFL'
#aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)
class BaiduNLP:
    def __init__(self):
        self.APP_ID='9519234'
        self.API_KEY='CIwEvSR9m9hEWnQp2GK7LGKI'
        self.SECRET_KEY='s4hA4YTO1SjqIkRzTCT5uHSa715BKHFL'
        self.baiduNlp=AipNlp(self.APP_ID, self.API_KEY, self.SECRET_KEY)
    '''----------分词-----------'''
    def wordseg(self,words):
        return self.baiduNlp.wordseg(words)

    '''----------词性标注-----------'''
    def wordpos(self,words):
        return self.baiduNlp.wordpos(words)

    '''----------向量表示-----------'''
    def wordembedding(self,words1,words2=''):
        return self.baiduNlp.wordembedding(words1,words2)

    '''----------评论观点抽取,默认7教育-----------'''
    def commenttag(self,words,type=7):
        comment=self.baiduNlp.commentTag(words,type)#返回处理
        commentTags=comment[u'tags']#得到评论观点，可能有多条评论观点
        length=len(commentTags)#得到有几个评论观点
        validComment = []
        for i in range(length):
            temp=commentTags[i]
            abstract=self.__deleteUnvalid(temp[u'abstract'])
            tempComement={u'abstract':abstract,u'adj':temp[u'adj'],u'fea':temp[u'fea'],u'type':temp[u'type']}
            validComment.append(tempComement)
        return validComment

    '''----------dnn语言模型-----------'''
    def dnnlm(self,words):
        return self.baiduNlp.dnnlm(words)

    '''----------短文相似度-----------'''
    def simnet(self,essay1,essay2):
        return self.baiduNlp.simnet(essay1,essay2)

    def __deleteUnvalid(self,sentence):#去除</span>
        abstract=sentence.replace("<span>","")
        abstract=abstract.replace("</span>", "")
        return  abstract



# aip=BaiduNLP();
# options = {
#     'type': 4, #汽车分类
# }
# result=aip.commenttag('香格里拉大酒店，早餐太难吃',options)
#result=aip.dnnlm("好未来大数据部自然语言测评系统之百度自然语言处理")
#result=aip.simnet("我的世界很美好啊","你的日子不好过啊")
# test1=aip.simnet('是','否')
# pprint(result)
#test1=aip.simnet('是','否')
#result=aip.wordembedding("百度","",2)
# test1=aip.simnet('是','否')
# pprint(result)



