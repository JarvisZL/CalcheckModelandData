import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def rename():
    filepath="C:/Users/JarvisZhang/Desktop/tmp/Numerals/"
    path = os.listdir(filepath)

    for eachpath in path:
        if eachpath == "0":
            child = os.path.join("%s%s" % (filepath, eachpath))
            subpath = os.listdir(child)
            cnt = 0
            for filename in subpath:
                oldname = child + os.sep + subpath[cnt]
                newname = child + os.sep + "0-" + str(cnt) + ".png"
                os.rename(oldname,newname)
                print(oldname,"======>",newname)
                cnt = cnt + 1

if __name__ == "__main__":
    rename()