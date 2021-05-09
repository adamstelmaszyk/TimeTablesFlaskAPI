from xml.etree.ElementTree import tostring

import lxml.etree
import lxml.html
import requests
from lxml import etree


class BaseLinks:

    def __init__(self):
        url = "http://plan.ckziu-elektryk.pl/lista.html"
        html = requests.get(url).text
        root = lxml.html.fromstring(html)
        self.ul = root.xpath('///ul')

    def classes_links(self):
        return_dictionary = dict()
        for item in self.ul[0]:  # PLANY KLAS
            for a in item:
                return_dictionary[a.text_content()] = a.attrib['href']
        print(return_dictionary)
        return return_dictionary

    def teachers_links(self):
        return_dictionary = dict()
        for item in self.ul[1]:  # PLANY NAUCZYCIELI
            for a in item:
                return_dictionary[a.text_content()] = a.attrib['href']
        print(return_dictionary)
        return return_dictionary

    def rooms_links(self):
        return_dictionary = dict()
        for item in self.ul[2]:  # PLANY SAL LEKCYJNYCH
            for a in item:
                return_dictionary[a.text_content()] = a.attrib['href']
        print(return_dictionary)
        return return_dictionary

