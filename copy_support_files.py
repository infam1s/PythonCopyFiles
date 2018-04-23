import os
import shutil
from distutils import dir_util
import errno
import time


src_dir1 = "C:\\Drop"
dst_dir1 = "C:\\Users\\anthony.helmey\\PBS_Support\\Systems and Projects\\USA"
US_src_files = os.listdir(src_dir1)

src_dir2 = "C:\\Drop2"
dst_dir2 = "C:\\Users\\anthony.helmey\\PBS_Support\\Systems and Projects\\Canada"
CA_src_files = os.listdir(src_dir2)

errors = []

# walk these sub directories and the ones within
subdir1 = [s[0] for s in os.walk(src_dir1)]
subdir2 = [p[0] for p in os.walk(src_dir2)]


def progress(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='X'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / total))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


print("Copying tree %s to %s" % (src_dir1, dst_dir1))
for f in US_src_files:
    try:
        dir_util.copy_tree(src_dir1, dst_dir1)
        #print("found this: %s" % g)
        #shutil.copy2(os.path.join(src_dir1, g), dst_dir1)
        #print("%s is being copied from %s to %s" % (g, src_dir1, dst_dir1))
        #progress(0, 10, prefix='Progress:', suffix='Complete')

    except shutil.Error as err:
        errors.extend(err.args[0])
        # if a file exists
        if err.errno == errno.EEXIST:
            shutil.copy2(src_dir1, dst_dir1)
        if err.errno == errno.ENOENT:
            shutil.copy2(src_dir1, dst_dir1)
    except dir_util.DistutilsFileError as errx:
        shutil.copy2(os.path.join(src_dir1, f), dst_dir1)

print("Copying tree %s to %s" % (src_dir2, dst_dir2))
for x in CA_src_files:
    try:
        dir_util.copy_tree(src_dir2, dst_dir2)
        #print("found this: %s" % g)
        #shutil.copy2(os.path.join(src_dir1, g), dst_dir1)
        #print("%s is being copied from %s to %s" % (g, src_dir1, dst_dir1))
        #progress(0, 10, prefix='Progress:', suffix='Complete')
        #for f, US_src_files in f:
        #    time.sleep(1)
        #    progress(i + 1, 10, prefix='Progress:', decimals=2, suffix='Complete')

    except shutil.Error as err:
        errors.extend(err.args[0])
        # if a file exists
        if err.errno == errno.EEXIST:
            shutil.copy2(src_dir1, dst_dir1)
        if err.errno == errno.ENOENT:
            shutil.copy2(src_dir1, dst_dir1)
    except dir_util.DistutilsFileError as errx:
        shutil.copy2(os.path.join(src_dir1, x), dst_dir1)

if src_dir1 == dst_dir1 and src_dir2 == dst_dir2:
    print("all files have been copied")



