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
from pathlib import Path
import nltk
import string
from nltk.corpus import stopwords

if __name__ == '__main__':
parser = argparse.ArgumentParser(description='Top-100 words')
parser.add_argument('path', type=Path, help='Input text directory')
args = parser.parse_args()
path = args.path
document = open(path, "r")
text = document.read()

stopwords = set(nltk.corpus.stopwords.words('english'))
punctuation = string.punctuation
text_manipulation = text.split()
text_manipulation2 = [word for word in text_manipulation if word.lower() not in stopwords]
text_manipulation2 = [word for word in text_manipulation2 if word.lower() not in punctuation]
clean_text = ' '.join(text_manipulation2)

words = []
words = words + clean_text.split()
most_common_words = collections.Counter(words).most_common(100)
print(most_common_words)
