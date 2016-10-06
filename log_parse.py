#program to parse through log files and return entries related to a given keyword.
#The keyword could be a ip addr, protocol, error; it will return the line containing that keyword.

import os

def log_parse(directory, key_word):
    entries=[]
    for root, dir, files in os.walk(directory):
        for f in files:
            with open(f, 'r') as rf:
                lines =rf.readlines()
                for line in lines:
                    line=line.strip().lower()
                    words=line.split(' ')
                    for word in words:
                        if word == key_word:
                            entries.append(line)

    print '/n'.join(entries)
