#!/usr/bin/python3
import nltk
import extraction_abc
import sys
import re
import os
from nltk.tokenize import sent_tokenize,word_tokenize
sys.path.append(os.path.join(os.path.dirname(__file__), '../LCM'))
import lcm_n_hcf as l
class LCMExtractParameters(extraction_abc.ExtractParameters):
    """ A Extract parameter class which can extract parameters from LCM and HCF problems"""

    def extract_and_solve(self, question):
        while True:
            copy_question = question
            question = question.replace(","," ");
            question = question.replace(":"," ");
            if question == copy_question:
                break

        sentences = sent_tokenize(question.lower())
        words = []
        for sen in sentences:
            words = words + word_tokenize(sen)
        punctuation = re.compile(r'[-?!,":;.()| ]')
        words = [punctuation.sub("", word) for word in words]
        numbers = [('zero','0'),('one','1'),('two','2'),('three','3'),('four','4'),('five','5'),('six','6'),('seven','7'),('eight','8'),('nine','9')]
        match = re.search(r"""((\d+ ?(\,|and) ?)+\d+)""",question,re.I|re.M)
        if "greatest" in words and "divisible" in words and match:
            #type a problems
            match_string = match.group(0)
            m = False
            for number in numbers:
                if number[0] in words or number[1] in words:
                    m = int(number[1])
                    break
            match_string = match_string.replace(' ','')
            match_string = match_string.replace('and',',')
            series = match_string.split(',')
            for i in range(len(series)):
                series[i] = int(series[i])
            if not m:
                return {"error","could not understand the question"}
            else:
                return l.lcmNhcf_typeA(series,m)
        elif "greatest" in words and "leave" in words and "same" in words and "remainder" and match:
            match_string = match.group(0)
            match_string = match_string.replace(' ','')
            match_string = match_string.replace('and',',')
            series = match_string.split(',')
            for i in range(len(series)):
                series[i] = int(series[i])
            return l.lcmNhcf_typeB(series)
        elif "product" in words and("hcf" in words or "h.c.f" in words) and("greater" in words or "greatest" in words) and ("two" in words or "2" in words):
            product_index = words.index("product")
            product = False
            for index in range(product_index,len(words)):
                if words[index].isdigit():
                    product = int(words[index])
                    break
            hcf_index = False
            if "hcf" in words:
                hcf_index = words.index("hcf")
            else:
                hcf_index = words.index("h.c.f")
            hcf = False
            for index in range(hcf_index,len(words)):
                if words[index].isdigit():
                    hcf = int(words[index])
                    break
            if not(hcf and product):
                return {"error":"Could not understand the question"}
            else :
                return l.lcmNhcf_typeC(product,hcf)
        elif "greatest" in words and "dividing" in words and ("remainders" in words or "remainder" in words):
            dividing_index = words.index("dividing")
            dividing_list = []
            for word in words[dividing_index+1:]:
                if word.isdigit():
                    dividing_list.append(int(word))
                elif word == "and" or word == "":
                    pass
                else:
                    break
            if "remainders" in words:
                remainder_index = words.index("remainders")
            else:
                remainder_index = words.index("remainder")
            remainder_list = []
            for word in words[remainder_index+1:]:
                if word.isdigit():
                    remainder_list.append(int(word))
                elif word == "and" or word == "":
                    pass
                else:
                    break
            return l.lcmNhcf_typeD(dividing_list,remainder_list)
        elif ("lcm" in words or "l.c.m" in words) and ("hcf" in words or "HCF" in words) and("ratio" in words  or "ratios" in words) and ("number" in words or "numbers" in words):
            number_index = False
            if "number" in words:
                number_index = words.index("number")
            else:
                number_index = words.index("numbers")
            for number in numbers:
                if words[number_index - 1] == number[0] or words[number_index - 1] == number[1]:
                    number_index = int(number[1])
            ratio_index = False
            if "ratio" in words:
                ratio_index = words.index("ratio")
            else:
                ratio_index = words.index("ratios")
            if(words[ratio_index + 1] == "of"):
                ratio_index = ratio_index + 1
            ratios = []
            for word in words[ratio_index + 1:]:
                if word.isdigit():
                    ratios.append(int(word))
                else:
                    break
            if len(ratios) != 3:
                return {"error":"Invalid number of ratios present in question"}
            lcm = int(words[words.index("is") + 1])
            return l.lcmNhcf_typeE(ratios,lcm)
        elif "least" in words and "divided" in words and "remainder" in words and not "multiple" in words:
            divided_index  = words.index("divided") + 1
            remainder_index = words.index("remainder") + 1
            if not words[divided_index].isdigit():
                divided_index = divided_index + 1
            dividing_list = []
            for word in words[divided_index:]:
                if word.isdigit():
                    dividing_list.append(int(word))
                elif word == "and" or word == "":
                    pass
                else:
                    break
            if not words[remainder_index].isdigit():
                remainder_index = remainder_index + 1
            remainder = int(words[remainder_index])
            return l.lcmNhcf_typeF(dividing_list,remainder)
        elif ("factors" in words or "factor" in words) and "lcm" in words and "hcf" in words and ("larger" in words or "largest" in words):
            hcf = False
            hcf_match = re.search(r"is (\d+)",question,re.I|re.M)
            if hcf_match:
                hcf = int(hcf_match.group(1))
            dividing_list = []
            for word in words[words.index("are") + 1:]:
                if word.isdigit():
                    dividing_list.append(int(word))
                elif word == "and" or word == "":
                    pass
                else:
                    break
            number_index = False
            if "number" in words:
                number_index = words.index("number")
            else:
                number_index = words.index("numbers")
            for number in numbers:
                if words[number_index - 1] == number[0] or words[number_index - 1] == number[1]:
                    number_index = int(number[1])
            return l.lcmNhcf_typeG(number_index,hcf,dividing_list)
        elif "gcd" in words or "hcf" in words or (("greatest" in words or "highest" in words) and "common" in words and ("divisor" in words or "factor" in words)):
            match = re.findall(r"(\d+(\.\d+)?)",question)
            numbers = []
            for num in match:
                numbers.append(float(num[0]))
            return l.lcmNhcf_typeH(numbers)
        elif "least" in words and "remainder" in words and "divided" in words and "multiple":
            multiple_index = words.index("multiple")+1
            if not words[multiple_index].isdigit():
                multiple_index = multiple_index + 1
            multiple_index = int(words[multiple_index])
            divided_index  = words.index("divided") + 1
            remainder_index = words.index("remainder") + 1
            if not words[divided_index].isdigit():
                divided_index = divided_index + 1
            dividing_list = []
            for word in words[divided_index:]:
                if word.isdigit():
                    dividing_list.append(int(word))
                elif word == "and" or word == "":
                    pass
                else:
                    break
            if not words[remainder_index].isdigit():
                remainder_index = remainder_index + 1
            remainder = int(words[remainder_index])
            return l.lcmNhcf_typeI(multiple_index,remainder,dividing_list)
        elif "lcm" in words or (("least" in words or "lowest" in words) and "common" in words and "multiple" in words):
            match = re.findall(r"(\d+(\.\d+)?)",question)
            numbers = []
            for num in match:
                numbers.append(float(num[0]))
            return l.lcmNhcf_typeJ(numbers)
