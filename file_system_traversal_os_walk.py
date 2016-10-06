import os

for root, dir, files in os.walk(path):
    for name in files:
        print os.path.join(root, name)
