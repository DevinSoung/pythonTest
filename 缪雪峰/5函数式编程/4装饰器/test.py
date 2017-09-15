import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('begin %s():' % func.__name__)
#         f1=func(*args,**kw)
#         print('end %s():' % func.__name__)
#         return f1
#     return wrapper
#
# @log
# def now():
#     print('2017-9-14')
#
# now()

def log():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % ('123',func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log
def now():
    print('2017-9-14')

now()