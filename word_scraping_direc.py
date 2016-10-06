#program to find keyword in a directory and return its count and the filename its in

import os

def dir_scrapin(directory, key_word):
    Key_word_count=0
    file_names=[]
    for root, dir, files in os.walk(directory):
        for f in files:
            with open(f,'r') as rf:
                lines=rf.readlines()
                for line in lines:
                    line=line.strip().lower()
                    if line.find(key_word)!=-1:
                        Key_word_count+=1
                        file_names.append(f)

    return Key_word_count
    return file_names 
