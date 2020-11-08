"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""
import collections
import argparse
import os
#import nltk
from nltk.corpus import stopwords

parser = argparse.ArgumentParser(description='Top-100 words')
parser.add_argument('dir', type=str, help='Input text directory')
args = parser.parse_args()
path = args.path
document = open(path)
text = document.read()
#stopwords = set(nltk.corpus.stopwords.words('english'))
#need to delete stopwords from text later
words = []
words = words + text.split()
#print(words)
#dict_of_words = { i: words[i] for i in range(0, len(words)) }
#print(dict_of_words)
most_common_words = collections.Counter(words).most_common(100)
print(most_common_words)
if __name__ == '__main__':
    pass
