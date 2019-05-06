import os
import shutil
import errno


def selectiveCopy(src, dst, ext):
    try:
        os.mkdir(dst)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    for folderName, subfolders, filenames in os.walk(src):
        print('The current folder is ' + folderName)

        for filename in filenames:
            if filename.endswith('{}'.format(ext)):
                print('FILE INSIDE ' + folderName + ': ' + filename)
                shutil.copy(os.path.join(folderName, filename), dst)


selectiveCopy('source', 'destination', 'extention')
