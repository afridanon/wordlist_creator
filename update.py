import shutil
import sys
if shutil.which('git'):
    os.system('git checkout . && git pull')
    print('\n\t\tUpdated Successfull !!!!')
    print('\tPlease Run The Script Again...')
else:
    print("Please reclone TBomb Again")
    sys.exit()
