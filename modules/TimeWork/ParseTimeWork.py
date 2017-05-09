import nltk
import TimeWork as TW
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
work = {'A':'-','B':'-','C':'N','AB':'-','BC':'N','AC':'N','ABC':'N'}


def pc(tokenized):
    try:
        for i in tokenized[:10]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            return tagged
    except Exception as e:
        print(str(e))
def assistedExist(wg):
    for tupel in wg:
        if tupel[0] == 'assisted' or tupel[0] == 'helped':
            return True
    return False

def findby(wg):
    i = 0
    for tupel in wg:
        if tupel[0] == 'by':
            return i
        i += 1
    return False

def makebar():
    for key, value in work.items():
        if work[key] == 'N':
            work[key] = '-'

def fractionExists(wg):
    for tupel in wg:
        if tupel[0] == 'fraction':
            return True
    return False

def remainingExists(wg):
    for tupel in wg:
        if tupel[0] == 'remaining':
            return True
    return False

def findCD(wg):
    i = 0
    for tupel in wg:
        if tupel[1] == 'CD':
            return i
        i = i + 1
    return False

def daysExist(wg):
    for tupel in wg:
        if tupel[0] == 'days':
            return True
    return False

def togetherExsit(wg):
    for tupel in wg:
        if tupel[0] == 'together':
            return True
    return False



def findpos(wg):
    i = 0
    for tupel in wg:
        if tupel[1] == 'DT' or tupel[1] == 'NNP':
            return i
        i += 1

def findNNP(wg):
    i = 0
    for tupel in wg:
        if tupel[1] == 'NNP':
            return i
        elif tupel[1] == 'DT' and tupel[0] == 'A':
            return i
        else:
            i = i + 1
    return False
def input_type1(wg):
    n = findpos(wg)
    token = wg[n]
    token2 = wg[n + 1]
    token3 = wg[n + 2]
    if token[1] == 'DT' or token[1] =='NNP':
        if token2[1] == 'MD' or token2[1] == 'VBZ' or token2[1] == 'NN' or token2[1] == 'RB':
            return True
    return False

    return True
def input_type2(wg):
    n = findpos(wg)
    tupel1 = wg[n]
    tupel2 = wg[n + 1]
    tupel3 = wg[n + 2]
    if tupel1[1] == 'DT' or tupel1[1] == 'NNP':
        if tupel2[0] == 'and':
            if tupel3[1] == 'NNP':
                return True
    return False

def input_type3(wg):
    n = findpos(wg)
    tupel1 = wg[n]
    tupel2 = wg[n + 1]
    tupel3 = wg[n + 2]
    tupel4 = wg[n + 3]
    tupel5 = wg[n + 4]
    if tupel1[1] == 'DT' or tupel1[1] == 'NNP':
        if tupel2[0] == ',':
            if tupel3[1] == 'NNP':
                if tupel4[0] == 'and':
                    if tupel5[1] == 'NNP':
                        return True
    return False




def extractValues(words_grammer):
    n = findpos(words_grammer)
    for i in range(len(words_grammer)):
        token = words_grammer[i]
        grammer = token[1]
        if grammer == 'CD':
            t = words_grammer[n]
            work[t[0]] = int(token[0])
            return True
    return False
def extractcouplevalues(words_grammer):
    n = findpos(words_grammer)
    for i in range(len(words_grammer)):
        token = words_grammer[i]
        grammer = token[1]
        if grammer == 'CD':
            t = words_grammer[n]
            t2 = words_grammer[n + 2]
            work[t[0] +t2[0]] = int(token[0])
            return True
    return False

def extrattriplevalues(words_grammer):
    n = findpos(words_grammer)
    for i in range(len(words_grammer)):
        token = words_grammer[i]
        grammer = token[1]
        if grammer == 'CD':
            t = words_grammer[n]
            t2 = words_grammer[n + 2]
            t3 = words_grammer[n + 4]
            work[t[0] +t2[0]+t3[0]] = int(token[0])
            return True
    return False

def questionCode1(words_grammer):
    if findNNP(words_grammer) and not(findCD(words_grammer)):
        n = findNNP(words_grammer)
        tupel1 = words_grammer[n]
        tupel2 = words_grammer[n + 1]
        tupel3 = words_grammer[n + 2]
        tupel4 = words_grammer[n + 3]
        tupel5 = words_grammer[n + 4]
        if tupel2[0] == 'and' and tupel3[1] == 'NNP' and daysExist(words_grammer):
            values = [tupel1[0]+tupel3[0]]
        elif tupel2[0] == ',' and tupel3[1] == 'NNP' and tupel4[0] == 'and' and tupel5[1] == 'NNP' and daysExist(words_grammer):
            values = [tupel1[0]+tupel3[0]+tupel5[0]]
        else:
            values = [tupel1[0]]
    elif togetherExsit(words_grammer) and daysExist(words_grammer) and not(findCD(words_grammer)):
        if work['C'] == 'N' and work['AC'] == 'N' and work['BC'] == 'N' and work['ABC'] == 'N':
            values = ['AB']
        else:
            makebar()
            values = ['ABC']
    else:
        return False
    values.append(1)
    return values

def questionCode2(words_grammer):
    if work['C'] == 'N' and work['AC'] == 'N' and work['BC'] == 'N' and work['ABC'] == 'N':
        values = ['AB']
    else:
        makebar()
        values = ['ABC']
    for tupel in words_grammer:
        if tupel[1] == "CD" and remainingExists(words_grammer):
            values.append(tupel[0])
            return values
    return False

def questionCode3(words_grammer):
    if work['C'] == 'N' and work['AC'] == 'N' and work['BC'] == 'N' and work['ABC'] == 'N':
        values = ['AB']
    else:
        makebar()
        values = ['ABC']
    for tupel in words_grammer:
        if tupel[1] == "CD" and remainingExists(words_grammer) and fractionExists(words_grammer):
            values.append(tupel[0])
            return values
    return False

def questionCode4(words_grammer):
    if not (work['C'] == 'N' and work['AC'] == 'N' and work['BC'] == 'N' and work['ABC'] == 'N'):
        makebar()

    for tupel in words_grammer:
        if assistedExist(words_grammer) and findCD(words_grammer):
            pos = findCD(words_grammer)
            tupel = words_grammer[pos]
            values = [tupel[0]]
            if findNNP(words_grammer):
                pos = findNNP(words_grammer)
                tupel = words_grammer[pos]
                values.append(tupel[0])
                if findby(words_grammer):
                    pos = findby(words_grammer)
                    tupel = words_grammer[pos + 1]
                    values.append(tupel[0])
                    return values
    return False






def solve(Question):
    #train_text = state_union.raw("/home/ankit/Downloads/TimeWork.txt")
    #sample_text = state_union.raw("/home/ankit/Downloads/ty.txt")
    #custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    #Question = "A can do a job in 20 days. B can do it in 40 days. If they work together in how many days they will finish the work."
    sentance = sent_tokenize(Question)
    for i in range(0,len(sentance) - 1):
        #tokenized = custom_sent_tokenizer.tokenize(sentance[i])
        #print([sentance[i]])
        words_grammer = pc([sentance[i]])
        if input_type1(words_grammer):
            if not(extractValues(words_grammer)):
                return False
        elif input_type2(words_grammer):
            if not(extractcouplevalues(words_grammer)):
                return False
        elif input_type3(words_grammer):
            if not(extrattriplevalues(words_grammer)):
                return False
        else:
            return False

    #tokenized = custom_sent_tokenizer.tokenize(sentance[len(sentance) - 1])
    words_grammer = pc([sentance[len(sentance) - 1]])
    if questionCode1(words_grammer):
        values = questionCode1(words_grammer)
        result = TW.sol_prob(work,int(values[1]),values[0],0,1)
    elif questionCode3(words_grammer):
        values = questionCode3(words_grammer)
        result = TW.sol_prob(work,int(values[1]),values[0],0,3)
    elif questionCode2(words_grammer):
        values = questionCode2(words_grammer)
        result = TW.sol_prob(work,int(values[1]),values[0],0,2)
    elif questionCode4(words_grammer):
        values = questionCode4(words_grammer)
        print(work)
        result = TW.sol_prob(work,int(values[0]),values[1],values[2],5)
    else:
        return False
    if result:
        return result
    else:
        return False
    return True
