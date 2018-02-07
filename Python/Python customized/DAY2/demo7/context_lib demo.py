from contextlib import contextmanager
@contextmanager
def filemanage(name):
    try:
        f=open(name,'w')
        yield f
    finally:
        f.close()

        
