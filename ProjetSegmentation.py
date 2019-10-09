# -*- coding: utf-8 -*-
import sys,re,os,io,naftawayh.wordtag,nltk,string
from tashaphyne.stemming import ArabicLightStemmer

class segmenteur:
    def __init__(self,url):
        File=open(url)
        self.text=File.read()

    def segmenteur_mots(self):
        liste_mots = [mot for mot in nltk.word_tokenize(unicode(self.text,"utf-8")) if mot not in string.punctuation]
        with io.open('output.txt', 'w',encoding="utf-8") as file:
            file.write(unicode("\n\n"+"il y a "+str(len(liste_mots))+" mots\n","utf-8"))
            file.write(unicode("la liste des mots : \n\n ","utf-8"))
            file.write(unicode(" [ "))
            for ch in liste_mots:
                file.write(" ' "+ch+" ' ,") 
            file.write(unicode(" ] "))

    def segmenteur_phrases(self):
        tagger = naftawayh.wordtag.WordTagger()
        ArListem = ArabicLightStemmer()

        stop_words1=[u"كما",u"أيضا",u"كذالك",u"مثلا",u"وكما",u"شبيه",u"نضير",u"ماعدا",u"باستثناء",u"إلا",u"بسبب",u"لأن",u"لكي",u"والنتيجة",u"والخلاصة",u"أولا",u"ثانيا",u"يليه",u"لذالك",u"إذا",u"نستنتج",u"أم",u"أي",u"فقد",u"لكن",u"بينما",u"فإذا",u"إذا",u"حيث",u"بسبب",u"لذالك",u"لما",u"حينما",u"وذلك",u"حيث"]
        stop_words2=[[u"بالإضافة",u"إلى"],[u"ومن",u"ذالك"],[u"من",u"هنا"],[u"ونخلص",u"إلى"],[u"وفي",u"البداية"],[u"إلى",u"جانب"],[u"علاوة",u"على"],[u"غير",u"أنه"]]

        #fonction return la premier element dans la liste stop_words2
        def prem_ele(u,x):
            h=[]
            for d in u :
                h.append(d[x])
            return h

        #eleminer la signe de ponctuation
        def ele_sign(s):
            if re.split(u'،',s):
                    lt=re.split(u'،',s)
                    if len(lt) > 0:
                        for u in lt:
                            if u != '':
                                return u                           

        liste1=[ch for ch in re.split(r"[.!؟:()[]\n]+",unicode(self.text,"utf-8"))if ch != '' ] 
        
        liste3=[]

        i=0
        while i<len(liste1) :
            liste2=[ch for ch in re.split(r"[ ]+",liste1[i])if ch != '' ]
           
            k=0
            s=''
            while k<len(liste2):
                if ele_sign(liste2[k]) == u'و'  :
                    stem = ArListem.light_stem(ele_sign(liste2[k+1]))
                    if tagger.is_verb(stem)==True and tagger.is_noun(stem)==False:
                        if s !='':
                            liste3.append(s)
                            s=''
                    else :
                        s+=liste2[k]
                        s+=' '
                elif ele_sign(liste2[k]) in stop_words1:
                    liste3.append(s)
                    s=''
                elif ele_sign(liste2[k])==u'ثم':
                    stem = ArListem.light_stem(ele_sign(liste2[k+1]))
                    if tagger.is_verb(stem)==True and tagger.is_noun(stem)==False:
                        if s !='':
                            liste3.append(s)
                            s=''
                        else :
                            s+=liste2[k]
                            s+=' '
                elif ele_sign(liste2[k][0]) == u'ف' :
                    stem = ArListem.light_stem(ele_sign(liste2[k][1::]))
                    if   tagger.is_verb(ArListem.get_stem())==True and tagger.is_noun(ArListem.get_stem())==False:
                        liste3.append(s)
                        s=''
                    else :
                        s+=liste2[k]
                        s+=' '
                elif ele_sign(liste2[k])  in prem_ele(stop_words2,0):
                    if ele_sign(liste2[k+1]) in prem_ele(stop_words2,1) :
                        liste3.append(s)
                        s=''
                        k+=1
                    else :
                        s+=liste2[k]
                        s+=' '
                else:
                    s += liste2[k]
                    s+=' '        
                k+=1
            if len(s)!=0:
                liste3.append(s)
                s=''
            i+=1

        liste3=[ch for ch in liste3 if ch !='']
        
        with io.open('output.txt', 'a',encoding="utf-8") as file:
            file.write(unicode("\n\n"+"il y a "+str(len(liste3))+" phrases\n","utf-8"))
            file.write(unicode("la liste des phrases : \n\n ","utf-8"))
            file.write(unicode(" [ "))
            for ch in liste3:
                file.write(" ' "+ch+" ' \n\n")        
            file.write(unicode(" ] "))
        

    def segmenteur_parags(self):
        liste=[ch for ch in re.split(r"[\n]+",self.text)if ch != '' ]
        with io.open('output.txt', 'a',encoding="utf-8") as file:
            file.write(unicode("\n\n"+"il y a "+str(len(liste))+" paragraphes\n","utf-8"))
            file.write(unicode("la liste des paragraphes : \n\n ","utf-8"))
            file.write(unicode(" [ "))
            for ch in liste:
                file.write(unicode(" ' "+ch+" ' \n\n","utf-8")) 
            file.write(unicode(" ] "))

print("la segmentation est fait avec succes By ^^!!")
