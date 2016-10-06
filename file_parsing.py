import os
os.chdir('/Users/Akki/Projects/Videos/') #To change the current directory
print os.getcwd() #To print the current working directory
for f in os.listdir():  #same as ls; lists the content of cwd
    filename, extension = os.path.splittext(f) #gives the tuple of the filename and extension
    f_title,f_course,f_num=filename.split('-') #splits the filename into 3 parts
    f_title=f_title.strip()
    f_course=f_course.strip() #strip() will remove the spaces before and after
    f_num=f_num.strip()[:1].zfill(2) #[:1] will remove the '#' before each number and zfill(2) will make all the numbers 2 digit wide
    print '{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext)
