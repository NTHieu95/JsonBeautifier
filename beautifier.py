import glob
import json
import os
import errno

for filename in glob.glob('Your directory/**/*.json', recursive=True):
    file = open(filename,'r')
    if not os.path.exists(os.path.dirname('out\\'+filename)):
        try:
            os.makedirs(os.path.dirname('out\\'+filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    output = open('out\\'+filename,'w')
    text = file.read()

    text=json.dumps(json.loads(text), indent=4)
    print(file.read())
    file.close()
    output.write(text.encode('ascii').decode('unicode-escape'))
    output.close()