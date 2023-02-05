# to add extra features to existing functions!!
# to change behavior of function/obj at compile time itself



# lets assume that div fun is not here and we cant modify it
# and we need condition that a>b else swap a & b

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

# smart_div is taking fun as arg
# inner is changing code/ changing the way div works

# div1 = smart_div(div)

@smart_div
def div(a,b):
    print(a/b)
    

# div(2,4)
# div1(2,4)
