#reads file and parses it for particular pattern
def pars():
    file=open("textfile.txt", 'r')
    lines=file.readlines()
    file.close()
    was_count=0
    is_count=0
    for line in lines:
        words=line.split(' ')
        for word in words:
            if word=='was':
                was_count+=1
            elif word=='is':
                is_count+=1

    print 'was: '+ str(was_count)
    print 'is:' + str(is_count)
