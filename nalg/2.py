import wikipedia
import striprtf
from striprtf.striprtf import rtf_to_text


def prefix(s):
    mx = 0
    s1 = ''
    s2 = ''
    for i in range(len(s)//2):
        s1 += s[i]
        s2 = s[len(s)-i-1] + s2
        if s1 == s2:
            mx = i+1
    return mx


def kmp(s, h):
    pr = [0]
    for i in range(len(s)):
        pr.append(prefix(s[:i+1]))
    h = ' ' + h
    s = ' ' + s
    j = 0
    i = 1
    cnt = 0
    while i < len(h):
        if h[i] == s[j+1]:
            if j+1 == len(s)-1:
                cnt += 1
                j = 0
                i += 1
            else:
                j += 1
                i += 1
        elif j != 0:
            j = pr[j]
        else:
            i += 1
    return cnt


def copypaste(txt, wikiname='Логика', language='ru'):
    wikipedia.set_lang(language)
    wikitxt = wikipedia.page(wikiname).content.lower()
    sym = ',.-=!:()—[];"' + "'"
    for i in sym:
        wikitxt = wikitxt.replace(i, '')
        txt = txt.replace(i, '')
    txtarr = txt.split()

    counter = ''

    for i in txtarr:
        if kmp(i, wikitxt):
            counter += '1' * len(i) + '0'
        else:
            counter += ' '

    counterArr = counter.split()

    copied = 0
    for i in counterArr:
        if kmp('0', i) >= 3:
            copied += kmp('1', i)
    return (copied / len(txt)) * 100


with open('C:/Users/warfa/Downloads/Домашнее задание 1/Логика.rtf', encoding='utf-8') as f:
    a = ''.join(f.readlines())
    text = rtf_to_text(a)
    print(round(copypaste(text), 2), '%')
