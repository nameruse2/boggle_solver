import itertools
letters = ["a", "e", "h", "d", "u", "m", "l", "s", "e"]
combos = []
words = []

for L in range(0, len(letters)+1):
    for subset in itertools.permutations(letters, L):
        combos.append(subset)

for i in combos:
    tester=''.join(i)
    words.append(tester)


for i in words:
    print(i)
