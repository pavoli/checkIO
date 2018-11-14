# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

def between_markers(text, begin, end):
    if begin is None and end is None:
        return text

    new_text = text
    pos_1 = new_text.find(begin)
    pos_2 = new_text.find(end)

    if pos_1 == -1:
        pos_1 = 0

    if pos_2 == -1:
        pos_2 = len(new_text)

    if pos_1 > pos_2:
        new_text = ''

    if begin in new_text:
        new_text = new_text.split(begin)[1]

    if end in new_text:
        new_text = new_text.split(end)[0]

    return new_text

''' best solition as i ever see...
def between_markers(text, begin, end):
    a = text.find(begin) + len(begin) if begin in text else 0
    b = text.find(end) if end in text else len(text)
    return text[a:b]
'''


if __name__ == '__main__':
    #assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    #assert between_markers("<head><title>My new site</title></head>", "<title>", "</title>") == "My new site", "HTML"
    #assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    #assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    #assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    #assert between_markers("No <hi> one", ">", "<") == '', 'Wrong direction2'