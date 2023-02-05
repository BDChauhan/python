def outer(text):
    t = text
    def inner():
        print(t)
    return inner

f = outer("Hey")
f()
# if __name__ == '__main__':
#     outer('Heyy')