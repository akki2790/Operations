#reads file and parses it for particular pattern with 'line.find()'
def parse(filename):
    file = open(filename, 'r')
    lines=file.readlines()
    file.close()

    yes_count=0
    no_count=0
    
    for line in lines:
        line=line.strip().lower()
        if line.find('yes')!=-1 and len(line)==3:
            yes_count+=1
        if line.find('no')!=-1 and len(line)==2:
            no_count+=1

    print 'Yeses: ' + str(yes_count)
    print 'Noes: ' + str(no_count)

    
