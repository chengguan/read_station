# Source: https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html

import re

f = open('station.config', 'r') 
o = f.readlines()

for each in o:
    each.replace('\t', '    ')
    ip = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", 
                    each)
    comments = re.findall(r"[ \t]+[\x20-\x7E]+", each)
    if ip:
        print(f"Valid IP found: {ip}")
        #comment.pop(0)
        for each_comment in comments:
            print(f"Comment: {each_comment.lstrip()}")
