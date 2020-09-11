x=6
print(x)
def example():
    globx=x
    print(globx)
    globx+=5
    return globx

x=example()
print(x)
