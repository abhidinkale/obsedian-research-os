import re

def parse_wikilinks(text):
    return re.findall(r'\[\[(.*?)\]\]', text)
