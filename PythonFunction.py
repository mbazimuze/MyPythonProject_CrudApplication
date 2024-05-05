
# function one
def greet():
    print("Hello")
    print("Good Morning")

#executing a function

greet()

# passing two arguments
def add(x,y):
    c = x + y
    print(c)
    return c

add(4,1)

# keep output to a variable. This may be used to insert into the DB
results = add(4,1)
print(results)

def add_sub(x,y):
    c = x + y
    d = x-y
    return c,d
# return multiple outputs
results1, results2 = add_sub(4,1)

print(results1,results2)

def update(x):
    x = 8;
    print("a", x)

b = 10
update(b)

print("b",b)








