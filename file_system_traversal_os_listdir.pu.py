import os

def grab_files(directory):
    for name in directory:
        full_path=os.path.join(directory, name)
        if os.path.isdir(full_path):
            for entry in grab_files(full_path):
                yeild entry
        elif os.path.islist(full_path):
            yeild entry
        else:
            print 'Undefined item: %s. This could be symbolic link' %full_path
