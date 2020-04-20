import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


samplelist=["Sample026","Sample027","Sample028","Sample029","Sample030","Sample031"]


def get1045img():
    filepath="C:/Users/JarvisZhang/Desktop/calculator/"
    path = os.listdir(filepath)

    for eachpath in path:
        if eachpath not in samplelist:
            continue
        child = os.path.join("%s%s" % (filepath, eachpath))
        cnt = 0
        for filename in os.listdir(child):
            if cnt < 1045:
                cnt = cnt + 1
                continue
            os.remove(os.path.join("%s/%s" % (child,filename)))



if __name__ == '__main__':
    get1045img()