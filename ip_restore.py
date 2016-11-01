def is_octet_valid(octet_string):
    if len(octet_string) <1: return False
    elif str(int(octet_string)) != octet_string or int(octet_string) > 255: return False
    return True





def restore_ip_iterative(raw_string):
    restored_ip =[]
    for a in xrange(1,4):
        if len(raw_string[a:]) > 9:continue
        for b in xrange(1,4):
            if len(raw_string[a+b:]) > 6:continue
            for c in xrange(1,4):
                d = len(raw_string[a+b+c:])
                if d > 3:continue
                if a+b+c+d == len(raw_string):
                    octetA = raw_string[:a]
                    octetB = raw_string[a:a+b]
                    octetC = raw_string[a+b:a+b+c]
                    octetD = raw_string[a+b+c:]
                    if is_octet_valid(octetA) and is_octet_valid(octetB) and is_octet_valid(octetC) and is_octet_valid(octetD):
                        restored_ip.append(octetA + "." + octetB + "." + octetC+ "." + octetD)
                            
    print restored_ip



    
restore_ip_iterative('2552551119')
