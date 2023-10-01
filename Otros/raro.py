import time

def medir(arg,callback):
    t0=time.time()
    try:
        res=callback(arg)
    except:
        res=0
    t1=time.time()
    return ((t1-t0)*1000), res