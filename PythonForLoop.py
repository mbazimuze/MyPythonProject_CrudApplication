# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print("\n")

# Another For loop

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print("\n")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print("\n")

# The continue statement, also borrowed from C, continues with the next iteration of the loop

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

print("\n")

print("For loop with objects and its values")

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print("\n")

print("For loop with serial number and its values")

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print("\n")

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy life', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print("\n")

for i in reversed(range(1, 10, 2)):
    print(i)

print("\n")

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

print("\n")

# Using set() on a sequence eliminates duplicate elements.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)