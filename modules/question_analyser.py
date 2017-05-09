#!/usr/bin/python3
import json
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import pickle
class QuestionAnalyser:
    def __init__(self,location,filenames,labels):
        self.__loc = location
        self.__fnames = filenames
        self.__labels  = labels

    def __tokenize(self,question):
        total_words = []
        sentences = sent_tokenize(question)
        for sentence in sentences:
            words = word_tokenize(sentence)
            total_words += words
        return total_words

    def __preprocess_question(self,question):
        stop_words = self.__stop_words
        lemmatizer = WordNetLemmatizer()
        words = self.__tokenize(question)
        punctuation = re.compile(r'[-.?!,":;()|0-9 ]')
        words = [punctuation.sub("", word) for word in words]
        words = [w.lower() for w in words]
        words = [w for w in words if not w in stop_words and not w.isdigit()]
        words = [lemmatizer.lemmatize(word).lower() for word in words ]
        return words

    def __preprocess(self):
        data = {}
        if len(self.__fnames) != len(self.__labels):
            print("Filenames and labels are not equal")
            sys.exit(0)
        for index in range(len(self.__fnames)):
            filename = self.__loc + "/" + self.__fnames[index]
            with open(filename,'r') as f:
                data[self.__labels[index]] = json.load(f)
        preprocessed_data ={}
        stop_words = set(stopwords.words('english'))
        stop_words.add('the')
        stop_words.add('.')
        stop_words.add('?')
        stop_words.add(',')
        self.__stop_words = stop_words
        for label in data:
            questions = data[label]
            preprocessed_questions = []
            for question in questions:
                words = self.__preprocess_question(question)
                preprocessed_questions.append(words)
            preprocessed_data[label] = preprocessed_questions
        self.__preprocessed_data = preprocessed_data
        self.__data = data

    def __get_feature_set(self):
        feature_set = []
        for category in self.__preprocessed_data:
            all_words = []
            for preprocessed_question in self.__preprocessed_data[category]:
                all_words+= preprocessed_question
            all_words = nltk.FreqDist(all_words)
            most_com = []
            for (name,times) in all_words.most_common(30):
                most_com.append(name)
            feature_set = feature_set + most_com
        self.__feature_set = set(feature_set)

    def __get_features(self,question):
        words = set(question)
        word_features = self.__feature_set
        features = {}
        for w in word_features:
            features[w] = (w in words)

        return features



    def train(self):
        self.__preprocess()
        self.__get_feature_set();
        feature_sets = []
        for category in self.__preprocessed_data:
            for question in self.__preprocessed_data[category]:
                features = self.__get_features(question)
                feature_sets.append((features,category))
        del self.__preprocessed_data
        del self.__data
        #here the classifier algorithm should come
        classifier = nltk.NaiveBayesClassifier.train(feature_sets)
        nb = open("nb.pickle","wb")
        pickle.dump(classifier, nb)
        nb.close()
        fs = open("fs.pickle","wb")
        pickle.dump(self.__feature_set,fs)
        fs.close()


    def predict(self,question):
        nb = open("nb.pickle","rb")
        classifier = pickle.load(nb)
        nb.close()
        fs = open("fs.pickle","rb")
        self.__feature_set = pickle.load(fs)
        fs.close()
        stop_words = set(stopwords.words('english'))
        stop_words.add('the')
        stop_words.add('.')
        stop_words.add('?')
        stop_words.add(',')
        self.__stop_words = stop_words
        words = self.__preprocess_question(question)
        question_features = self.__get_features(words)
        return classifier.classify(question_features)
