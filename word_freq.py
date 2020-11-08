"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""
import os
import argparse
import nltk
from nltk.corpus import stopwords
parser = argparse.ArgumentParser(description='Top-100 words')
parser.add_argument('dir', type=str, help='Input text directory')
args = parser.parse_args()
if __name__ == '__main__':
    pass
