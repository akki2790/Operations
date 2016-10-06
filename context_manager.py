#file parsing using Context Manager
#with context manager we can work on a file within that loop and not worry about having to close the file after we are done.


#print out the content of the file
with open('test.txt', 'r') as f:
    f_content=f.read()
    print f_content

            #OR

with open('test.txt', 'r') os f:
    for line in f:
        print line


#grabbing limited number of characters from the file. 100 characters in this case
with open('text.txt', 'r') as f:
    f_chunk=f.read(100)
    print f_chunk


#if the file is too big, the variable holding the content of the file will become too big and working on it can be slow.
#to prevent this we can read the content in chunks and then work on it
with open('text.txt', 'r') as f:
    chunk=100
    f_content=f.read(chunk)
    while len(f_content)>0:
        print f_content
        f_content=f.read(chunk)

#read from one file and write in another
with open('text.txt', 'r') as rf:
    with open('text.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

#copying a picture file
with open('image.jpg', 'rb') as ri:
    with open('image_copy.jpg', 'wb') as wi:
        for line in ri:
            wi.write(line)

#copying a image file in chunks
with open('image.jpg', 'rb') as ri:
    with open('image_copy.jpg', 'wb') as wi:
        chunk=512
        ri_chunk=ri.read(chunk)
        while len(ri_chunk)>0:
            wi.write(ri_chunk)
            ri_chunk=ri.read(chunk)




            
