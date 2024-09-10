#Sample .py upload

#Caching example
def cache(fun):
    cache_dict={}
    def wrapper(*args):
        if args in cache_dict:      # Cache pull if possible 
            return cache_dict[args]
        result = fun(*args)
        cache_dict[args]=result
        return result
    return wrapper

@cache
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)

print(fibo(100))
print(fibo(200))
print(fibo(0))
