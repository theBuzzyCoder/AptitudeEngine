#!/usr/bin/python3
import nltk
import extraction_abc
import sys
import re
import os
from nltk.tokenize import sent_tokenize,word_tokenize

sys.path.append(os.path.join(os.path.dirname(__file__), '../TimeSpeedDistance'))
import tsd
class TrainsExtractParameters(extraction_abc.ExtractParameters):
    """ A Extract parameter class which can extract parameters from train problems"""

    def __understand_sentence(self, sentence_words, object_to_be_saved):
        speed_units = {
        "m" : {"mtrps","mtr/s","metres/sec","meters per second","meters","metres per second"},
        "k":{"kmph","km/hr","kilometers per hour","kilometers/hour"},
        "mi":{"miph","mi/hr","miles per hour","miles/hour"}
        }
        time_units = {
        "m" : {"secs","seconds","s"},
        "k" : {"hours","h","hrs"},
        "mi" : {"hours","h","hrs"}
        }
        distance_units = {
        "m" : {"meter","meters","metres","metre","m","mtr"},
        "k" : {"km","kilometers","kilometres","kilometer","kilometre"},
        "mi" : {"mi","mile","miles"}
        }
        objects = {"man","pole","car","bike","telegraph","train","platform","tunnel","bridge"}
        once = False
        for word in sentence_words:
            if type(word) == tuple:
                for cat in speed_units:
                    if word[1].lower() in speed_units[cat]:
                        object_to_be_saved['speed'] = eval(word[0])
                        object_to_be_saved['s-unit'] = cat
                        break
                    elif word[1].lower() in distance_units[cat]:
                        object_to_be_saved['length'] = eval(word[0])
                        object_to_be_saved['l-unit'] = cat
                        break
            else:
                if word.lower() in objects:
                    if not once:
                        object_to_be_saved['name'] = word
                        once = True


    def extract_and_solve(self, question):
        opposite = True
        s_objects = [{'name':"",'length':0,'l-unit':'m','speed':0,'s-unit':'m'}, {'name':"",'length':0,'l-unit':'m','speed':0,'s-unit':'m'}]
        time = [0,0,0]
        given = {'distance':0,'unit':'m','time':time}
        output ={"unit":"m"}
        speed_units = {
        "m" : {"mtrps","mtr/s","metres/sec","meters per second","meters","metres per second"},
        "k":{"kmph","km/hr","kilometers per hour","kilometers/hour"},
        "mi":{"miph","mi/hr","miles per hour","miles/hour"}
        }
        time_units = {
        "m" : {"secs","seconds","s","second"},
        "k" : {"hours","h","hrs","hour"},
        "mi" : {"hours","h","hrs","hour"}
        }
        distance_units = {
        "m" : {"meter","meters","metres","metre","m","mtr"},
        "k" : {"km","kilometers","kilometres","kilometer","kilometre"},
        "mi" : {"mi","mile","miles"}
        }
        objects = {"man","pole","car","bike","telegraph","train","platform","tunnel","bridge"}
        sentences = sent_tokenize(question)
        if len(sentences) != 3:
            return {"error":"""Format required for relative speed problem is not maintained.
            Format is sentence 1 describes the properties of object1.
            sentence 2 describes the properties of object 2.
            Sentence 3 describes the distance or time between objects ,what the output is? in what unit should the output be etc."""}
        sentence_words = []
        for sen in sentences:
            sentence_words.append(word_tokenize(sen))
        if "same" in sentence_words:
            opposite = False
        chunkGram = r"""unit: {<CD> <NN.?>}
        object : {<NN.?>}
        what : {<WRB|WP>}
        """
        chunkParser = nltk.RegexpParser(chunkGram)
        structured_sentences = []
        for words in sentence_words:
            pos_tag = nltk.pos_tag(words)
            chunked = chunkParser.parse(pos_tag)
            structured_sentence = []
            for subtree in chunked.subtrees():
                if type(subtree) is nltk.Tree and subtree.label() != "S":
                    if subtree.label() == "object":
                        structured_sentence.append(subtree[0][0])
                    elif subtree.label() == "unit":
                        structured_sentence.append((subtree[0][0],subtree[1][0]))
                    else:
                        structured_sentence.append(0)
            structured_sentences.append(structured_sentence)
        self.__understand_sentence(structured_sentences[0], s_objects[0])
        self.__understand_sentence(structured_sentences[1], s_objects[1])
        #code to extract details about distance and other things
        question_sentence = structured_sentences[2]
        question_mode = False
        which_obj = False
        what = False
        for word in question_sentence:
            if word == 0:
                question_mode = True
            elif type(word) == tuple:
                for cat in distance_units:
                    if word[1].lower() in distance_units[cat]:
                        given['distance'] = eval(word[0])
                        given['unit'] = cat
                        break
                    elif word[1].lower() in time_units[cat]:
                        if cat == 'm':
                            time[2] = eval(word[0])
                        else:
                            time[1] = eval(word[0])
            else:
                if question_mode:
                        if word.lower() == s_objects[0]['name']:
                            which_obj = 1
                        elif word.lower() == s_objects[1]['name']:
                            which_obj = 2
                        else:
                            if word.lower() == "length":
                                what = word.lower()
                            elif word.lower() == "speed":
                                what = word.lower()
                            elif word.lower() == "distance":
                                output['what'] = word.lower()
                            elif word.lower() == "time":
                                output['what'] = word.lower()
                            else:

                                for cat in distance_units:
                                    if word.lower()  in  distance_units[cat] or word.lower() in speed_units[cat] or word.lower() in time_units[cat]:
                                        output['unit'] = cat
                                        break
        if what and which_obj:
            output['what'] = what + "-" +str(which_obj)
        return tsd.relative_speed(s_objects[0],s_objects[1],given,output,opposite)
